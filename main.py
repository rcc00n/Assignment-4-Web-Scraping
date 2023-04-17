"""
Created by Zlata Mstyslavska (Part A), Vadim Rudenko (Part B and combining code in one file) and Harsh Darji (Part C)
For AUSCI 135
16 April 2023
"""
from urllib.request import urlopen
import urllib.request
import pycountry
import re
import ssl
import certifi


def provinceScraper(url: str) -> dict[str: int]:
    """
        Function to scrape the data from the webpage and get the exact number of occurrence of each Province or Territory
        on the page. Also sort the dict with the numbers of occurrences of Provinces form the highest occurrence to the lowest.

        :param url: url of the web page to be scraped
        :return: sorted dict with the key: name of Province/Territory and value: number of occurrence
    """
    text = str(urlopen(
        url).read())  # open the url, get the web page content in bytes(with HTML tags) and converts it to string

    # list of all abbreviations of the Provinces and numbers of occurrences on the page
    provinces = [[["Alberta", "AB", "Alb."], 0],
                 [["British Columbia", "BC", "B.C."], 0],
                 [["Manitoba", "MB", "Man."], 0],
                 [["New Brunswick", "NB", "N.B."], 0],
                 [["Newfoundland", "NL", "N.L."], 0],
                 [["Labrador", "NL", "N.L."], 0],
                 [["Northwest Territories", "NT", "N.W.T."], 0],
                 [["Nova Scotia", "NS", "N.S."], 0],
                 [["Nunavut", "NU", "Nvt."], 0],
                 [["Ontario", "ON", "Ont."], 0],
                 [["Yukon", "YT", "Y.T."], 0],
                 [["Saskatchewan", "Sask.", "S.K."], 0],
                 [["Prince Edward Island", "P.E.", "P.E.I."], 0],
                 [["Quebec", "Q.C.", "Que."], 0],
                 ]

    # loop to count the number of occurrences of each Province and Territory on the page(including abbreviations)
    for province in range(len(provinces)):
        for name in provinces[province][0]:
            provinces[province][1] += text.count(name)  # add the number of occurrence of specific Province with its //
            # abbreviation to the current number
    provinces = {key[0]: value for key, value in
                 provinces}  # Converting the list of lists of the Provinces and their //
    # abbreviations and number of occurrences to the dict with key: full name of the Province/Territory and value: number of occurrence
    return dict(
        sorted(provinces.items(), key=lambda item: item[1], reverse=True))  # returns the sorted dictionary of provinces


def displayInfo(cbcDict: dict[str: int], windspeakerDict: dict[str: int]) -> None:
    """
       Displays the table with the name of the province and number of occurrence on specific web page and total occurrence on both pages.
       :param cbcDict: sorted dict with number of occurrences of provinces and their name from the CBC News webpage
       :param windspeakerDict: sorted dict with number of occurrences of provinces and their name from the Windspeaker News webpage
       :return: None
    """
    total_mentioned = {key: (value + windspeakerDict[key]) for key, value in
                       cbcDict.items()}  # creates the dict with //
    # total numbers of occurrence of province names on both webpages

    print("Province/Territory       CBC         WindS.      Total")
    for key, value in cbcDict.items():
        print(
            f"{key:<25} {value:<12} {windspeakerDict[key]:<12} {total_mentioned[key]}")  # displays the table in the console in the columns with specific alignment
    print(
        f"The province/territory most in the news is: {list(total_mentioned.keys())[0]}")  # Displays the province with the highest number of occurrences



def clean_country_name(country) -> str:
    """
        Returns country name and cleans it if it's needed
        :param country: country that the scraper found on a page
        :return: country name
    """
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
    """
        Creates the list of countries via using pycountry
        :return: None
    """
    countries = list(pycountry.countries)
    return [clean_country_name(country.name) for country in countries]


