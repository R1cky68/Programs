# Couple of modules here, pandas for data manipulation, re (regular expressions), standard scaler for feature scaling, matplotlib.pyplot for data visualisation, numpy for numerical operations, scikitlearn for machine learning tasks
import pandas as pd
import re
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import warnings
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

warnings.simplefilter('ignore')

# Population data contains letters and numbers (zip codes at end), we'll extract just the zip codes at the end
df=pd.read_excel('/Users/hargundadyala/Documents/Programs/Predict/Coffee_shop_data.xlsx')
population=pd.read_csv('/Users/hargundadyala/Documents/Programs/Predict/population.csv', skiprows=[0])

population.head()

# Info method provides information about each of the data types of each column and the presence of any missing values in the df dataframe 
df.info()

# Checks rows and columns in data frame
df.shape
population.shape

# Get basic facts about the data 
df.describe()

# Counts occurrences of each unique value in city column and selects the top 5 cities based on the occurrences, then creates a bar plot for the selected cities
ax=df['City'].value_counts().head(5).plot(kind="bar")
ax.set_title("Cities with most shops")
plt.show()

ax=df['Business Name'].value_counts().head(10).plot(kind="bar")
ax.set_title("Top 10 Businesses")
plt.show()

# print("Current working directory:", os.getcwd())

# Checks number of null values in each column of the dataframe
df.isna().sum()

# Converts zip code column in dataframe to object data type string (str), to help join data and perform operations
df['Zip Code']=df['Zip Code'].astype(str)

# Extract zip code from population, so it gets the last 5 digits and returns an extracted zip code if a match is found 
def find_zip_code(geocode):
    pattern = r'\d{5}$'

    match = re.search(pattern, geocode)

    if match:
        zip_code = match.group(0)
    return zip_code

# Applying function to extract zip code, the result is stored in a new Zip Code column in the population dataframe
population['Zip Code']=population['Geography'].apply(find_zip_code)

# Copying df dataframe (cafe_data) and merging both dataframes, based on the zip code column, result stored in df dataframe
cafe_data=df.copy()
df=pd.merge(cafe_data,population)

# Keeping only total from population (and other selected columns by user), whilst the total column is renamed to population
columns=cafe_data.columns.values.tolist()+['Total']
df=df[columns]
df=df.rename(columns={"Total":"Population"})
df

# Keeping only relevant features from dataset, as seen below
df=df[['Zip Code', 'Rating', 'Median Salary', 'Latte Price', 'Population']]
df.shape
df.columns

# Calculate the total number of coffee shops for each zip code and stored in coffee_shop_counts dataframe
coffee_shop_counts = df['Zip Code'].value_counts().reset_index()
coffee_shop_counts.columns = ['Zip Code', 'CoffeeShopCount']

# Ensuring zip code is a string type in both dataframes
df['Zip Code'] = df['Zip Code'].astype(str)
coffee_shop_counts['Zip Code'] = coffee_shop_counts['Zip Code'].astype(str)

# Merge the counts back into the original Dataframe
df = df.merge(coffee_shop_counts, on='Zip Code', how='left')

print(df)

# Identifying and sorting dataframe into Top 5 zip codes (criteria: high population, low total number of coffee shops, low ratings, high median salary), high-low (true) and vice versa
sorted_df = df.sort_values(by=['Population', 'CoffeeShopCount', 'Rating', 'Median Salary'],
                           ascending=[False, True, True, False]).reset_index(drop=True)

# Create a list and deduping zip code column and displaying all of records for the top 5, if conditions are met the zip code is added to the list
lst=[]
for i in range (len(sorted_df)):
    if len(lst)!=5:
        if (sorted_df['Zip Code'][i]) not in lst:
           lst.append(sorted_df['Zip Code'][i])

    top_5_zip_codes_df = sorted_df[sorted_df['Zip Code'].isin(lst)]
    top_5_zip_codes_df

