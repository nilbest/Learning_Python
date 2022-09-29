import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('.\\Final Test Programms\\Medical-Data-Visualizer\\medical_examination.csv')
#print(df)


# Add 'overweight' column
# To determine if a person is overweight, first calculate their BMI by 
# dividing their weight in kilograms by the square of their height in meters. 
# If that value is > 25 then the person is overweight. 
# Use the value 0 for NOT overweight and the value 1 for overweight.
bmi = (df['weight'])/((df['height']/100)**2)
df['overweight'] = np.where(bmi >25, 1,0)


# Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
    #global df
    # Create DataFrame for cat plot using `pd.melt` using just the values 
    # from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio' ,value_vars=['active','alco','cholesterol', 'gluc','overweight','smoke'])

    # Group and reformat the data to split it by 'cardio'. 
    # Show the counts of each feature. 
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio","variable","value"]).size().reset_index(name="total")
    

    # Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x= 'variable', y='total', col='cardio', hue='value', kind="bar").fig
    
    # Do not modify the next two lines
    fig.savefig('.\\Final Test Programms\\Medical-Data-Visualizer\\catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    #global df
    
    #Erstellung einer Kopie
    #df_heat = df
    
    #Data cleaning
    #diastolic pressure is higher than systolic 
    #(Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    #con_1 = df['ap_lo'] <= df['ap_hi']

    #height is less than the 2.5th percentile 
    # (Keep the correct data with (df_heat['height'] >= df_heat['height'].quantile(0.025)))
    #con_2 = ((df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)))
    #height is more than the 97.5th percentile
    

    #weight is less than the 2.5th percentile
    #weight is more than the 97.5th percentile
    #con_3 = ((df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975)))
    
    #df_heat = df[con_1 & con_2 & con_3]
    
    #Better looking way
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
                & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975)) 
                & (df['weight'] >= df['weight'].quantile(0.025)) 
                & (df['weight'] <= df['weight'].quantile(0.975))]
    
    #print(df_heat)
    

    # Calculate the correlation matrix
    #print(df_heat)
    corr = df_heat.corr()
    #print(corr)
    corr = corr.round(1)
    #print(corr)
    #print(corr)
    
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    #print(mask)


    # Set up the matplotlib figure
    #fig, ax = None
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, square=True, vmin=-0.16, vmax=0.32 , center=0, linewidths=2, annot=True, fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('.\\Final Test Programms\\Medical-Data-Visualizer\\heatmap.png')
    return fig
