# Tableau Build Guide — Electric Vehicle Market Performance & Insights

## Connect the supplied dataset
1. Open Tableau Desktop or Tableau Public.
2. Select **Connect → To a File → Text File**.
3. Open `data/ev_market_train.csv`.
4. Confirm `model_year` is numeric; numeric measures such as `range_km`, `battery_capacity_kwh`, `efficiency_wh_per_km`, `price_usd`, `customer_rating` and `annual_sales_units` should be measures.
5. Save the workbook as `EV_Market_Performance_Insights.twbx`.

## Create these worksheets
1. **KPI - Average Range**: drag `range_km` to Text and change aggregation to AVG.
2. **KPI - Average Price**: drag `price_usd` to Text; use AVG and currency formatting.
3. **KPI - Battery Capacity**: drag `battery_capacity_kwh` to Text and use AVG.
4. **Vehicle Mix by Category**: `category` to Rows; `vehicle_id` to Columns as COUNT; sort descending.
5. **Average Range by Category**: `category` to Rows; `range_km` to Columns as AVG.
6. **Average Price by Category**: `category` to Rows; `price_usd` to Columns as AVG.
7. **Battery Technology**: `battery_type` to Rows; `vehicle_id` to Columns as COUNT.
8. **Market Region Mix**: `market_region` to Rows; `vehicle_id` to Columns as COUNT.
9. **Use Case Distribution**: `recommended_use_case` to Rows; `vehicle_id` to Columns as COUNT.
10. **Data Quality**: use a text table showing null counts from the exported `analysis/missing_values.csv` if you want to show data-quality checks.

## Assemble dashboard
- Create a new Dashboard, set a size around 1200 × 850.
- Place three KPI sheets along the top.
- Place category mix, range and price charts in the middle.
- Place battery type, region and use-case charts below.
- Add filters for `category`, `market_region`, `battery_type`, `manufacturer` and `model_year`; choose **Apply to Worksheets → All Using This Data Source**.
- Add the title **Electric Vehicle Market Performance & Insights**.
- Add a note: “Descriptive results are based on the supplied training dataset.”

## Publish and get a demo URL
1. Sign in to Tableau Public.
2. Choose **Server → Tableau Public → Save to Tableau Public As**.
3. Give the workbook a public title and wait for publishing to finish.
4. Copy the published view URL and use it as the SkillWallet Demo Link.
5. Use your GitHub repository URL as the GitHub Link.

Note: this guide does not create or publish a Tableau workbook automatically. You must perform the Tableau steps above in your own Tableau account.