# Features excluding latte price and zip (X) and creating a target variable (y)
X = df.drop(['Latte Price', 'Zip Code'], axis=1)
y = df['Latte Price']

# The train_test_split function from Sci-kit learn splits the feature matrix (X) and target variable into training and testing (y) sets, 20% data for testing, 80% for training, makes it reproduceable by fixing the random seed
X_train, X_test, y_train, y_test, = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling, which normalises the range of independent variables or features of a dataset (keeps features on same scale, important for algorithms), fit gets mean+SD whilst transform method scales the data based on the parameters (learned from training data)
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Model selection - using regression models to predict continuous outcome variables (can take infinite values within range, eg coffee price), linear regression, random forest and gradient boosting, categorical variables are binary
models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(),
    'Gradient Boosting': GradientBoostingRegressor()
}

# So that was a dictionary above that contains the models

# Hyperparameter training, hyperparameters are settings that need to be adjusted for optimal performance, systemtically trying different combinations of settings to maximise the model's accuracy and generalisation (so it adapts)
param_grid = {
    'Random Forest': {'n_estimators' : [50, 100, 200], 'max_depth' : [None, 10, 20]},
    'Gradient Boosting': {'n_estimators' : [50, 100, 200], 'learning_rate' : [0.01, 0.1, 0.2], 'max_depth' : [3, 5, 10]},
}

# The n_estimators mean th grid will search for models with 50/100/200 trees, of its max_depth (none = unlimited)

# Using GridSearchCV to perform hyperparameter training
for model_name, model in models.items():
    
    # Hyperparameter search tuning, the loop iterates through each model in the dictionary (as above), for each model it does a GridSearchCV and checking the cross validation parameter
    if model_name in param_grid:
        grid_search = GridSearchCV(model, param_grid[model_name], cv=5, scoring='neg_mean_squared_error')
        grid_search.fit(X, y)
    
        # Setting the best hyperparameters for the model, which is re-assigned to the dictionary under the same model name
        models[model_name] = grid_search.best_estimator_

# Model training - teaching model from training dataset so it can predict values
for model_name, model in models.items():
    model.fit(X_train, y_train)

# Model evaluation - results show linear regression is generally the best based on those metrics
for model_name, model in models.items():
    y_pred = model.predict(X_test)
    print(f"{model_name} Metrics:")
    print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R-squared:", r2_score(y_test, y_pred))
    print()

# Remove zip_code and latte_price columns from top 5 predictions
zip_codes_df = top_5_zip_codes_df.drop(['Zip Code', 'Latte Price'], axis=1)
zip_codes_df = sc.transform(zip_codes_df)

for model_name, model in models.items():
    predicted_prices = model.predict(zip_codes_df)

# Initialising empty dictionary to store predicted prices of each model (then iterate over each)
predictions = {}

for model_name, model in models.items():
    # Predicting prices of lattes in top 5 zip codes and storing them in dictionary here
    predicted_prices = model.predict(zip_codes_df)
    predictions[model_name] = predicted_prices

# Convert predictions dictionary to dataframe
predictions_df = pd.DataFrame(predictions)

# Adding zip codes to the predictions dataframe
predictions_df['Zip Code'] = top_5_zip_codes_df['Zip Code'].values

# Rearranging to have zip codes column first
cols = ['Zip Code'] + [col for col in predictions_df.columns if col !='Zip Code']
predictions_df = predictions_df[cols]
predictions_df

# Grouping dataframe by zip code and selecting columns containing predictions from gradient boosting model, then aggragation functions calculate max high and vice versa for each group, columns are renamed then printed (from linear regression model for each zip code)
agg_df = predictions_df.groupby('Zip Code')['Linear Regression'].agg([["Highest", "max"], ("Lowest", "min")]).reset_index()
agg_df.columns = ['Zip Code', 'Highest', 'Lowest']
print(agg_df)

# So it'll show the zip code with highest and lowest predicted values for coffee prices, hence set your price somewhere between these values for each location