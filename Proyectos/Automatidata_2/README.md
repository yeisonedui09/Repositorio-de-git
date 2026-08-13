# NYC TLC Taxi Data Analysis & Dashboard

## Project Overview

This project analyzes data from the New York City Taxi and Limousine Commission (TLC) to explore taxi trip patterns, fares, tips, distances, and revenue.

The project combines **Exploratory Data Analysis (EDA) in Python** with an interactive **Tableau dashboard** to identify relevant patterns and provide insights that could support business decisions.

## Objectives

The main objectives of this project are to:

- Explore the structure and quality of the TLC dataset.
- Identify missing values, inconsistencies, and potential outliers.
- Analyze trip distance, duration, fares, tips, and total revenue.
- Identify trends by month and day of the week.
- Explore differences between taxi vendors.
- Examine relationships between trip characteristics and revenue.
- Present key findings through an interactive Tableau dashboard.

## Dataset

The dataset contains NYC taxi trip records with information including:

- Pickup and drop-off dates and times
- Passenger count
- Trip distance
- Rate code
- Pickup and drop-off locations
- Payment type
- Fare amount
- Tips
- Tolls
- Additional charges
- Total trip amount
- Taxi vendor

The dataset contains **22,699 observations and 18 columns**.

## Tools & Technologies

- **Python**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
- **Jupyter Notebook**
- **Tableau**
- **Git & GitHub**

## Exploratory Data Analysis

The EDA includes:

- Data structure and data type assessment
- Missing value checks
- Descriptive statistics
- Outlier identification
- Distribution analysis
- Trip distance analysis
- Trip duration analysis
- Tip analysis
- Revenue analysis
- Monthly and weekly trends
- Drop-off location analysis
- Vendor comparisons

Visualizations used during the analysis include:

- Scatter plots
- Histograms
- Bar charts
- Box plots

## Data Quality

During the analysis, several potential data quality issues were identified, including negative values in some monetary fields and unusually large values in variables such as fare amount, tip amount, and total amount.

These observations were investigated as potential outliers or data inconsistencies before being considered in the analysis.

Date columns were also converted to datetime format to allow trip duration and time-based variables to be derived correctly.

## Key Questions

The analysis focuses on questions such as:

- What are the typical characteristics of NYC taxi trips?
- How does trip distance relate to fare and revenue?
- How does revenue vary by month and day of the week?
- How do tips vary by passenger count and vendor?
- Are there unusual or extreme trip distances or fares?
- Which drop-off locations have the highest average trip distances?
- What patterns could be useful for understanding taxi demand and revenue?

## Tableau Dashboard

The final Tableau dashboard presents the main findings from the EDA in an interactive format.

The dashboard is designed to help users explore:

- Trip volume
- Revenue
- Fares
- Tips
- Trip distance
- Time-based patterns
- Vendor differences
- Location-related patterns
