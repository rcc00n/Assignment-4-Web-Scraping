import urllib.request
import pycountry
import re
from typing import List, Dict


def clean_country_name(country: str) -> str:
    if country in ['US', 'U.S.', 'USA', 'U.S.A.', 'United States']:
        return 'United States'
    return country


def get_list_of_provinces() -> List[List[str]]:
    return [
        ["Alberta", "AB", "Alb."],
        ["British Columbia", "BC", "B.C."],
        ["Manitoba", "MB", "Man."],
        ["New Brunswick", "NB", "N.B."],
        ["Newfoundland", "NL", "N.L."],
        ["Labrador", "NL", "N.L."],
        ["Northwest Territories", "NT", "N.W.T."],
        ["Nova Scotia", "NS", "N.S."],
        ["Nunavut", "NU", "Nvt."],
        ["Ontario", "ON", "Ont."],
        ["Yukon", "YT", "Y.T."],
        ["Saskatchewan", "Sask.", "S.K."],
        ["Prince Edward Island", "P.E.", "P.E.I."],
        ["Quebec", "Q.C.", "Que."]
    ]


def get_list_of_countries() -> List[str]:
    countries = list(pycountry.countries)
    return [clean_country_name(country.name) for country in countries]


def get_text_of_the_page(url: str) -> str:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')
    return re.sub('<[^>]*>', ' ', html_content)


def region_occurrence(page_text: str, region_names: List[str]) -> Dict[str, int]:
    region_counts = {}
    for region in region_names:
        count = len(re.findall(r'\b' + re.escape(region) + r'\b', page_text, re.IGNORECASE))
        if count > 0:
            region_counts[region] = count
    return region_counts


def sort_region_counts(region_counts: Dict[str, int]) -> List:
    return sorted(region_counts.items(), key=lambda x: x[1], reverse=True)


def main():
    url = 'https://www.cbc.ca/news/world'
    page_text = get_text_of_the_page(url)

    province_names = get_list_of_provinces()
    province_counts = {}
    for province in province_names:
        province_counts[province[0]] = sum(
            region_occurrence(page_text, province).values()
        )
    sorted_provinces = sort_region_counts(province_counts)

    country_names = get_list_of_countries()
    country_counts = region_occurrence(page_text, country_names)
    sorted_countries = sort_region_counts(country_counts)

    print("Most talked about province:", sorted_provinces[0][0])
    print("Most talked about country:", sorted_countries[0][0])

    print("\nProvinces:")
    for province, count in sorted_provinces:
        print(f"{province}: {count}")

    print("\nCountries:")
    for country, count in sorted_countries:
        print(f"{country}: {count}")

if __name__ == "__main__":
    main()
