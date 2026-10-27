# Electric Vehicle Market Performance & Insights
## Data Analytics Project Report

**Project domain:** Transportation / Electric Vehicles  
**Tools:** Python, pandas, CSV, Tableau (dashboard recreation guide)  
**Dataset files:** `ev_market_train.csv`, `ev_market_test.csv`

## 1. Problem statement
The electric vehicle market includes multiple vehicle categories, battery technologies, price levels and use cases. Comparing these attributes in raw tables is difficult. This project summarizes the supplied dataset and presents key measures through a dashboard to make category and regional comparisons easier.

## 2. Objectives
- Understand the dataset structure and data quality.
- Compare vehicle categories by count, range, price and customer rating.
- Review battery types, battery capacity and degradation fields.
- Compare records across market regions and recommended use cases.
- Provide a clear dashboard and reproducible analysis outputs.

## 3. Dataset overview
- Training dataset: **200,000 rows × 37 columns**.
- Test dataset: **100,000 rows × 37 columns**.
- The columns include model identity, category, model year, manufacturer, region, range, battery specifications, efficiency, price, ratings, sales and use-case fields.

## 4. Key findings
- Mean listed driving range is **324.5 km**; median is **337.9 km**.
- Mean battery capacity is **78.2 kWh**.
- Mean listed price is **$64,921**; median is **$42,815**.
- Mean customer rating is **4.09/5**.
- Mean value of the five-year battery degradation field is **12.31%**.
- Most common vehicle category by record count: **Two-Wheeler Scooter** (19,652 records).
- Highest average range by category: **Luxury Sedan** (550.6 km).
- Lowest average range by category: **Two-Wheeler Scooter** (105.0 km).
- Most frequent recommended use case: **Family Daily Use**.
- Most frequent battery type: **NMC**.

## 5. Data quality
- Total missing cells in training dataset: **18,996**.
- Fully duplicated rows: **1**.
- Missingness is not uniform across fields. Review the generated `analysis/missing_values.csv` before modelling.
- Inspect outliers, confirm units and check the meaning of missing values before imputing or removing records.

## 6. Dashboard design
The dashboard contains KPI cards and charts for:
1. Records by vehicle category.
2. Average range by category.
3. Battery technology mix.
4. Records by market region.
5. Average price by category.
6. Recommended use cases.
7. Category performance summary table.
8. Data-quality table showing fields with the most missing values.
It includes category and region filters. The HTML file is self-contained and can be opened directly in a browser.

## 7. Recommendations
1. Compare range and price together when evaluating value.
2. Compare battery range and degradation indicators rather than treating battery capacity as the only quality measure.
3. Compare vehicles within similar categories and use cases.
4. Handle missing values carefully and document every cleaning decision.
5. For a Tableau submission, recreate the recommended charts in Tableau and publish the workbook using Tableau Public.

## 8. Limitations
This report describes only the supplied dataset. Its source and representativeness have not been independently validated, so results should not be treated as verified facts about the entire global EV market. Descriptive analysis does not prove causal relationships.

## 9. Conclusion
The project converts the supplied EV dataset into an accessible dashboard and repeatable analysis workflow. It provides a starting point for exploring range, battery technology, pricing, region and use case while highlighting data-quality checks needed before more advanced modelling.
