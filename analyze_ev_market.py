from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "analysis"
train_path = DATA / "ev_market_train.csv"
test_path = DATA / "ev_market_test.csv"

train = pd.read_csv(train_path)
print("TRAIN SHAPE:", train.shape)
if test_path.exists():
    test = pd.read_csv(test_path)
    print("TEST SHAPE:", test.shape)

print("\nDATA TYPES")
print(train.dtypes.to_string())
print("\nMISSING VALUES (top 20)")
print(train.isna().sum().sort_values(ascending=False).head(20).to_string())
print("\nDUPLICATE ROWS:", train.duplicated().sum())

metrics = ["range_km", "battery_capacity_kwh", "efficiency_wh_per_km",
           "price_usd", "customer_rating", "co2_saved_tons_per_year",
           "battery_degradation_pct_5yr"]
print("\nNUMERIC SUMMARY")
print(train[metrics].describe().round(2).to_string())

summaries = {
    "category_summary.csv": train.groupby("category").agg(
        records=("vehicle_id", "count"), avg_range_km=("range_km", "mean"),
        avg_price_usd=("price_usd", "mean"), avg_rating=("customer_rating", "mean")),
    "region_summary.csv": train.groupby("market_region").agg(
        records=("vehicle_id", "count"), avg_range_km=("range_km", "mean"),
        avg_price_usd=("price_usd", "mean"), avg_rating=("customer_rating", "mean")),
    "battery_summary.csv": train.groupby("battery_type").agg(
        records=("vehicle_id", "count"), avg_range_km=("range_km", "mean"),
        avg_degradation_pct=("battery_degradation_pct_5yr", "mean")),
}
for filename, frame in summaries.items():
    frame.round(2).to_csv(OUT / filename)
    print(f"\n{filename}\n", frame.round(2).to_string())

train.isna().sum().sort_values(ascending=False).rename("missing_count").to_csv(OUT / "missing_values.csv")
train[metrics].describe().round(2).to_csv(OUT / "numeric_descriptive_statistics.csv")
print("\nAnalysis complete. Tables saved in:", OUT)
