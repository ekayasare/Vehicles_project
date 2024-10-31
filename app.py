import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.header('Car Sales Advertisements')
st.write('Filter the data below to see the ads by price')

df = pd.read_csv('vehicles_us.csv')
df[['make', 'model']] = df['model'].str.split(' ', n=1, expand=True)

df['model_year'] = df['model_year'].fillna(0)
if np.array_equal(df['model_year'], df['model_year'].astype('int')):
    df['model_year'] = df['model_year'].astype('int')

df['cylinders'] = df['cylinders'].fillna(0)
if np.array_equal(df['cylinders'], df['cylinders'].astype('int')):
    df['cylinders'] = df['cylinders'].astype('int')

df['odometer'] = df['odometer'].fillna(0)
if np.array_equal(df['odometer'], df['odometer'].astype('int')):
    df['odometer'] = df['odometer'].astype('int')

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

fig_mean_price_model = px.scatter(mean_price_by_model1.head(10), x='model', y='price', color='model',
                              title='Top 10 Most Expensive Car Models(Average Price)',
                              labels={'price': 'Average Price (USD)'})
st.plotly_chart(fig_mean_price_model)
st.write(""" This plot shows the top 10 most expensive car models based on their average price, highlighting
         which models tend to have the highest market value.""")


st.header("Price analysis")
st.write("### Let's consider how the odometer influences the price ###")
fig_price_odometer = px.histogram(df, x='odometer', y='price', 
                                  title='Price vs Odometer',
                                  labels={'odometer': 'Odometer Reading (miles)', 'price': 'Price (USD)'})
st.plotly_chart(fig_price_odometer)

st.header("Conclusion")
st.write(""" The histogram shows the relationship between car prices and odometer readings.
         Vehicles with lower odometer readings generally have higher prices, with most of the cars clustered around 50,000 to 150,000 miles.
         As the odometer readings increase, prices tend to decrease, indicating that higher mileage cars are typically less expensive.
         This suggests a clear trend where lower mileage correlates with higher vehicle prices.""")
st.checkbox(
    label="**Confirm Data Preparation and Visualization Steps**: Includes handling missing data using `fillna`, converting `date_posted` to `datetime`, and visualizing data through histograms and scatter plots. [See more details](https://github.com/streamlit)",
    value=False,  # Default unchecked
    help="This checkbox confirms the key data preparation and visualization tasks have been completed.",
    disabled=False)