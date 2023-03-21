import json
import pandas as pd

# Load JSON file into a list of dictionaries
with open('comp_23725602_ranking.json') as f:
    data = json.load(f)

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame in a table view
print(df)
