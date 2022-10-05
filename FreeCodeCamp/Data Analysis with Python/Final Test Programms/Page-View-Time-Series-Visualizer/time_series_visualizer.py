import matplotlib.pyplot as plt
#from matplotlib.ticker import ScalarFormatter
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import datetime
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
    
    
    
    
    #set width of bar
    barWidth = 0.25

    



    df_bar=pd.pivot_table(data=df_bar, index='Year', columns='Month', values='value')
    #print(df_bar)   
        
        
        
    fig, ax = plt.subplots(figsize=(16,9))
    plt.rcParams['axes.formatter.useoffset'] = False
    #y_formatter = ScalarFormatter(useOffset=False)
    #ax.yaxis.set_major_formatter(y_formatter)
    
    #plt.yticks(np.arange(0, df_bar.all().max(), 20000))
    df_bar.plot(ax = ax, kind='bar')
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    handles, labels = ax.get_legend_handles_labels()
    new_labels = ['January','February','March','April','May','June',
                  'July','August','September','October','November','December']
    
    # after plotting the data, format the labels
    #current_values = plt.gca().get_yticks()
    # using format string '{:.0f}' here but you can choose others
    #plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
    
    ax.legend(handles = handles, labels = new_labels, loc = 'upper left', bbox_to_anchor = (1, 1.02))

    # Save image and return fig (don't change this part)
    fig.savefig('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box.sort_values(by=['year','date'],ascending=[False,True],inplace=True)
    
    # Draw box plots (using Seaborn)   
    fig,ax = plt.subplots(1,2, figsize=(16, 9))
    sns.boxplot(x='year',y='value', data=df_box,ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
     
    sns.boxplot(x='month',y='value',data=df_box,ax=ax[1]) 
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('.\\Final Test Programms\\Page-View-Time-Series-Visualizer\\box_plot.png')
    return fig
