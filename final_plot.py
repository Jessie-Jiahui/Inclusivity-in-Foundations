import plotly.plotly as py
import plotly.graph_objs as go

from final_proj import *


def plot_shades_year(product_name, year_in_string):
    data = colors_in_year(year_in_string)

    # trace list
    l = []
    # number of dot in list
    y = []

    for shade in data:
        # hover.append(shade.color_name)
        # lightness_list.append(shade.lightness)

        trace = go.Scatter(
            x= [year_in_string],
            y= [shade.lightness],
            mode= 'markers',
            marker= dict(size= 10,
                        # line= dict(width=1),
                        color= shade.hsl,
                        # opacity= 0.3
                       ),
            name= shade.color_name)
            # text= [shade.color_name]) # The hover text goes here... 
        l.append(trace);

    layout= go.Layout(
        title= 'Shades Distribution of {} in {}'.format(product_name, year_in_string),
        hovermode= 'closest',
        autosize=False,
        width=800,
        height=800,
        xaxis=go.layout.XAxis(
            title='Year',
            ticktext=['2013','2015','2016','March 2018', 'July 2018'],
            tickvals=[1, 2, 3, 4],
            tickmode='array',
            automargin=True,
            titlefont=dict(size=30),
        ),
        yaxis=go.layout.YAxis(
            title='Lightness',
            ticktext=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100'],
            tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            tickmode='array',
            automargin=True,
            titlefont=dict(size=30),
        ),
        showlegend= False
    )
    fig= go.Figure(data=l, layout=layout)
    py.plot(fig, filename='color-foundation-in-{}').format(year_in_string)


# plot_shades_year('esteelauder_doublewear', '2016')


def plot_shades(product_name):
    # trace list
    l = []
    # number of dot in list
    y = []

    # for year_in_string in data_pool["esteelauder_doublewear"]["years"].keys():
    for year_in_string in list(esteelauder_doublewear_data.years_diction.keys()):
        data = colors_in_year(year_in_string)
        for shade in data:
            # hover.append(shade.color_name)
            # lightness_list.append(shade.lightness)

            trace = go.Scatter(
                x= [year_in_string],
                y= [shade.lightness],
                mode= 'markers',
                marker= dict(size= 10,
                            # line= dict(width=1),
                            color= shade.hsl,
                            # opacity= 0.3
                           ),
                name= shade.color_name)
                # text= [shade.color_name]) # The hover text goes here... 
            l.append(trace);

    layout= go.Layout(
        title= 'Shades Distribution of {}'.format(product_name),
        hovermode= 'closest',
        autosize=False,
        width=800,
        height=800,
        # xaxis= dict(
        #     title= 'Year',
        #     ticklen= 5,
        #     zeroline= False,
        #     gridwidth= 2,
        # ),
        # yaxis=dict(
        #     title= 'Lightness',
        #     ticklen= 5,
        #     gridwidth= 2,
        # ),
        xaxis=go.layout.XAxis(
            title='Year',
            ticktext=['2013','2015','2016','March 2018', 'July 2018'],
            tickvals=[2013, 2015, 2016, 2018.3, 2018.7],
            tickmode='array',
            automargin=True,
            titlefont=dict(size=20),
        ),
        yaxis=go.layout.YAxis(
            title='Lightness',
            ticktext=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100'],
            tickvals=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            tickmode='array',
            automargin=True,
            titlefont=dict(size=20),
        ),
        showlegend= False
    )
    fig= go.Figure(data=l, layout=layout)
    py.plot(fig, filename='color-foundation')

# plot_shades('esteelauder_doublewear')