import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Sea Level Predictor/epa-sea-level.csv')
    
    # Create a scatter plot 
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # First line of best fit (all data)
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend to future 
    years_extended = pd.Series(range(1880,2051))
    
    # Using y = mx + n
    y_pred = result.slope * years_extended + result.intercept 
    
    # Draw this prediction
    ax.plot(years_extended, y_pred, color='red')
    
    #* Second line of best fit (from year 2000 onward)
    
    # Make a DataFrame with the data 
    df_recent = df[df['Year'] >= 2000]
    
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Extend to future 
    years_recent = pd.Series(range(2000,2051))
    
    # Using y = mx + n
    y_recent = result_recent.slope * years_recent + result_recent.intercept
    
    # Draw this prediction
    ax.plot(years_recent, y_recent, color='green')
    
    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    fig.savefig('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Sea Level Predictor/examples/sea_level_plot.png')
    return ax
    
     
    
    