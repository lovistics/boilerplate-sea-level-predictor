import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5)
    
    # Create first line of best fit (1880-2050)
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    # Calculate the line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    
    # Create array for line of best fit
    years_extended = pd.Series(range(1880, 2051))
    line_of_best_fit = slope * years_extended + intercept
    
    # Plot first line of best fit
    plt.plot(years_extended, line_of_best_fit, color='red', label='Best Fit Line (1880-2050)')
    
    # Create second line of best fit (2000-2050)
    recent_df = df[df['Year'] >= 2000]
    x_recent = recent_df['Year']
    y_recent = recent_df['CSIRO Adjusted Sea Level']
    
    # Calculate the line of best fit for recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(x_recent, y_recent)
    
    # Create array for recent line of best fit
    years_recent_extended = pd.Series(range(2000, 2051))
    line_of_best_fit_recent = slope_recent * years_recent_extended + intercept_recent
    
    # Plot second line of best fit
    plt.plot(years_recent_extended, line_of_best_fit_recent, color='green', label='Best Fit Line (2000-2050)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Adjust plot settings
    plt.grid(True)
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
