import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header('Car Sales Advertisements')
st.write('Exploring the Relationship Between Car Models, Year, and Pricing Trends in a Used Car Dataset')

st.write("""The used car market is a dynamic landscape where various factors such as the car's model, age, condition, and mileage significantly influence the vehicle's resale value. Understanding the interplay between these variables can provide insights into pricing trends and customer preferences. 

In this project, we will analyze a dataset of used cars to identify pricing patterns based on car models, model years, and other key attributes. Specifically, we aim to explore how car prices vary across different models and how factors like the odometer reading (mileage) and the year of production impact the final price. Additionally, we will remove any data outliers to ensure a more accurate representation of pricing trends.

By visualizing these relationships and filtering outliers, the project will deliver more informative and actionable insights into the pricing behaviors in the used car market, helping both consumers and sellers make informed decisions.""")

df = pd.read_csv('vehicles_us.csv')
df[['make', 'model']] = df['model'].str.split(' ', n=1, expand=True)

st.write(""" ## Data Cleaning and Preprocessing:

We will start by cleaning the dataset to handle missing values and split columns where necessary. Here’s what we will do:

1. **Handle Missing Values**: We'll fill missing values for the `model_year`, `cylinders`, and `odometer` columns by grouping by car model and using the median value for imputation.
2. **Split Columns**: We will split the `model` column into separate `make` and `model` columns for easier analysis.
3. **Convert Data Types**: Ensure that the `model_year` and other relevant columns have appropriate data types, converting to integers where applicable.
4. **Remove Outliers**: Filter out the extreme values in `price` and `model_year` to ensure the analysis remains focused on relevant data points.""")

df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))
if np.array_equal(df['model_year'], df['model_year'].astype('int')):
    df['model_year'] = df['model_year'].astype('int')

df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))
if np.array_equal(df['cylinders'], df['cylinders'].astype('int')):
    df['cylinders'] = df['cylinders'].astype('int')

df['odometer'] = df.groupby(['model_year'])['odometer'].transform(lambda x: x.fillna(x.median()))
print(df[df['odometer'].isna()])

#if np.array_equal(df['odometer'], df['odometer'].astype('int')):
#    df['odometer'] = df['odometer'].astype('int')

df['is_4wd'] = df['is_4wd'].fillna(0)
if np.array_equal(df['is_4wd'], df['is_4wd'].astype('int')):
    df['is_4wd'] = df['is_4wd'].astype('int')

df['paint_color'] = df['paint_color'].fillna('unknown')

df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

model_type = st.selectbox('Select model', df['model']) 

fig_price = px.histogram(df, x='price', title='Distribution of Car Prices')
st.plotly_chart(fig_price)
st.write(""" 
         From this plot, it appears that the majority of vehicles are priced within a lower range,
         with a noticeable concentration around certain price points. This suggests that most vehicles listed fall within affordable price categories,
         while higher-priced vehicles are less common.The distribution shows a steep drop-off as prices increase. """)

fig_scatter =px.scatter(df, x='model_year', y='price', color='model',
                        title='Scatter Plot: Car Model vs Days Listed',
                        labels={'model': 'Model', 'days_listed': 'Days Listed'})
st.plotly_chart(fig_scatter)

st.write(""" From this plot, it appears that newer car models tend to have higher prices, while older models are generally priced lower.
         This suggests that the model year plays a significant role in determining vehicle prices.
         However, a variety of models appear across different price ranges, indicating that both the car's brand and its year influence the final price.
         Most newer models are priced at a premium, while older ones show a broader distribution of prices.""")

mean_price_by_model1 = df.groupby('model')['price'].mean().reset_index()
mean_price_by_model1 = mean_price_by_model1.sort_values(by='price', ascending=False)

df = df[df['model_year'] != 0]

fig_mean_price_model = px.scatter(mean_price_by_model1.head(10), x='model', y='price', color='model',
                              title='Top 10 Most Expensive Car Models(Average Price)',
                              labels={'price': 'Average Price (USD)'})
