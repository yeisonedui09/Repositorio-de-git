import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np


# 1 Import the Data
df = pd.read_csv('Proyectos/Medical Data Visualizer/medical_examination.csv')


# 2 Add an overweight column to the data
# IMC = peso(kg) / altura(m)**2 . Si > 25 es 1(True) , sino 0(False)
df['overweight'] = (df['weight'] / (df['height'] /100)**2 >25 ).astype('int8')

# 3 Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype('int8')
df['gluc'] = (df['gluc'] > 1).astype('int8')

# 4 Draw the Categorical Plot using pd.melt
def draw_cat_plot():
    # 5 Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df , id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])
    
    # 6 Group and reformat the data in df_cat
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7 Making the graphic
    g = sns.catplot(x='variable', y='total', hue='value',col='cardio', data=df_cat,kind='bar')
    
    # 8 Obtener the pic
    fig = g.figure

    # 9 Do not touch
    fig.savefig('Proyectos/Medical Data Visualizer/examples/catplot.png')
    return fig

# 10 # Draw the Heat Map 
def draw_heat_map():
    # 11 Clean the data in the df_heat
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
                & (df['height'] >= df['height'].quantile(0.025)) 
                & (df['height'] <= df['height'].quantile(0.975))
                & (df['weight'] >= df['weight'].quantile(0.025)) 
                & (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 12 Calculate the correlation matrix
    corr = df_heat.corr(numeric_only=True)
    
    # 13 Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14 Set up the matplotlib figure.
    fig, ax =plt.subplots(figsize=(12,12))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f',  square=True, linewidths=.5, cbar_kws={'shrink':.5},ax=ax)
    
    fig.savefig('Proyectos/Medical Data Visualizer/examples/heatmap.png')
    
    return fig

    
    
    