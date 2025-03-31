# Vehicles_project
https://vehicles-project-8raw.onrender.com

---

# Sprint 4 Project – Predicting Vehicle Prices from U.S. Used Car Listings

This project focused on analyzing historical data from U.S. used car listings to understand pricing trends and vehicle characteristics. The goal was to build a machine learning model that predicts a car’s market price based on its specifications and condition.

### Exploring Used Car Listings

The dataset included thousands of listings with details like vehicle condition, mileage, transmission type, paint color, and how long each car was listed. This project gave me hands-on experience with real-world preprocessing challenges like missing values and inconsistent data types.

#### The Data

The dataset included key features for each listing:

- **`price`**: Sale price of the vehicle
- **`model_year`**, **`condition`**, **`odometer`**, **`cylinders`**
- **`fuel`**, **`transmission`**, **`type`**, **`paint_color`**
- **`is_4wd`**, **`date_posted`**, **`days_listed`**

These features helped describe each vehicle’s condition, performance, and market exposure.

#### The Process

1. **Data Cleaning & Preprocessing**  
   - Imputed missing values in `model_year`, `cylinders`, and `odometer` using grouped medians.
   - Converted categorical variables and date formats for modeling.
   - Removed outliers to improve model quality and visualization clarity.

2. **Exploratory Data Analysis (EDA)**  
   - Analyzed price distributions by condition, vehicle type, and mileage.
   - Explored time-on-market trends using the `days_listed` column.
   - Visualized key relationships using scatterplots and boxplots.

3. **Modeling & Evaluation**  
   - Trained baseline Linear Regression to establish a performance benchmark.
   - Evaluated more complex models like Random Forest and Gradient Boosting.
   - Used **Root Mean Squared Error (RMSE)** to measure prediction quality.

### Results & Takeaways

I built a model that accurately predicts car prices using a mix of numeric and categorical features. Along the way, I learned how to handle real-world messiness in data — like missing records, type mismatches, and noisy values — and how to translate that into a working ML pipeline.