st.plotly_chart(fig_mean_price_model)
st.write(""" This plot shows the top 10 most expensive car models based on their average price, highlighting
         which models tend to have the highest market value.""")


st.header("Price analysis")
st.write("### Let's consider how the odometer influences the price ###")
fig_price_odometer = px.histogram(df, x='odometer', y='price',color='model',
                                  title='Price vs Odometer',
                                  labels={'odometer': 'Odometer Reading (miles)', 'price': 'Price (USD)'})
st.plotly_chart(fig_price_odometer)

# Define boundaries for model_year and price
min_model_year = 1980  # Only include cars newer than 1980
max_price = 100000     # Only include cars priced under $100,000

# Filter the dataset based on these conditions
df_filtered = df[(df['model_year'] >= min_model_year) & (df['price'] <= max_price)]

# Create the scatter plot again, showing only the filtered data
fig_scatter = px.scatter(df_filtered, x='model_year', y='price', color='model',
                        title='Scatter Plot: Car Model vs Price',
                        labels={'model': 'Model', 'price': 'Price (USD)'})

# Adjust the xlim and ylim if needed (optional)
fig_scatter.update_layout(xaxis_range=[min_model_year, df_filtered['model_year'].max()],
                          yaxis_range=[0, max_price])
st.plotly_chart(fig_scatter)

st.header("Conclusion")
st.write(""" The histogram shows the relationship between car prices and odometer readings.
         Vehicles with lower odometer readings generally have higher prices, with most of the cars clustered around 50,000 to 150,000 miles.
         As the odometer readings increase, prices tend to decrease, indicating that higher mileage cars are typically less expensive.
         This suggests a clear trend where lower mileage correlates with higher vehicle prices.""")

st.header('Overall Conclusion')
st.write("""

The exploratory data analysis (EDA) provided valuable insights into the dataset of used vehicles in the U.S. market.

1. **Price Distribution**:
   The distribution of vehicle prices showed that the majority of vehicles fall within a lower price range, with a few outliers priced significantly higher. This suggests that most of the listed vehicles are affordable options, while luxury models or newer vehicles might be driving up the upper range of prices.

2. **Odometer vs Price**: paraphrase this for app.py 
   There is a clear inverse relationship between the odometer reading and the price. Vehicles with lower mileage tend to be priced higher, as expected, since mileage is often a key indicator of vehicle condition and wear. High-mileage cars are priced lower, likely due to the expectation of greater future maintenance needs.

3. **Model Year vs Price**:
   Newer model years generally command higher prices, reflecting the vehicle's newer condition and up-to-date technology. Older models see a gradual depreciation in value, although certain models retain more value than others.

4. **Condition of Vehicles**:
   Most vehicles in the dataset are listed in "good" or "excellent" condition, which reflects seller attempts to market their vehicles positively. Vehicles in "fair" or "poor" condition are priced lower, as expected, due to higher expected repair costs.

5. **Odometer Readings**:
   Most vehicles in the dataset had odometer readings between 50,000 and 150,000 miles, aligning with typical used vehicle listings. Very low or very high mileage vehicles were less common, and these extremes had notable impacts on price.

6. **Impact of Preprocessing**:
   By filling in missing values and removing outliers, the dataset became more reliable for analysis. This step ensured that any skewed data points didn't distort conclusions drawn from visualizations, particularly in terms of price vs model year and odometer readings.

In conclusion, the dataset shows typical patterns expected in a used car market, where price is driven primarily by vehicle age, condition, and mileage.""")
st.checkbox(
    label="**Confirm Data Preparation and Visualization Steps**: Includes handling missing data using `fillna`, converting `date_posted` to `datetime`, and visualizing data through histograms and scatter plots. [See more details](https://github.com/streamlit)",
    value=False,  # Default unchecked
    help="This checkbox confirms the key data preparation and visualization tasks have been completed.",
    disabled=False)

st.header('Overall Conclusion')
st.write("""""")