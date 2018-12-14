# Jiahui Zhou
# SI508-Final project

#### Please install the following libraries:
###### bs4
###### alternate_advanced_caching
###### requests
###### datetime
###### json
###### plotly
###### plotly.plotly
###### plotly.graph_objs

#### Project Overview
It is a program to use data to validate an opinion "The Makeup Industry Is Now More Skin Shade–Inclusive Than Ever." I chose 
the data of historical shades set evolution of Estee Lauder Double Wear Foundation, for both its largest color variations in current mainstream foundations and its constant name convention (otherwise, I am not able to scrape its previous color set on the webpage). I manually got the 5 sets of shade codes for year 2013, 2015, 2016, March 2018, and July 2018, scaped individual color hex code from its website, and use a color API to transfer the code into HSL(hue, saturation, lightness) color mode. Then I used plot.ly to visually present them. 

#### Sample Output
###### Image 'Shades_Distribution_of_esteelauder_doublewear_all' is the sample output of the command 'plot all'
###### Image 'Shades_Distribution_of_esteelauder_doublewear_2018_7' is the sample output of the command 'plot 2018.7'

#### Run Process
###### 1. Make sure you have installed all the libraries I listed above. No need to register anything including to use the color API I used in this project.
###### No database-related things in this project.
###### Run file 'main.py'
###### Try command 'plot all' to see the shades of each publish in the last five years
###### Try command 'plot <Year>'(e.g. plot 2018.7) to see the shades of publish in the specific year
###### Quit input by `exit`
###### Term explanation on input of `help`
###### Final project requirements meet: 
###### Three data sources used in total: color API, hex codes scraped from website, manually pullup shades changes in years
###### Caching in final_proj.py, with the code of alternative_advanced_caching.py
###### Process API data into a color class, saved hex codes into color class, shade changes data into a nested dictionary
###### import modules bs4, datetime, plotly
###### test file 'final_proj_test.py' with 3 unittest.TestSuite subclasses and 13 test methods
###### Produce a product as result of a visualization
###### Define 2 classes: Foundation, Color
###### Sample outputs included

#### File overview:
###### main.py: program the interactive command lines
###### final_proj.py: define Foundation class and Color class, include codes that scrapes the color hex codes, and API to change them to hsl color mode
###### final_plot.py: define two functions to plot the shades set either in a single year, or plot all years in one figure
###### final_proj_test.py: test file
###### esteelauder_doublewear_data.py: manually pullup data for shades changes, in dictionary type
###### advanced_expiry_caching.py: copy from code provided on the class. Define a chache class to store the respond to a cache file.
###### page_scraped.json: cache file
###### color_hsl.json: cache file
###### Shades_Distribution_of_esteelauder_doublewear_all': sample output of the command 'plot all'
###### Shades_Distribution_of_esteelauder_doublewear_2018_7': sample output of the command 'plot 2018.7'
###### README.md






