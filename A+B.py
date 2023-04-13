import urllib.request
import pycountry
import re


def clean_country_name(country) -> str:
    name_variants = {
        'US': 'United States',
        'U.S.': 'United States',
        'USA': 'United States',
        'U.S.A.': 'United States',
        'United States': 'United States',
        'UK': 'United Kingdom',
        'U.K.': 'United Kingdom',
        'United Kingdom': 'United Kingdom',
        'Russia': 'Russia',
        'Russian Federation': 'Russia',
        'Ukraine': 'Ukraine',
        'Republic of Ukraine': 'Ukraine'
    }

    if country in name_variants:
        return name_variants[country]
    return country


def get_list_of_countries():
    countries = list(pycountry.countries)
    country_names = [clean_country_name(country.name) for country in countries]
    country_names.extend(['Russian Federation', 'Republic of Ukraine'])
    return country_names


def get_text_of_the_page(url: str) -> str:
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')
    return re.sub('<[^>]*>', ' ', html_content)


def country_occurrence(page_text: str, country_names: list) -> dict:
    country_counts = {}
    for country in country_names:
        count = len(re.findall(r'\b' + re.escape(country) + r'\b', page_text, re.IGNORECASE))
        if count > 0:
            canonical_name = clean_country_name(country)
            country_counts[canonical_name] = country_counts.get(canonical_name, 0) + count
    return country_counts


def sort_country_counts(country_counts: dict):
    return sorted(country_counts.items(), key=lambda x: x[1], reverse=True)


def main():
    url = 'https://www.cbc.ca/news/world'
    page_text = get_text_of_the_page(url)
    country_names = get_list_of_countries()
    country_counts = country_occurrence(page_text, country_names)
    sorted_countries = sort_country_counts(country_counts)

    print("Most talked about country:", sorted_countries[0][0])

    for country, count in sorted_countries:
        print(f"{country}: {count}")


if __name__ == "__main__":
    main()
