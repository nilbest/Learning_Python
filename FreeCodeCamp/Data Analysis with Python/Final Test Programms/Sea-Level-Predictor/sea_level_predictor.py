import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('.\\Final Test Programms\\Sea-Level-Predictor\\epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    
    #Add The Year 2050
    
    # Create first line of best fit
    first_line = linregress(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])
    #print(first_line)
    #print(df['Year'].count())
    
    #Add The Year 2050
    #year_list=[]
    for year in range(df['Year'].max()+1,2051):
        #year_list.append(year)
        df = pd.concat([df,pd.Series({'Year': year}).to_frame().T], ignore_index=True)
    
    #print(year_list)
    #df = pd.concat([df,pd.Series({'Year': year}).to_frame().T], ignore_index=True)
    
    #print(df)
    #xA = np.arange(df['Year'].min(),2051,1)
    #yA = xA*first_line.slope + first_line.intercept
    
    plt.plot(df['Year'],first_line.intercept + first_line.slope*df['Year'], 'r',label='1. fitted line')
    #plt.plot(xA,yA, 'r',label='1. fitted line')

    #print(df['Year'].count())
    
    # Create second line of best fit
    conditions_1=(df['Year']>= 2000) & (df['Year']<= 2013)
    conditions_2=(df['Year']>= 2000) & (df['Year']<= 2050)
    x_line = df.loc[conditions_1,['Year']]
    y_line = df.loc[conditions_1,['CSIRO Adjusted Sea Level']]
    x= df.loc[conditions_2,['Year']]
    y= df.loc[conditions_2,['CSIRO Adjusted Sea Level']]

    second_line = linregress(x=x_line['Year'],y=y_line['CSIRO Adjusted Sea Level'])
    plt.plot(x['Year'], second_line.intercept + second_line.slope*x['Year'], 'g',label='2. fitted line')
    #print(x['Year'].count())
    
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('.\\Final Test Programms\\Sea-Level-Predictor\\sea_level_plot.png')
    return plt.gca()