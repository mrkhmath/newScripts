import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def graphSubj(su):
# Load the Excel file
    file_path = 'C:/Users/kh_ma/Downloads/Agg'+su+'.xlsx'
    data = pd.read_excel(file_path)

    # Calculate the difference in grades for each DOK level
    data['DOK1 Progress'] = data['Grade Total 23-24 DOK1'] - data['Grade Total 22-23 DOK1']
    data['DOK2 Progress'] = data['Grade Total 23-24 DOK2'] - data['Grade Total 22-23 DOK2']
    data['DOK3,4 Progress'] = data['Grade Total 23-24 DOK3,4'] - data['Grade Total 22-23 DOK3,4']

    # Define a function to categorize progress
    def categorize_progress(progress):
        if pd.isna(progress):
            return 'No Data'
        elif progress > 0:
            return 'Progressed'
        elif progress < 0:
            return 'Regressed'
        else:
            return 'No Change'

    # Apply the function to each DOK level
    data['DOK1 Category'] = data['DOK1 Progress'].apply(categorize_progress)
    data['DOK2 Category'] = data['DOK2 Progress'].apply(categorize_progress)
    data['DOK3,4 Category'] = data['DOK3,4 Progress'].apply(categorize_progress)

    # Count the number of students in each category for each DOK level
    dok1_counts = data['DOK1 Category'].value_counts()
    dok2_counts = data['DOK2 Category'].value_counts()
    dok3_4_counts = data['DOK3,4 Category'].value_counts()

    # Prepare the data for plotting
    categories = ['Progressed', 'Regressed', 'No Change', 'No Data']
    dok1_values = [dok1_counts.get(category, 0) for category in categories]
    dok2_values = [dok2_counts.get(category, 0) for category in categories]
    dok3_4_values = [dok3_4_counts.get(category, 0) for category in categories]

    dok3_4_progress = data[data['DOK3,4 Category'] != 'No Data']['DOK3,4 Category'].value_counts()

    # Prepare data for plotting
    progress_categories = dok3_4_progress.index
    progress_values = dok3_4_progress.values
    
    # Create the plot
    plt.figure(figsize=(6, 4))
    plt.bar(progress_categories, progress_values, color=['green', 'orange', 'blue'])
    # plt.xlabel('Progress Category')
    plt.ylabel('Number of Students')
    plt.title('Progression in DOK 3,4 - '+su.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
for s in ['math','science','english','arabic']:
    graphSubj(s)
  