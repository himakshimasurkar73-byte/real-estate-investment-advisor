# Real Estate Investment Advisor

## 1. Project Introduction
The Real Estate Investment Advisor is a Python-based web
application that helps users explore property data, assess
investment potential, and estimate future property values.

## 2. Project Objectives
- Analyze housing property data.
- Explore property price trends.
- Assess investment potential using predefined rules.
- Estimate future property value using a mathematical formula.
- Search properties using filters.

## 3. Technologies Used
- Python
- Pandas
- Matplotlib
- Streamlit

## 4. Project Modules
1. Data Preprocessing
2. Exploratory Data Analysis
3. Investment Advisor
4. Interactive Web Application

## 5. Application Features
- Dashboard with dataset statistics.
- Investment Calculator with a score out of 5.
- Future Value Predictor.
- Market Trends with 10 charts.
- Property Search by city, property type, and BHK.

## 6. Investment Assessment
The application evaluates five criteria:
- Property price compared with the dataset average.
- Property age.
- Number of nearby schools.
- Number of nearby hospitals.
- Availability of security.

The final score is out of 5.

## 7. Future Value Prediction
The application uses compound growth:

Future Value = Current Value × (1 + Growth Rate / 100) ^ Years

The growth rate is an assumption, not a guaranteed forecast.

## 8. Important Limitation
The project uses a dataset that may contain synthetic
housing data. Its results should not be treated as verified
market predictions or guaranteed investment advice.

## 9. How to Run
1. Install Python.
2. Install the required libraries.
3. Open the project folder in VS Code.
4. Run the Streamlit application.

Command:
python -m streamlit run app_new.py