# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to load and process data
def load_and_process_data(file_t1_path, file_t2_path):
    # Read the files into pandas DataFrames
    df_t1 = pd.read_csv(file_t1_path)
    df_t2 = pd.read_csv(file_t2_path)
    
    # Merge the two dataframes based on the Teacher column
    df_merged = pd.merge(df_t1[['Teacher', 'Mean']], df_t2[['Teacher', 'Mean']], on='Teacher', suffixes=('_T1', '_T2'))
    
    # Calculate the performance difference for each teacher
    df_merged['Performance Change'] = df_merged['Mean_T2'] - df_merged['Mean_T1']
    
    return df_merged

# Function to plot the data
def plot_performance_comparison(df_merged):
    # Set the figure size and layout
    plt.figure(figsize=(10, 8))

    # Number of teachers
    n_teachers = len(df_merged)
    index = np.arange(n_teachers)

    # Bar width
    bar_width = 0.35

    # Plotting with distinct colors
    plt.bar(index, df_merged['Mean_T1'], bar_width, color='royalblue', label='T1 Mean')
    plt.bar(index + bar_width, df_merged['Mean_T2'], bar_width, color='seagreen', label='T2 Mean')

    plt.xlabel('Teachers')
    plt.ylabel('Mean Performance Score')
    plt.title('Comparison of Teacher Performance between T1 and T2')
    plt.xticks(index + bar_width / 2, df_merged['Teacher'], rotation=90)
    plt.legend()
    plt.savefig(f'C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\t123VsT223.png')
    plt.close()
    # Add text for labels, title, and custom x-axis tick labels, etc.
    # plt.tight_layout()

    # plt.show()

# File paths
file_t1_path = 'C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\teachers_performance_summary23T1.csv'
file_t2_path = 'C:\\Users\\kh_ma\\Documents\\scripts\\DataAnalysis\\teachers_performance_summary23T2.csv'

# Load and process data
df_merged = load_and_process_data(file_t1_path, file_t2_path)

# Plot the performance comparison
plot_performance_comparison(df_merged)
