# Demographic Data Analyzer

This is the boilerplate for the Demographic Data Analyzer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer

###########################################################################

Demographic Data Analyzer
You will be working on this project with our Replit starter code.

We are still developing the interactive instructional part of the Python curriculum. For now, here are some videos on the freeCodeCamp.org YouTube channel that will teach you everything you need to know to complete this project:

Python for Everybody Video Course (14 hours)
How to Analyze Data with Python Pandas (10 hours)

###########################################################################


In this challenge you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

_________________________________________________________________________________________________

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

___________________________________________________________________________________________________

################################################################################################

You must use Pandas to answer the following questions:

How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
- Done

What is the average age of men?
- Done

What is the percentage of people who have a Bachelor's degree?
- Done

What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
- Done

What percentage of people without advanced education make more than 50K?
- Done

What is the minimum number of hours a person works per week?
- Done

What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?


What country has the highest percentage of people that earn >50K and what is that percentage?
Identify the most popular occupation for those who earn >50K in India.
Use the starter code in the file demographic_data_analyzer. Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.

################################################################################################

Unit tests are written for you under test_module.py.

Development
For development, you can use main.py to test your functions. Click the "run" button and main.py will run.

################################################################################################

Testing
We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.

################################################################################################

Submitting
Copy your project's URL and submit it to freeCodeCamp.

################################################################################################

Dataset Source
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.