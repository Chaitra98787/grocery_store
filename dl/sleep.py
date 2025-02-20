import pandas as pd
import numpy as np

# Load the original dataset
dataset = pd.read_csv('sleepanalysis.csv')

# Define a function to generate synthetic records
def generate_synthetic_data(num_records):
    synthetic_data = pd.DataFrame()
    synthetic_data['Person ID'] = range(dataset['Person ID'].max() + 1, dataset['Person ID'].max() + 1 + num_records)
    synthetic_data['Gender'] = np.random.choice(dataset['Gender'].unique(), size=num_records)
    synthetic_data['Age'] = np.random.randint(18, 65, size=num_records)
    synthetic_data['Occupation'] = np.random.choice(dataset['Occupation'].unique(), size=num_records)
    synthetic_data['Sleep Duration'] = np.random.uniform(4, 10, size=num_records)
    synthetic_data['Quality of Sleep'] = np.random.randint(1, 10, size=num_records)
    synthetic_data['Physical Activity Level'] = np.random.randint(0, 100, size=num_records)
    synthetic_data['Stress Level'] = np.random.randint(1, 10, size=num_records)
    synthetic_data['BMI Category'] = np.random.choice(dataset['BMI Category'].unique(), size=num_records)
    synthetic_data['Blood Pressure'] = np.random.choice(dataset['Blood Pressure'].unique(), size=num_records)
    synthetic_data['Heart Rate'] = np.random.randint(60, 100, size=num_records)
    synthetic_data['Daily Steps'] = np.random.randint(0, 20000, size=num_records)
    synthetic_data['Sleep Disorder'] = np.random.choice(dataset['Sleep Disorder'].unique(), size=num_records)
    
    return synthetic_data

try:
    # Generate 1000 new records
    new_records = generate_synthetic_data(1000)

    # Combine with existing dataset
    combined_dataset = pd.concat([dataset, new_records], ignore_index=True)

    # Save to a new CSV file
    combined_dataset.to_csv('expanded_sleepanalysis.csv', index=False)

    # Print success message
    print(f"Generated {len(new_records)} new records.")
    print("Combined dataset saved as 'expanded_sleepanalysis.csv'.")

except Exception as e:
    print(f"An error occurred: {e}")
