import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('C:\\Users\\NCE\\pythonScripts\\DataAnalysis\\updated_MarkEnteredReport 23T2.csv')

# Set up the visual appearance of plots
sns.set_theme(style="whitegrid")

# Define a function to generate analysis for each teacher
def analyze_teacher_performance(dataframe):
    # Get a unique list of teachers
    teachers = dataframe['Teacher'].unique()
    
    # Prepare an empty DataFrame for summaries
    summaries = pd.DataFrame(columns=['Teacher', 'Mean', 'Median', 'Std Dev', 'Min', 'Max'])
    
    # Loop through each teacher to calculate summaries and generate plots
    for teacher in teachers:
        teacher_data = dataframe[dataframe['Teacher'] == teacher]['T2 Marks']
        mean = teacher_data.mean()
        median = teacher_data.median()
        std_dev = teacher_data.std()
        min_mark = teacher_data.min()
        max_mark = teacher_data.max()
        
        # Append summary to the summaries DataFrame
        new_row = pd.DataFrame([{'Teacher': teacher, 'Mean': mean, 'Median': median, 'Std Dev': std_dev, 'Min': min_mark, 'Max': max_mark}])
        summaries = pd.concat([summaries, new_row], ignore_index=True)
        # Generate and save a histogram for each teacher
        plt.figure(figsize=(10, 6))
        sns.histplot(teacher_data, kde=True, binwidth=5)
        plt.title(f'Marks Distribution for {teacher}')
        plt.xlabel('T2 Marks')
        plt.ylabel('Frequency')
        plt.savefig(f'C:\\Users\\NCE\\pythonScripts\\DataAnalysis\\marks_distribution_{teacher.replace(" ", "_")}.png')
        plt.close()
    
    # Save the summaries to an HTML file
    summaries.to_csv('C:\\Users\\NCE\\pythonScripts\\DataAnalysis\\teachers_performance_summary23T2.csv', index=False)

    return summaries

# Call the function
teacher_summaries = analyze_teacher_performance(df)

# Display the first few rows of the summaries DataFrame
teacher_summaries.head()
