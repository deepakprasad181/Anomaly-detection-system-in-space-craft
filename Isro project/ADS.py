import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown

# Load CSV files for nominal and non-nominal data
nominal_data = pd.read_csv("NOMINAL.csv")
non_nominal_data = pd.read_csv("AE01.csv")

# Function to plot data and detect anomalies
def plot_selected_parameter(selected_parameter):
    plt.figure(figsize=(10, 6))
    
    # Plot nominal data
    plt.plot(nominal_data.index, nominal_data[selected_parameter], label='Nominal Data')
    
    # Calculate the difference between non-nominal and nominal data
    difference = non_nominal_data[selected_parameter] - nominal_data[selected_parameter]
    
    # Define a threshold for anomaly detection
    threshold = 0.1  # Adjust as needed
    
    # Detect anomalies
    anomalies = non_nominal_data[np.abs(difference) > threshold]
    
    # Plot non-nominal data
    plt.plot(non_nominal_data.index, non_nominal_data[selected_parameter], label='Non-Nominal Data')
    
    # Plot anomalies
    plt.scatter(anomalies.index, anomalies[selected_parameter], color='red', label='Anomalies')
    
    plt.title('Sensor Data Plot: {}'.format(selected_parameter))
    plt.xlabel('Time')
    plt.ylabel('Parameter Value')
    plt.legend()
    plt.show()
    
    # Print the number of values deviating beyond the threshold
    num_anomalies = len(anomalies)
    if num_anomalies == 0:
        print("No anomalies detected for parameter: {}".format(selected_parameter))
    else:
        print("Number of values deviating beyond the threshold:", num_anomalies)
        
        # Sort the anomalies by deviation
        anomalies_sorted = anomalies.copy()
        anomalies_sorted['Deviation'] = np.abs(difference[anomalies.index])
        anomalies_sorted = anomalies_sorted.sort_values(by='Deviation', ascending=False)

        # Print the indices, actual values, and deviations for the top N values
        N = min(3, num_anomalies)  # Change 3 to any desired number of top anomalies
        print("\nTop {} anomalies (index, actual value, deviation):".format(N))
        for i in range(N):
            index = anomalies_sorted.index[i]
            actual_value = non_nominal_data[selected_parameter].loc[index]
            deviation = anomalies_sorted['Deviation'].iloc[i]
            print("Index {}: Actual Value: {}, Deviation: {} points".format(index, actual_value, deviation))

# Get list of available parameters
available_params = nominal_data.columns.tolist()

# Dropdown widget for selecting parameters
param_dropdown = Dropdown(
    options=available_params,
    description='Select Parameter:'
)

# Function to handle dropdown selection
def on_dropdown_change(change):
    selected_param = change.new
    plot_selected_parameter(selected_param)

# Link dropdown to selection handler
param_dropdown.observe(on_dropdown_change, names='value')

# Display dropdown widget
display(param_dropdown)