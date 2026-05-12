python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Step 1: Load Data
def load_data(file_path):
    return pd.read_csv(file_path)

# Step 2: Data Cleaning
def clean_data(df):
    df.dropna(inplace=True)
    df.rename(columns={
        'location': 'Location',
        'plot_size': 'Plot Size (Hectares)',
        'irrigation_method': 'Irrigation Method',
        'water_usage': 'Annual Water Usage (Cubic Meters)',
        'crop_types': 'Crop Types',
        'livestock_population': 'Livestock Population',
        'resource_use': 'Resource Use (Fertilizers, Seeds)',
        'renewable_energy': 'Renewable Energy Use',
        'gov_subsidies': 'Government Subsidies',
        'greenhouse_ops': 'Greenhouse Operations'
    }, inplace=True)
    return df

# Step 3: Basic Analysis - Calculate total water usage
def calculate_total_water_usage(df):
    return df['Annual Water Usage (Cubic Meters)'].sum()

# Step 4: Visualization
def plot_data(df):
    df['Plot Size (Hectares)'].plot(kind='hist', bins=10, color='skyblue')
    plt.title('Distribution of Plot Sizes')
    plt.xlabel('Plot Size (Hectares)')
    plt.ylabel('Frequency')
    plt.show()

# Example usage
file_path = 'agricultural_data.csv'
data = load_data(file_path)
cleaned_data = clean_data(data)
total_water_usage = calculate_total_water_usage(cleaned_data)
print(f"Total Water Usage: {total_water_usage} Cubic Meters")
plot_data(cleaned_data)
