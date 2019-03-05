*Jiahui Zhou, University of Michigan, School of Information, UX Design & Research*

# Project Overview
It is a program to use data to validate an opinion "The Makeup Industry Is Now More Skin Shade–Inclusive Than Ever." I chose 
the data of historical shades set evolution of Estee Lauder Double Wear Foundation, for both its largest color variations in current mainstream foundations and its constant name convention (otherwise, I am not able to scrape its previous color set on the webpage). 

In this project, I:
* Researched and gathered information about a foundation which is able to has constant name convention and release information
* Scrape data from Estee Lauder Double Wear Foundation's website for information about the shades such as its name, hex-code etc.
* Used an open-source color API to transfer each of the hex-code into its HSL(hue, saturation, lightness) color mode.
* Used Plot.ly to visualize the shades information in years on the canvas according to users' requirements.

Here you can:
*  get a list of all the national parks in a state by providing the state's abbreviation.
*  plot all the national parks in the state you just indicate on a map.
*  get a list of 20 nearby places around a certain national park by providing the sequence number of that site in the previous national parks list.
*  plot those nearby places on a map.

Below are some sample visualizations you will get:
#### Shades Distribution of Estee Lauder Doublewear for All Years
![Shades_Distribution_of_esteelauder_doublewear_all](Shades_Distribution_of_esteelauder_doublewear_all.png?raw=true "Shades Distribution of Estee Lauder Doublewear for All Years")
#### Shades Distribution of Estee Lauder Doublewear for Year 2018.7
![Shades_Distribution_of_esteelauder_doublewear_2018_7](Shades_Distribution_of_esteelauder_doublewear_2018_7.png?raw=true "hades Distribution of Estee Lauder Doublewear for Year 2018.7")

# Introduction to the Files
There are a total of 5 python files you need to run this program and do the things mentioned above. These files are:
*  `alternate_advanced_caching.py`
*  `main.py`
*  `final_proj.py.py`
*  `final_plot.py`
*  `esteelauder_doublewear_data.py`

Of those 5 files, `main.py` is the main file you should run to perform all the functions. All the other four files are all supporting files. The detail about how to interact with the program will be talked in the *Instructions* section.

There are also 2 JSON files that will be generated during you run the main file. These files are just used for caching purpose and will not affect running the main file in any way.

# Dependencies to Install Before You Run the Code
## 1. Plot.ly

Plotly is a graphing service that you can work with from Python. It allows you to create many different kinds of graphs, including the ones we will see in this program.

First, you need to go to the official site of Plot.ly: https://plot.ly/ and create an account. You also need to make sure to click on the confirmation email that Plot.ly sends after you create an account, since without this you won’t be able to get an API key that will be needed in this program.

To be able to use Plot.ly from your python programs, you will need to install the Plot.ly module and set up your installation with your private API key. Here are the instructions:

### 1) Installation
To install Plotly's python package, use the package manager pip inside your terminal.
If you don't have pip installed on your machine, click https://pip.pypa.io/en/latest/installing/ for pip's installation instructions.

`$ pip install plotly`

or

`$ sudo pip install plotly`

### 2) Set Credentials
After installing the Plot.ly package, you're ready to fire up python:

`$ python`

and set your credentials:

```python
import plotly
plotly.tools.set_credentials_file(username='DemoAccount', api_key='DemoKey')
```

You'll need to replace 'DemoAccount' and 'DemoKey' with your Plotly username and API key.
Find your API key here https://plot.ly/Auth/login/?next=%2Fsettings%2Fapi.

The initialization step places a special .plotly/.credentials file in your home directory. Your ~/.plotly/.credentials file should look something like this:

```JSON
{
    "username": "DemoAccount",
    "stream_ids": ["ylosqsyet5", "h2ct8btk1s", "oxz4fm883b"],
    "api_key": "DemoKey"
}
```

## 2. BeautifulSoup:

Since you should already set up `pip` when you finish setting up the Plot.ly. You can also use `pip` to install BeautifulSoup if you don't have it on your computer.

Open your terminal window and type in:

`pip install beautifulsoup4`

and you are all set!

# Instructions
Great! Now you are ready to explore and use the program.

This program is interactive. When you run it in the terminal, you can type in different commands to instruct the program to do things you want it to do. Here's a list of commands that you can enter and their corresponding results:

* plot all - e.g. plot all

This command plots all shades of each publish in the last five years, with year labeled.

* plot <Year> - e.g. plot 2018.7

This command plots the shades of the foundation released in that specified year.

* exit - e.g. exit

This command exits the program.

* help - e.g. help

This command lists all available commands you can input right now.

The introduction of the program and all instructions will appear again when you run the program so that you don't have to refer back and forth.


### Now you have grasped all the things you need to run this program! Feel free to explore it and see how makeup industry making more inclusive by adding more shades for yellow and black people!
