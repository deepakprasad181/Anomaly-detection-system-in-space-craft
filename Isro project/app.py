from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load CSV files for nominal and non-nominal data
nominal_data = pd.read_csv("NOMINAL.csv")
non_nominal_data = pd.read_csv("AE01.csv")

# Get list of available parameters
available_params = nominal_data.columns.tolist()

# Function to detect anomalies
def detect_anomalies(selected_parameter):
    # Calculate the difference between non-nominal and nominal data
    difference = non_nominal_data[selected_parameter] - nominal_data[selected_parameter]
    
    # Define a threshold for anomaly detection
    threshold = 0.1  # Adjust as needed
    
    # Detect anomalies
    anomalies = non_nominal_data[np.abs(difference) > threshold]
    
    # Print the number of values deviating beyond the threshold
    num_anomalies = len(anomalies)
    if num_anomalies == 0:
        anomaly_info = "No anomalies detected for parameter: {}".format(selected_parameter)
        top_anomalies = []
    else:
        anomaly_info = "Number of values deviating beyond the threshold: {}".format(num_anomalies)
        
        # Sort the anomalies by deviation
        anomalies_sorted = anomalies.copy()
        anomalies_sorted['Deviation'] = np.abs(difference[anomalies.index])
        anomalies_sorted = anomalies_sorted.sort_values(by='Deviation', ascending=False)

        # Prepare information for top anomalies
        top_anomalies = []
        N = min(3, num_anomalies)  # Change 3 to any desired number of top anomalies
        for i in range(N):
            index = anomalies_sorted.index[i]
            actual_value = non_nominal_data[selected_parameter].loc[index]
            deviation = anomalies_sorted['Deviation'].iloc[i]
            top_anomalies.append((index, actual_value, deviation))

    return anomaly_info, top_anomalies

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_parameter = request.form['parameter']
        anomaly_info, top_anomalies = detect_anomalies(selected_parameter)
        return render_template('index.html', available_params=available_params, anomaly_info=anomaly_info, top_anomalies=top_anomalies)
    return render_template('index.html', available_params=available_params, anomaly_info='', top_anomalies=[])

@app.route('/update_graph', methods=['POST'])
def update_graph():
    selected_parameter = request.json['parameter']
    anomaly_info, _ = detect_anomalies(selected_parameter)
    data = {
        'x': non_nominal_data.index.tolist(),
        'y': non_nominal_data[selected_parameter].tolist(),
        'type': 'scatter',
        'mode': 'lines',
        'name': 'Non-Nominal Data'
    }
    return jsonify([data])

if __name__ == '__main__':
    app.run(debug=True)
