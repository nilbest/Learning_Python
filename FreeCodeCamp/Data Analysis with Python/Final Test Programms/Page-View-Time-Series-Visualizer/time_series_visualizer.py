import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\fcc-forum-pageviews.csv')
#df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
df['date'] = pd.to_datetime(df['date'], yearfirst=True)
df.set_index('date', inplace=True)
#print(df)

# Clean data
#without under 2.5% and above 97.5%
df = df[(df['value'] >= (df['value'].quantile(0.025)))
        &(df['value'] <= (df['value'].quantile(0.975)))
        ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(21, 9))
    plt.plot(df.index,df['value'], 'r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.groupby([pd.to_datetime(df.index).year,pd.to_datetime(df.index).month]).agg({'value': np.sum})
    df_bar.index = df_bar.index.rename(['Year','Month'])
    
    #First try's
    #df_bar = df
    #df_bar['year'] = pd.DatetimeIndex(df.index).year
    #df_bar['month'] = pd.DatetimeIndex(df.index).month
    #years = df_bar['year'].unique().tolist()
    #months = df_bar['month'].unique().tolist()
    
    #sum_list = []
    #for year in years:
    #    for month in months:
            #print(df[(df_bar['year']==year)&(df_bar['month']==month)]['value'])
            #print((df_bar['year'].isin([year])) & (df_bar['month'].isin([month])))
            #Problem not able to locate the right values to every year and month
    #print(sum_list)        
    #df_bar['m_value'] = sum_list
    
    # Draw bar plot
    #print(df_bar)
    #print(df_bar['value'].tolist())
    #print(df_bar.index)
    
    print(df_bar)
    #print(df_bar.index.Month)
    
    
    
    #set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
    
    # set height of bar
    #January = df_bar[df_bar['date']==1].tolist()
    #print(df_bar.iloc[df_bar.index.get_level_values('Month') == 1])
    print(df_bar.index.get_level_values('Month').unique().tolist())
    month_list = df_bar.index.get_level_values('Month').unique().tolist()
    month_list.sort()
    
    print(month_list)
    print(df_bar.iloc[df_bar.index.get_level_values('Month') == 1]['value'].tolist())
    #print(January)
    #February = 
    #ECE = [28, 6, 16, 5, 10]
    #CSE = [29, 3, 24, 25, 17]
    #
    # Set position of bar on X axis
    #br1 = np.arange(len(IT))
    #br2 = [x + barWidth for x in br1]
    #br3 = [x + barWidth for x in br2]
    #
    ## Make the plot
    #plt.bar(br1, IT, color ='r', width = barWidth,
    #        edgecolor ='grey', label ='IT')
    #plt.bar(br2, ECE, color ='g', width = barWidth,
    #        edgecolor ='grey', label ='ECE')
    #plt.bar(br3, CSE, color ='b', width = barWidth,
    #        edgecolor ='grey', label ='CSE')
    #
    ## Adding Xticks
    #plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
    #plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
    #plt.xticks([r + barWidth for r in range(len(IT))],
    #        ['2015', '2016', '2017', '2018', '2019'])
    #
    #plt.legend()




    # Save image and return fig (don't change this part)
    fig.savefig('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = None




    # Save image and return fig (don't change this part)
    fig.savefig('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\box_plot.png')
    return fig
