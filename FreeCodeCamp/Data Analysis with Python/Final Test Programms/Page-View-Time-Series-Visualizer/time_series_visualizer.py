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
    df_bar = df
    df_bar['year'] = pd.DatetimeIndex(df.index).year
    df_bar['month'] = pd.DatetimeIndex(df.index).month
    #df_bar['monthly_value']=df_bar['year','month'].unique().sum()
    #df_bar['monthly_value']= df_bar.loc[pd.DatetimeIndex(df.index).month].sum()
    years = df_bar['year'].unique().tolist()
    months = df_bar['month'].unique().tolist()
    #print(df_bar['year'].unique())
    #print(years)
    #print(df_bar)
    #print(years)
    #print(months)
    df_bar['m_value'] = np.nan 
    
    #sum_list = []
    for year in years:
        for month in months:
            #df.loc[df['team'] == 'A', 'points'].sum()
            #print(df[(df_bar['year']==year)&(df_bar['month']==month)]['value'])
            #print((df_bar['year'].isin([year])) & (df_bar['month'].isin([month])))
            
            #print(df_bar[(df_bar['year'].isin([year])) & (df_bar['month'].isin([month]))]['value'].sum())
            sum = df_bar[(df_bar['year'].isin([year])) & (df_bar['month'].isin([month]))]['value'].sum()
            #sum_list.append(sum)
            #print(df_bar.groupby((df_bar['year'].isin([year])) & (df_bar['month'].isin([month]))).sum())
            #df_bar['m_value'] = df_bar.groupby((df_bar['year'].isin([year])) & (df_bar['month'].isin([month]))).sum()
            #df_bar['m_value'] = df_bar.loc[(df_bar['year']==year) & (df_bar['month']==month),'value'].sum()
            #pass
    #print(sum_list)        
    df_bar['m_value'] = sum_list
    print(df_bar)
    
    # Draw bar plot
    fig = None




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
