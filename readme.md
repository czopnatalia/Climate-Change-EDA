# Climate Change Diagnostic Analysis (2000–2024) – Nowy Sącz Region

## Project Overview
This project provides a comprehensive descriptive and diagnostic analysis of climate change in the Nowy Sącz region, Poland. Utilizing ERA5 reanalysis data from the Copernicus Climate Data Store, the study examines 25 years of hourly meteorological observations (2000–2024) to identify long-term trends and anomalies.  

The analysis confirms a significant climate transformation in the region, shifting towards systemic warming and altered precipitation patterns.

## Key Features & Methodology
Data Engineering (ETL): Processing and cleaning large-scale datasets spanning over two decades using Python.

Exploratory Data Analysis (EDA): Statistical identification of temperature anomalies and precipitation variability relative to the reference period.

Correlation & Collinearity: Conducted Pearson correlation analysis and calculated Variance Inflation Factor (VIF) to refine predictors and avoid redundancy.

Anomaly Detection: Calculated climate norms based on a reference period (2000–2010) to highlight the acceleration of warming in the last decade.

Seasonality Analysis: Diagnosed the "defragmentation of winter" and the significant expansion of the thermal vegetation period.

Advanced Visualization: Interpreting complex correlation matrices and long-term climate trends using Matplotlib and Seaborn.

## Key Findings
Systemic Warming: Average annual temperatures show a clear upward trend, with 2024 recording a record anomaly of +2.4°C.

Season Shifts: Thermal summer is expanding by approx. 0.94 days/year, while thermal winter is shortening by 1.26 days/year.

Precipitation Changes: Although the frequency of heavy rain days has slightly decreased in this dataset, the concentration of events and rising temperatures suggest an increased risk of drought.

Snow Cover Decline: A steady decrease in the number of days with snow cover (-0.48 days/year) impacts regional water retention.

## Future ML Applications
The EDA results serve as a foundation for building several predictive models:

Binary Classification: Early warning systems for heatwaves and agricultural frost.

Regression: Forecasting energy demand for cooling/heating and predicting the first snowfall of the season.

Multi-class Classification: Categorizing hydrological risk levels (drought vs. flood).

## Tech Stack
Language: Python

Libraries: Pandas, NumPy, Xarray (for NetCDF), Scikit-learn (for VIF/Standardization), Matplotlib, Seaborn

Data Sources: ERA5 Reanalysis (Copernicus Climate Change Service CDS API)

## Conclusions & Detailed Analysis
For a comprehensive breakdown of the results, including long-term climate projections and strategic recommendations for the Nowy Sącz region, please refer to the full technical report:
[Full Diagnostic Report (PDF file)](report.pdf)