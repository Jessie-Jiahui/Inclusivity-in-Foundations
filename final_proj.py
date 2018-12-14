## Final Project, Fall 2018
from bs4 import BeautifulSoup
from alternate_advanced_caching import Cache
import requests
from datetime import datetime
import json
import plotly.plotly as py
import plotly.graph_objs as go

from esteelauder_doublewear_data import *

## you can, and should add to and modify this class any way you see fit
## you can add attributes and modify the __init__ parameters,
##   as long as tests still pass
##
## the starter code is here just to make the tests run (and fail)
# data_pool = {
#     "esteelauder_doublewear": {
#         "years": {
#             "2013": ["1c1", "1n1", "1w1", "1w2", "2c1", "2n1", "2n2", "2w1", "3c1", "3n1", "3w1", "4c1", "4n1", "4w1", "5c1", "5n1", "5w1", "6c1", "6n1", "6w2"],
#             "2015": ["1c1", "1n1", "1n2", "1w1", "1w2", "2c1", "2c3", "2n1", "2w1", "2w2", "3c1", "3c2", "3n1", "3n2", "3w1", "3w2", "4c3", "4n1", "4n2", "4w1", "4w2", "5c1", "5n1", "5n2", "5w1", "5w2", "6c1", "6c2", "6n1", "6w1"],
#             "2016": ["1c1", "1n1", "1n2", "1w1", "1w2", "2c0", "2c1", "2c3", "2n1", "2w0", "2w1", "2w2", "3c1", "3c2", "3n1", "3n2", "3w1", "3w2", "4c3", "4n1", "4n2", "4w1", "4w2", "5c1", "5n1", "5n2", "5w1", "5w2", "6c1", "6c2", "6n1", "6n2", "6w1", "6w2", "7c1", "7n1", "7w1", "8n1"],
#             "2018.3": ["1c0", "1c1", "1n1", "1n2", "1w1", "1w2", "2c0", "2c1", "2c3", "2n1", "2n2", "2w0", "2w1", "2w2", "3c1", "3c2", "3n1", "3n2", "3w1", "3w1.5", "3w2", "4c3", "4n1", "4n2", "4w1", "4w2", "5c1", "5n1", "5n2", "5w1", "5w1.5", "5w2", "6c1", "6c2", "6n1", "6n2", "6w1", "6w2", "7c1", "7n1", "7w1", "8n1"], 
#             "2018.7": ["0n1", "1c0", "1c1", "1n0", "1n1", "1n2", "1w0", "1w1", "1w2", "2c0", "2c1", "2c3", "2c4", "2n1", "2n2", "2w0", "2w1", "2w2", "3c1", "3c2", "3c3", "3n1", "3n2", "3w1", "3w1.5", "3w2", "4c1", "4c2", "4c3", "4n1", "4n2", "4n3", "4w1", "4w2", "4w3", "4w4", "5c1", "5c2", "5n1", "5n1.5", "5n2", "5w1", "5w1.5", "5w2", "6c1", "6c2", "6n1", "6n2", "6w1", "6w2", "7c1", "7c2", "7n1", "7w1", "8c1", "8n1"], 
#         },
#         "url": "https://www.esteelauder.com/product/643/22830/product-catalog/makeup/face/foundations/double-wear/stay-in-place-makeup"}
# }


# define the foundation instance
# it is useful when I have more than one product to analyze
class Foundations():
    def __init__(self, foundation_name, url, years_diction):
        self.foundation_name = foundation_name
        self.url = url
        self.years_diction = years_diction

    def __str__(self):
        return '''The data is for {}.'''.format(self.foundation_name)


foundation_name = "esteelauder_doublewear"
esteelauder_doublewear_data = Foundations(foundation_name, data_pool[foundation_name]["url"], data_pool[foundation_name]["years"])

# print(list(esteelauder_doublewear_data.years_diction.keys()))
# print(esteelauder_doublewear_data.__str__())

# define the color instance
class Color():
    def __init__(self, color_name, hsl, lightness, color_code):
        self.color_name = color_name  #1c1
        self.hsl = hsl  #
        self.lightness = lightness  #68 
        self.color_code = color_code  ##e6bb98

    def __str__(self):
        return '''{} is {}, is {}'''.format(self.color_name, self.color_code, self.hsl)



## Return the lightness of the input color-code
## param: a color code
## returns: the lightness of the color
def get_hsl_for_color(color_code):
    cache_file = "color_hsl.json"
    cache = Cache(cache_file)

    base = "http://thecolorapi.com/id?"
    params_diction = {}
    params_diction["hex"] = color_code
    params_diction["format"] = json

    identifier = base + params_diction["hex"]

    response = cache.get(identifier)
    while response is None:
        response = json.loads(requests.get(base, params_diction).text)
        cache.set(identifier, response, 30)

    hsl = response["hsl"]['value']
    return hsl
    
# print(get_hsl_for_color("#e6bb98")) # hsl(27, 61%, 75%)



## Return the list of scraped color instances
## param: product name
## returns: all of the scraped color instances that are listed on the website
def get_color_instance_list(product):
    cache_file = "page_scraped.json"
    url_to_scrape = esteelauder_doublewear_data.url
    cache = Cache(cache_file)

    while cache.get(url_to_scrape) is None:
        html_text = requests.get(url_to_scrape).text
        cache.set(url_to_scrape, html_text, 30)

    soup = BeautifulSoup(cache.get(url_to_scrape), features='html.parser')

    colors = soup.find(class_="js-shade-picker shade-list").find_all(class_='swatches--single')

    color_instance_list = []
    for color in colors:
        color_name = color.a["name"].split(" ")[0]

        color_code = color.find(class_='swatch--1')["style"].split(":")[1].replace(";", "")
        hsl = get_hsl_for_color(color_code)
        lightness = hsl.split(",")[2].replace(" ","").replace(")","")

        color_instance_list.append(Color(color_name, hsl, lightness, color_code))
    return color_instance_list


color_instance_list = get_color_instance_list("esteelauder_doublewear")
# for color in color_instance_list:
#   print(color.__str__())


## Return the list of color instances for a typical year
## param: year in string type
## returns: all of the color instances of that typical year
def colors_in_year(year_in_string):
    colors_in_year_list = []
    for color in esteelauder_doublewear_data.years_diction[year_in_string]:
        for color_instance in color_instance_list:
            if color == color_instance.color_name.lower():
                colors_in_year_list.append(color_instance)

    return colors_in_year_list

# colors_in_2013 = colors_in_year("2013")
# colors_in_2015 = colors_in_year("2015")
# colors_in_2016 = colors_in_year("2016")
# colors_in_2018_3 = colors_in_year("2018.3")
# colors_in_2018_7 = colors_in_year("2018.7")

