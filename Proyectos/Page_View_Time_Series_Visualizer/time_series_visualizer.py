import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Import data
df = pd.read_csv('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Page View Time Series Visualizer/fcc-forum-pageviews.csv',
                 index_col='date',
                 parse_dates=True)

# Clean Data: Keep only yhe data between 2.5 and 97.5 percentile
df = df[(df['value'] >= df['value'].quantile(0.025)) 
        & (df['value'] <= df['value'].quantile(0.975))]


# Draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))

    ax.plot(df.index ,df['value'], color='red', linewidth=1 )

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.savefig('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Page View Time Series Visualizer/examples/line_plot.png')
    return fig

# Draw bar plot
def draw_bar_plot():
    # Make a copy of DataFrame
    df_bar = df.copy()
    
    # Create de column year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Create a categorical column for month
    month_order = ['January', 'February', 'March', 'April',
        'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December']
    
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)
    
    # Group by year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Draw the bar plot
    fig = df_bar.plot(kind='bar', figsize=(10,8)).figure

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    fig.savefig('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Page View Time Series Visualizer/examples/bar_plot.png')
    return fig

# Draw Box plot
def draw_box_plot():
    #Make a copy of DataFrame
    df_box = df.copy()
    
    # Reset the index
    df_box.reset_index(inplace=True)
    
    # Make a column year and month
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    # Create a categorical column for month
    month_order = [
    'Jan', 'Feb', 'Mar', 'Apr',
    'May', 'Jun', 'Jul', 'Aug',
    'Sep', 'Oct', 'Nov', 'Dec'
    ]
    
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    
    # Draw the box plot
    fig, ax = plt.subplots(1,2, figsize=(20,7))

    sns.boxplot(x='year', y='value', data = df_box, ax= ax[0])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1])

    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    
    fig.savefig('C:/Users/yeiso/OneDrive/Escritorio/Repositorio de git/Proyectos/Page View Time Series Visualizer/examples/box_plot.png')
    return fig
    
    
    
    
    
    
    