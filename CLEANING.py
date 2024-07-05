import pandas as pd

# Step 1: Read the CSV file
#... file location
input_file_path = '.../MotorVehicleCollisions.csv'
df = pd.read_csv(input_file_path)

# Step 2: Drop specific columns
columns_to_drop = ['ZIP CODE', 'LOCATION', 'CROSS STREET NAME', 'OFF STREET NAME']
df.drop(columns=columns_to_drop, inplace=True)

# Step 3: Drop rows with missing values in specific columns
columns_to_check = ['BOROUGH', 'ON STREET NAME', 'COLLISION_ID', 'CONTRIBUTING FACTOR VEHICLE 1']
df.dropna(subset=columns_to_check, inplace=True)

# Step 4: Remove rows where LATITUDE and LONGITUDE are 0 or empty
df = df[(df['LATITUDE'] != 0) & (df['LONGITUDE'] != 0) & (df['LATITUDE'].notna()) & (df['LONGITUDE'].notna())]

# Step 5: Rename specific fields
factor_renaming = {
    'Cell Phone (hand-Held)': 'Cell Phone',
    'Cell Phone (hand-free)': 'Cell Phone',
    'Cell Phone (hand-held)': 'Cell Phone',
    'Drugs(illegal)': 'Drugs (Illegal)',
    'Illnes': 'Illness',
    'Passing Too Closely': 'Passing or Lane Usage Improper',
    'Listening/Using Headphones': 'Other Electronic Device',
    'Reaction to Other Uninvolved Vehicle': 'Reaction to Uninvolved Vehicles'
}

df['CONTRIBUTING FACTOR VEHICLE 1'] = df['CONTRIBUTING FACTOR VEHICLE 1'].replace(factor_renaming)

# Step 6: Extract the year from the date column and create a new column
df['CRASH DATE'] = pd.to_datetime(df['CRASH DATE'], format='%m/%d/%Y')
df['YEAR'] = df['CRASH DATE'].dt.year

#just checking to see how many rows are left
num_rows = len(df)
print(f"Number of rows in the cleaned DataFrame: {num_rows}")

# Step 7: Save the updated DataFrame to a new CSV file
#... file location
output_file_path = '.../CleanedMotorVehicleCollisions.csv'
df.to_csv(output_file_path, index=False)

print(f"Cleaned CSV file saved to {output_file_path}")