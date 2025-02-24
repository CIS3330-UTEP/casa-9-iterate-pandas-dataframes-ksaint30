import pandas as pd
df = pd.read_csv("big-mac-full-index.csv")
# iterrow()
for index, row in df.iterrows():
    total_price =row['local_price']*row['dollar_ex']
    print(f"{row['name']} ${total_price}")

# apply()
def calculate_local_price(row):
    return f"{row['name']} - Local Price: {row['local_price']}"

results = df.apply(calculate_local_price, axis=1)
for res in results.head(6):
    print(res)