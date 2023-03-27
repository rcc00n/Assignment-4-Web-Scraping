# Assignment-4-Web-Scraping
a) Which Province/Territory is the most talked about in CBC news and
Windspeaker?:
Using information on the main page of both news sources, determine which of Canada’s
provinces or territories is most in the news. Print a table, in order from top to bottom,
sorted with the most talked about Province/Territory at the top. Also print a message
indicating which province/territory is most in the news. Note that a province/territory
may be referenced by name and also by a variety of abbreviations (e.g. “B.C.”, “BC”,
“British Columbia”). Count all of these references.
Here is a sample of the expected output (WindS is for Windspeaker)
Province/Territory CBC WindS. Total
British Columbia 103 89 192
Alberta 24 37 61
Yukon 12 8 20
Northwest Territories 3 5 8
Nunavut 0 1 1
⋮ ⋮ ⋮ ⋮
The province/territory most in the news is: British Columbia


b) Which country is the most talked about in CBC World?
You can get a list of country with this code:
import pycountry
countries = list(pycountry.countries)
for country in countries:
print(country.name)
Especially for the US, make sure you clean your data and consider the U.S. USA, U.S.A.
United States, etc. all together.


c) Which topics are the most talked about in CBC news, Windspeaker, and CBC
world:
Using the information on the main page of both news sources, determine the 10 most
referenced topics in the news. Do this by building a frequency dictionary of the words
that occur in the body of the page (i.e. not in the head). Further, clean the words so that:
1) html commands are not included
2) words shorter than four characters are not included (“B.C.” should be considered
4-characters)
3) words that are common prepositions are not included. Here is a list of common
prepositions
prepositions = ['aboard', 'about', 'above', 'across', 'after',
'against', 'along', 'amid', 'among', 'anti',
'around', 'as', 'at', 'before', 'behind', 'below',
'beneath', 'beside', 'besides', 'between',
'beyond', 'but', 'by', 'concerning', 'considering',
'despite', 'down', 'during', 'except',
'excepting', 'excluding', 'following', 'for', 'from',
'in', 'inside', 'into', 'like', 'minus',
'near', 'of', 'off', 'on', 'onto', 'opposite',
'outside', 'over', 'past', 'per', 'plus',
'regarding', 'round', 'save', 'since', 'than',
'through', 'to', 'toward', 'towards', 'under',
'underneath', 'unlike', 'until', 'up', 'upon', 'versus',
'via', 'with', 'within', 'without']

![image](https://user-images.githubusercontent.com/123768783/228080304-6f8b54bf-7d49-46c9-8317-bfd4cb4a1598.png)
