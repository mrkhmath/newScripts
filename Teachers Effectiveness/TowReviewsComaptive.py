import pandas as pd

# Load the Excel file
df = pd.read_excel("C:/Users/kh_ma/Downloads/TeacheingQualityReviewCompartive.xlsx")

import matplotlib.pyplot as plt

# Calculate the value counts (ratios) for each column, excluding NA values
ratios_22_23 = df['22-23'].dropna().value_counts(normalize=True)
ratios_23_24 = df['23-24'].dropna().value_counts(normalize=True)

# Plotting pie charts
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# We will recreate the pie charts with the color scheme from the user's provided image.
# The colors from the provided image appear to be green, red, orange, and a lighter orange.
# We'll define a custom color palette to match these colors as closely as possible.

# Custom color palette
colors = ['#008000', '#FF0000', '#FFA500', '#FFD700']  # Green, Red, Orange, Gold

# Now we will use these colors for our pie charts.
# We need to map the unique values in our dataframe to these colors.

# Since the number of colors in the provided palette may not match the number of unique values in our data,
# we will cycle through the palette as needed using the itertools.cycle function.

from itertools import cycle
color_cycle_22_23 = cycle(colors[:len(ratios_22_23)])
color_cycle_23_24 = cycle(colors[:len(ratios_23_24)])

# Assign colors to each unique value
colors_22_23 = {value: next(color_cycle_22_23) for value in ratios_22_23.index}
colors_23_24 = {value: next(color_cycle_23_24) for value in ratios_23_24.index}

# Plotting pie charts with the custom colors
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Pie chart for 22-23 with custom colors
axs[0].pie(ratios_22_23, labels=ratios_22_23.index, autopct='%1.1f%%', startangle=140, colors=[colors_22_23[value] for value in ratios_22_23.index])
axs[0].set_title('22-23 Teaching Quality Review')

# Pie chart for 23-24 with custom colors
axs[1].pie(ratios_23_24, labels=ratios_23_24.index, autopct='%1.1f%%', startangle=140, colors=[colors_23_24[value] for value in ratios_23_24.index])
axs[1].set_title('23-24 Teaching Quality Review')

plt.tight_layout()
plt.show()