def get_text_of_the_page(url: str) -> str:
    """
        Remove tags form html page
        :param url: url address of the page we are scraping
        :return: text of the page without tags
    """
    response = urllib.request.urlopen(url)
    html_content = response.read().decode('utf-8')
    return re.sub('<[^>]*>', ' ', html_content)


def country_occurrence(page_text: str, country_names: list) -> dict:
    """
        This function counts occurance of each country in the text via using regular expressions ignoring the case
        :param page_text: string with a text of our web page
        :param country_names: list of countries
        :return: dictionary with counted countries, where name of countries are keys
    """
    country_counts = {}
    for country in country_names:
        count = len(re.findall(r'\b' + re.escape(country) + r'\b', page_text, re.IGNORECASE))
        if count > 0:
            country_counts[country] = count
    return country_counts


def sort_country_counts(country_counts: dict):
    """
        This function sorts the dictionary of countries
        :param country_counts: dictionary with counted countries, where name of countries are keys
        :return: sorted dictionary with counted countries, where name of countries are keys
    """
    return sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

def remove_head_prepositions(url: str) -> list:
    '''
    :param url: url of the website to scrape
    :return: stage1_filter - list of words on website without head of the website
            and prepositions
    '''

    prepositions = [
        'aboard', 'about', 'above', 'across', 'after', 'against', 'along', 'amid',
        'among', 'anti', 'around', 'as', 'at', 'before', 'behind', 'below',
        'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by',
        'concerning', 'considering', 'despite', 'down', 'during', 'except',
        'excepting', 'excluding', 'following', 'for', 'from', 'in', 'inside', 'into',
        'like', 'minus', 'near', 'of', 'off', 'on', 'onto', 'opposite', 'outside',
        'over', 'past', 'per', 'plus', 'regarding', 'round', 'save', 'since', 'than',
        'through', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike',
        'until', 'up', 'upon', 'versus', 'via', 'with', 'within', 'without'
    ]

    myRequest = urllib.request.Request(url)  # Making my Request object
    response = urllib.request.urlopen(
        myRequest, context=ssl.create_default_context(cafile=certifi.where()))
    html_content = response.read().decode('utf-8')

    page_without_head = re.sub('<[^>]*>', ' ', html_content)

    list_of_page = page_without_head.split()

    stage1_filter = []

    for i in list_of_page:
        # remove all words greater than 4 characters and less than 20 characters
        # and not in prepositions to be appended to stage1_filter
        if (len(i) > 4) and (len(i) < 20) and (i not in prepositions):
            stage1_filter.append(i)

    # print(stage1_filter)

    return stage1_filter


def combine_words(remove_head_prepositions__: list) -> list:
    '''
    :param remove_head_prepositions__: list returned by remove_special_chars
    :return: remove_head_prepositions__ - list of words on website without head
                                      of the website, prepositions and special
                                      characters.
    '''

    i = 0

    while i < len(remove_head_prepositions__):

        # combining some common words
        if remove_head_prepositions__[i] == 'Prime' and remove_head_prepositions__[i + 1] == 'Minister':
            j = remove_head_prepositions__[
                i + 1].replace("Minister", 'Prime-Minister')
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        elif remove_head_prepositions__[i] == 'Justin' and remove_head_prepositions__[i + 1] == 'Trudeau':
            j = remove_head_prepositions__[
                i + 1].replace("Trudeau", 'Justin-Trudeau')
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        elif remove_head_prepositions__[i] == 'British' and remove_head_prepositions__[i + 1] == 'Columbia':
            j = remove_head_prepositions__[
                i + 1].replace("Columbia", 'British-Columbia')
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        elif remove_head_prepositions__[i] == 'First' and remove_head_prepositions__[i + 1] == 'Nations':
            j = remove_head_prepositions__[i + 1].replace("Nation", 'First-Nations')
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        elif (remove_head_prepositions__[i] == 'machine' and remove_head_prepositions__[i + 1] == 'learning'):
            j = remove_head_prepositions__[
                i + 1].replace("learning", 'machine-learning')
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        elif remove_head_prepositions__[i] == 'Trudeau':
            j = remove_head_prepositions__[i].replace("Trudeau", "Justin-Trudeau")
            remove_head_prepositions__.pop(i)
            remove_head_prepositions__.append(j)
            i -= 1

        i += 1


    return remove_head_prepositions__


