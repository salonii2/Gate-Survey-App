import pandas as pd
import numpy as np

# Number of rows in the dataset
num_samples = 1000

# Define possible values for each feature
materials = ['Metal', 'Wood', 'Glass', 'Composite']
locations = ['Indoor', 'Outdoor']
opening_mechanisms = ['Sliding', 'Swinging', 'Automatic', 'Folding']
security_features = ['Advanced Lock', 'Simple Latch', 'Reinforced', 'Standard Lock']
use_cases = ['Residential', 'Commercial', 'Industrial']
budgets = ['Low', 'Medium', 'High']
climate_suitabilities = ['Hot', 'Cold', 'Humid', 'All']
parking_spaces = ['Yes', 'No']
cable_layouts = ['Underground', 'Overhead', 'None']
storage_spaces = ['Small', 'Medium', 'Large', 'None']

# Randomly generate values for each feature
np.random.seed(42)  # For reproducibility

data = {
    'Gate_ID': range(1, num_samples + 1),
    'Material': np.random.choice(materials, num_samples),
    'Location': np.random.choice(locations, num_samples),
    'Height (ft)': np.round(np.random.uniform(5, 10, num_samples), 1),  # Heights between 5 and 10 feet
    'Width (ft)': np.round(np.random.uniform(3, 20, num_samples), 1),   # Widths between 3 and 20 feet
    'Opening_Mechanism': np.random.choice(opening_mechanisms, num_samples),
    'Security_Features': np.random.choice(security_features, num_samples),
    'Use_Case': np.random.choice(use_cases, num_samples),
    'Budget': np.random.choice(budgets, num_samples),
    'Climate_Suitability': np.random.choice(climate_suitabilities, num_samples),
    'Parking_Space': np.random.choice(parking_spaces, num_samples),
    'Cable_Layout': np.random.choice(cable_layouts, num_samples),
    'Storage_Space': np.random.choice(storage_spaces, num_samples)
}

# Create a DataFrame with the generated data
df_bulk = pd.DataFrame(data)

# Save the dataset to CSV
df_bulk.to_csv('C:\\Users\\SALONI SHARMA\\OneDrive\\Documents\\CU DOC\\gate ml\\bulk_gate_recommendation_dataset.csv', index=False)

print(f"Generated {num_samples} rows of data and saved to 'bulk_gate_recommendation_dataset.csv'")
