import pandas as pd 

df = pd.read_csv("Sales-Export_2019-2020.csv")

df.columns = df.columns.str.strip()

for column in ["order_value_EUR", "cost"]:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    else:
        print(f"Warning: column '{column}' not found in the dataset.")

print("\n" + "=" * 60)
print("Exploratory Analysis")
print("=" * 60 + "\n")
print("Shape of Data")

numeric_columns = df.select_dtypes(include=['number']).columns

print("\n Important statistics")
if len(numeric_columns) >= 2:
    for column in numeric_columns[:2]:
        values = df[column]
        print(f"\nColumn: {column}")
        print(f"Count: {values.count()}")
        print(f"Mean: {values.mean():.2f}")
        print(f"Median: {values.median():.2f}")
        print(f"Minimum: {values.min():.2f}")
        print(f"Maximum: {values.max():.2f}")
        print(f"Standard deviation: {values.std():.2f}")
else:
    print("Must contain two or more numeric columns for the data")