def remove_special_chars(combinie_words__: list) -> list:
    '''
    :param combinie_words__: list returned by remove_head_prepositions
    :return: stage2_filter - list of words on website without head of the website,
                            prepositions and special characters
    '''

    stage2_filter = [re.sub('[^a-zA-Z0-9]+', '', _)
                     for _ in combinie_words__]

    i = 0
    while i < len(stage2_filter):
        if 'ian' in stage2_filter[i]:
            # replacing words ending with 'ian/ians' with 'a'
            # NOTE: this is shaky -> needs to external libraries
            # Words like 'Russians' are converted to 'Russa' which
            # is due to the restrictions placed on the kind of tools
            # to be used for cleaning strings.
            if 'ians' in stage2_filter[i]:
                j = stage2_filter[i].replace('ians', 'a')
                stage2_filter.pop(i)
                stage2_filter.append(j)
                i -= 1
            j = stage2_filter[i].replace('ian', 'a')
            stage2_filter.pop(i)
            stage2_filter.append(j)
            i -= 1
        # replacing plural words with singular words
        if stage2_filter[i][-1] == 's':
            # NOTE: this part is a bit shaky -> might need external libraries
            # Words that are not plural (like indegenious, politics) are also
            # changed to indegeniou and politic
            k = stage2_filter[i][:len(stage2_filter[i]) - 1]
            stage2_filter.pop(i)
            stage2_filter.append(k)
            i -= 1
        i += 1


    return stage2_filter


def get_counts_words(remove_special_chars__: list) -> str:
    '''
    :param remove_special_chars__: list returned by combine_words
    :return: new line character
    '''

    # counts of each word as lists inside one big list (nested list)
    counts = [[x, remove_special_chars__.count(x)] for x in set(remove_special_chars__)]

    i = 0

    while i < len(counts):
        if counts[i][1] < 2:
            counts.pop(i)
            i -= 1
        i += 1

    # sorting the list in descending order of counts
    sorted_counts = sorted(counts, key=lambda x: x[1], reverse=True)

    print('WORD')
    print('_____________________________')
    print()
    for i in range(10):
        print(f"{sorted_counts[i][0]:<25} {sorted_counts[i][1]:<25}")

    return '\n'

def main(urls: list):

    # Part A:
    print("Part A:\n")
    cbcNews = provinceScraper("https://www.cbc.ca/news")  # Get the sorted dictionary of occurrence of each province//
    # territory from the CBC News webpage
    windSpeaker = provinceScraper(
        "https://windspeaker.com/")  # Get the sorted dictionary of occurrence of each province//
    # territory from the Windspeaker News webpage
    displayInfo(cbcNews, windSpeaker)  # Displays the table with all information
    print("\n")

    # Part B:
    print("Part B: \n" )
    url = 'https://www.cbc.ca/news/world'
    page_text = get_text_of_the_page(url)
    country_names = get_list_of_countries()
    country_counts = country_occurrence(page_text, country_names)
    sorted_countries = sort_country_counts(country_counts)
    print("Most talked about country:", sorted_countries[0][0])
    for country, count in sorted_countries:
        print(f"{country}: {count}")
    print("\n")

    print("Part C:")
    for url, website_name in urls.items():  # scraping all websites given
        print(f'The Most Frequent Words On {website_name} are:')
        print(get_counts_words(remove_special_chars(combine_words(remove_head_prepositions(url)))))


urls = {'https://www.cbc.ca/news': 'CBC', 'https://www.cbc.ca/news/world': 'CBC World',
        'https://windspeaker.com/': 'Windspeaker'}
main(urls)
