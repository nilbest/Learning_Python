import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('.\\Final Test Programms\\Demographic-Data-Analyzer\\adult.data.csv',header=0)
    
    #df = df.replace({'?': None})
    #print(df.to_string())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    #print(race_count)
    
    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male',['age']].mean()[0]
    #print(f'Durchschnitt mann: {average_age_men}')

    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df.education.value_counts().Bachelors / df.education.count())*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~(df['education'].isin(['Bachelors','Masters','Doctorate']))]
    

  
    
    # percentage with salary >50K
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].count().salary / higher_education.education.count())*100
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].count().salary / lower_education.education.count())*100

    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #d[(d['x']>2) & (d['y']>7)]    
    num_min_workers = df[(df['hours-per-week'] == min_work_hours)&(df['salary'] == '>50K')].count().salary 

    rich_percentage = (num_min_workers / df[df['hours-per-week'] == min_work_hours].count().salary)*100
    #print(rich_percentage)
    
    # What country has the highest percentage of people that earn >50K?
    
    only_rich = df[df['salary'] == '>50K']
    rich_countrys = only_rich['native-country'].unique().tolist()
    
    #all_countrys = df['native-country'].unique().tolist()
    #print(df[(df['native-country'] == all_countrys[0]) & (df['salary']=='>50K')].count().salary)
    
    highest_earning_country_percentage = 0
    
    for country in rich_countrys:
        num_rich = df[(df['native-country'] == country) & (df['salary']=='>50K')].count().salary
        num_all = df[(df['native-country'] == country)].count().salary
        per_rich = (num_rich/num_all)*100
        if highest_earning_country_percentage < per_rich:
            highest_earning_country = country
            highest_earning_country_percentage = per_rich
         
    #print(highest_earning_country)
    #print(highest_earning_country_percentage)

    
    

    # Identify the most popular occupation for those who earn >50K in India.
    occupation = pd.DataFrame({'Occupation':df[(df['native-country'] == 'India') & (df['salary']=='>50K')]['occupation'].value_counts().index.tolist(),
                                'Count':df[(df['native-country'] == 'India') & (df['salary']=='>50K')]['occupation'].value_counts().values.tolist()
                                })
    
    top_IN_occupation = occupation[occupation['Count'] == (occupation['Count'].max())]['Occupation'].values[0]
    #print(top_IN_occupation)
    
    
    # Round all Percentages
    average_age_men = round(average_age_men, 1)
    percentage_bachelors = round(percentage_bachelors, 1)
    higher_education_rich = round(higher_education_rich, 1)
    lower_education_rich = round(lower_education_rich, 1)
    rich_percentage = round(rich_percentage, 1)
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)
    


    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

#calculate_demographic_data()