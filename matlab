To translate the MATLAB code into Python and extend it for root cause analysis, you'll need to use libraries like Pandas for data manipulation and Matplotlib for plotting. Here's a Python version of the code:

```python
import pandas as pd
import matplotlib.pyplot as plt

def plot_sensor_data():
    # Load nominal and non-nominal datasets from Excel files
    try:
        nominal_data = pd.read_excel('DATA WITH PARAMETERS.xlsx') # Update with your nominal dataset file name
        non_nominal_data = pd.read_excel('DATA WITH PARAMETERS NON NOMINAL.xlsx') # Update with your non-nominal dataset file name
    except Exception as e:
        print(f"Error loading Excel files: {e}")
        return

    # Parameter names
    parameter_names = ['time', 'phaseBit', 'mass-dynamics', 'E1FiringBit', 'E2FiringBit', 'E3FiringBit', 'E4FiringBit', 
                       'CengFirBit - NA', 'Engine1-Thrust', 'Engine2-Thrust', 'Engine3-Thrust', 'Engine4-Thrust', 'CentalEngine-Thrust - NA', 
                       'EngTorque-Yaw', 'EngTorque-Roll', 'EngTorque-Pitch', 'Dynamics-MCMFPA-rVector-x', 'Dynamics-MCMFPA-rVector-y', 
                       'Dynamics-MCMFPA-rVector-z', 'Dynamics-MCMFPA-vVector-vx', 'Dynamics-MCMFPA-vVector-vy', 'Dynamics-MCMFPA-vVector-vz', 
                       'qbody-1', 'qbody-2', 'qbody-3', 'qbody-4', 'wbody-1', 'wbody-2', 'wbody-3', 'Dynamics-latitude-ME', 'Dynamics-longitude-ME', 
                       'Dynamics-height-ME', 'LanderPositionENU-East', 'LanderPositionENU-North', 'LanderPositionENU-Up(Not same as height)', 
                       'LanderVelocityENU-East', 'LanderVelocityENU-North', 'LanderVelocityENU-Up', '-1', 'LanderHeightFromSurface (With DEM)', 
                       'LanderYawWRTVertical', 'LanderRollWRTVertical', 'LanderPitchWRTVertical', 'R1-AvgThrust', 'R2-AvgThrust', 'R3-AvgThrust', 
                       'R4-AvgThrust', 'R5-AvgThrust', 'R6-AvgThrust', 'R7-AvgThrust', 'R8-AvgThrust', 'TotalRCSAvgThrust', 'NetThrustFromEngineAndRCS', 
                       'DynamicsHeight(Height from mean moon surface)', 'Dynamics-J2000-rVector-x', 'Dynamics-J2000-rVector-y', 'Dynamics-J2000-rVector-z', 
                       'Dynamics-J2000-vVector-vx', 'Dynamics-J2000-vVector-vy', 'Dynamics-J2000-vVector-vz', 'VerticalVelocity(velocity along radial mcmf vector)', 
                       'arc range', 'HorizontalVelocity (Net horizontal velocity, norm taken so always positive)', 'lNav-Dynamics-r-NUE(1)', 
                       'lNav-Dynamics-r-NUE(2)', 'lNav-Dynamics-r-NUE(3)', 'lNav-Dynamics-v-NUE(1)', 'lNav-Dynamics-v-NUE(2)', 'lNav-Dynamics-v-NUE(3)', 
                       'lNav-Qlocaldyn-1', 'lNav-Qlocaldyn-2', 'lNav-Qlocaldyn-3', 'lNav-Qlocaldyn-4', 'Usable Oxidizer Left', 'Usable Fuel Left', 
                       'Oxidizer Consumed', 'Fuel Consumed', 'ThrusterConsumedMass (Outdated)', 'ALSPath', 'local surface slope', 'curvilinear cross (Z) landing site distance', 
                       'curvilinear along (X) landing site distance', 'Net horizontal distance from landing site norm(X,Z)', 'ThrusterConsumedMass', 
                       'TotalAccInIIU-x', 'TotalAccInIIU-y', 'TotalAccInIIU-z', 'CdA-Ox-1', 'CdA-Ox-2', 'CdA-Ox-3', 'CdA-Ox-4', 'CdA-Fu-1', 'CdA-Fu-2', 
                       'CdA-Fu-3', 'CdA-Fu-4']

    # Plotting function
    def plot_selected_parameter(selected_parameter):
        # Plot nominal data
        plt.plot(nominal_data['time'], nominal_data[selected_parameter], 'b', label='Nominal Data')

        # Plot non-nominal data
        plt.plot(non_nominal_data['time'], non_nominal_data[selected_parameter], 'r.', label='Non-Nominal Data')

        # Set plot title and labels
        plt.title(f'Parameter: {selected_parameter}')
        plt.xlabel('Time')
        plt.ylabel(selected_parameter)

        # Add legend
        plt.legend(loc='best')
        plt.show()

    # Create a dropdown menu for parameter selection
    selected_parameter = parameter_names[0]

    # Plot selected parameter
    plot_selected_parameter(selected_parameter)

# Call the function
plot_sensor_data()
```

This code will plot the nominal and non-nominal data for the selected parameter. To extend it for root cause analysis, you'll need to specify what analysis you want to perform and provide additional details on how to identify root causes.