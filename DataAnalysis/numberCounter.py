import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:/Users/NCE/Downloads/MarkEnteredReport 23T2.csv'  # Update this with the path to your Excel file
data = pd.read_csv(file_path)

# Define a function to calculate the statistics
def calculate_score_statistics(df, column_name="T2 Marks"):
    above_65 = df[column_name] >= 60
    above_75 = df[column_name] > 75
    below_60 = df[column_name] < 60
    return above_65.sum(), above_75.sum(), below_60.sum()

# Group data by grade level and subject, then calculate statistics
grade_subject_stats = data.groupby(['Grade', 'Subject Name']).apply(calculate_score_statistics).reset_index()

# Rename columns for clarity
grade_subject_stats.columns = ['Grade', 'Subject Name', 'Stats']
grade_subject_stats[['Above 65%', 'Above 75%', 'Below 60%']] = pd.DataFrame(grade_subject_stats['Stats'].tolist(), index=grade_subject_stats.index)
grade_subject_stats.drop('Stats', axis=1, inplace=True)

# Export to CSV
csv_file_path = 'C:/Users/NCE/Downloads/grade_subject_statistics.csv'
grade_subject_stats.to_csv(csv_file_path, index=False)

# Calculate average statistics for visualization
average_stats = grade_subject_stats.groupby('Subject Name')[['60% or Above', 'Above 75%', 'Below 60%']].mean().reset_index()

# Plot
fig, ax = plt.subplots(figsize=(14, 8))
ind = range(len(average_stats))
width = 0.25       

plt.bar(ind, average_stats['Above 65%'], width, label='Above 65%', color='green')
plt.bar([i + width for i in ind], average_stats['Above 75%'], width, label='Above 75%', color='blue')
plt.bar([i + 2*width for i in ind], average_stats['Below 60%'], width, label='Below 60%', color='red')

plt.xlabel('Subject Name')
plt.ylabel('Average Number of Students')
plt.title('Average Student Performance by Subject Across All Grades')
plt.xticks([i + width for i in ind], average_stats['Subject Name'], rotation=90)
plt.legend(loc='best')
plt.tight_layout()

# Save the chart as an image
fig.savefig('C:/Users/NCE/Downloads/student_performance_chart.png')
