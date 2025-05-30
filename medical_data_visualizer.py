import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.value_counts().reset_index(name = 'total').sort_values(by = 'variable')

    # 7
    cat_plot_graph = sns.catplot(data = df_cat, kind='bar', x='variable' , y= 'total', hue='value', col = 'cardio')

    # 8
    fig = cat_plot_graph.fig 

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025))&
    (df['height'] <= df['height'].quantile(0.975))&
    (df['weight'] >= df['weight'].quantile(0.025))&
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(corr, center = 0, annot = True, fmt = '.1f', linewidths = 0.5, linecolor = 'red', cbar_kws = {'shrink':0.5}, square = True, mask = mask,)

    fig.savefig('heatmap.png')
    return fig
