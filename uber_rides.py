# Importing pandas library for data manipulation
import pandas as pd

# Importing numpy library for numerical computations
import numpy as np

# Importing matplotlib.pyplot for data visualization
import matplotlib.pyplot as plt

# Importing seaborn for enhancing the visual aesthetics of plots
import seaborn as sns

# Load the Uber dataset into a pandas DataFrame for analysis
dataset = pd.read_csv("uber dataset.csv")

# Display the first few rows of the dataset to understand its structure and contents
dataset.head()

# Display information about the dataset including data types, non-null counts, and memory usage
dataset.info()  # Providing insights into the structure and composition of our dataset

"""# Data Preprocessing

* Since we've identified numerous null values in the PURPOSE column, we'll fill these with the keyword 'NOT'.

* Alternatively, other strategies can be explored for handling null values.

"""

# Fill missing values in the 'PURPOSE' column with "NOT" as a placeholder
dataset['PURPOSE'].fillna("NOT", inplace=True)  # Filling missing purpose with placeholder "NOT"

# Converting START_DATE and END_DATE to datetime format for future analysis

# Transform the 'START_DATE' column to datetime format, gracefully handling any errors
dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')

# Modify the 'END_DATE' column to datetime format, gracefully managing any errors that may occur
dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

"""First, the START_DATE will be separated into separate columns for date and time. Then, the time portion will be categorized into four distinct categories: Morning, Afternoon, Evening, and Night"""

# Extracting date from the START_DATE column
dataset['date'] = pd.DatetimeIndex(dataset['START_DATE']).date

# Extracting hour from the START_DATE column
dataset['time'] = pd.DatetimeIndex(dataset['START_DATE']).hour

# Categorizing the time into day and night periods
dataset['day-night'] = pd.cut(x=dataset['time'],
                              bins=[0, 10, 15, 19, 24],
                              labels=['Morning', 'Afternoon', 'Evening', 'Night'])

"""After creating the new columns, we can proceed to remove any rows containing null values."""

# Dropping rows with missing values to ensure data integrity
dataset.dropna(inplace=True)  # Cool: "Cleaning up the dataset by removing any missing values!"

# Removing duplicate entries from the dataset to ensure data integrity and avoid redundancy
dataset.drop_duplicates(inplace=True)  # Keepin' it clean by dropping duplicates! 🧹✨

"""# Data Visualization

* In this section, we aim to gain insights and compare across all columns.

* Let's kick things off by examining the unique values in columns with object datatype.

"""

# Identifying columns with data type 'object' (typically categorical variables)
obj = (dataset.dtypes == 'object')

# Extracting the list of columns with object data type
object_cols = list(obj[obj].index)

# Initializing a dictionary to store unique values count for each categorical column
unique_values = {}

# Looping through each categorical column to find unique values count
for col in object_cols:
    unique_values[col] = dataset[col].unique().size

# Displaying the dictionary containing unique values count for each categorical column
unique_values

# Set the figure size for better visualization
plt.figure(figsize=(10, 6))

# Plotting the count of ride purposes using seaborn's countplot
sns.countplot(y=dataset['PURPOSE'], order=dataset['PURPOSE'].value_counts().index)

# Adding labels and title
plt.xlabel('Count')
plt.ylabel('Purpose')
plt.title('Distribution of Uber Ride Purposes')

# Rotating y-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.show()

"""# Histogram of Ride Distances

A histogram will visualize the distribution of ride distances, helping to understand the range and frequency of distances traveled.


"""

# Set the style
plt.style.use('seaborn-darkgrid')

# Plotting the histogram of ride distances
plt.figure(figsize=(10, 6))
plt.hist(dataset['MILES'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)

# Adding labels and title
plt.xlabel('Distance (Miles)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.title('Histogram of Ride Distances', fontsize=16)

# Adding grid lines for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding a vertical line for mean distance
mean_distance = dataset['MILES'].mean()
plt.axvline(mean_distance, color='red', linestyle='--', linewidth=2, label=f'Mean Distance: {mean_distance:.2f} miles')
plt.legend()

# Display the plot
plt.show()

"""# Bar Chart of Start Locations

This graph will display the frequency of rides starting from different locations.

"""

# Set style
sns.set_style("whitegrid")

# Plotting the bar chart with customized aesthetics
plt.figure(figsize=(12, 8))
sns.countplot(y=dataset['START'],
              order=dataset['START'].value_counts().index[:10],
              palette="viridis")  # Using Viridis color palette for a visually appealing look

# Adding labels and title with larger fonts
plt.xlabel('Count', fontsize=14)
plt.ylabel('Start Location', fontsize=14)
plt.title('Top 10 Start Locations for Uber Rides', fontsize=16)

# Rotating y-axis labels for better readability
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Adding a background grid for better readability
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adding a horizontal line to separate the title
plt.axhline(y=-1, color='grey', linestyle='--', linewidth=0.8)

# Removing spines
sns.despine()

# Show plot
plt.show()

"""# Now, we will compare the purposes of Uber rides across two different categories."""

# Set the background style
sns.set_style("whitegrid")

# Set the figure size for better visualization
plt.figure(figsize=(15, 5))

# Define custom colors for each category
colors = ['#1f77b4', '#ff7f0e']

# Plotting the count of Uber ride purposes with respect to categories
sns.countplot(data=dataset, x='PURPOSE', hue='CATEGORY', palette=colors)

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Adding labels and title
plt.xlabel('Purpose of Ride', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Count of Uber Ride Purposes by Category', fontsize=14)

# Add gridlines to the plot
plt.grid(True, linestyle='--', alpha=0.7)

# Customize legend
plt.legend(title='Category', title_fontsize='12', fontsize='10')

# Show plot
plt.show()

"""- Ride Categories: The majority of rides in the dataset belong to the "Business" category, indicating that Uber is primarily used for business-related purposes.

- Ride Purposes: The most common purposes of Uber rides include "Meeting", "Meal/Entertain", "Customer Visit", and "Errand/Supplies". This suggests that Uber is frequently used for various activities such as business meetings, dining out, and running errands.

- Ride Distances: The distribution of ride distances varies, with some rides being short (e.g., under 5 miles) and others being longer (e.g., over 10 miles). This indicates that Uber is used for both short-distance and long-distance travel.

- Start and Stop Locations: The dataset contains rides starting and ending at various locations, with certain locations appearing more frequently than others. This could reflect areas with high population density or business activity.

- Duration of Rides: The duration of rides varies, with some rides being shorter and others being longer. Factors such as traffic conditions and distance traveled likely influence ride durations.
"""
