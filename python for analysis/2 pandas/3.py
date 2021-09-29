import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

reviews = pd.read_csv('winemag-data_first150k.csv')
# fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# reviews['points'].value_counts().sort_index().plot.bar(
#     ax=axes[0]
# )

# reviews['province'].value_counts().head(20).plot.bar(
#     ax=axes[1]
# )

# fig, axes = plt.subplots(2, 2, figsize=(16, 8))

# reviews['points'].value_counts().sort_index().plot.bar(
#     ax=axes[0][0], fontsize=12, color='forestgreen'
# )
# axes[0][0].set_title("Wine Scores", fontsize=18)

# reviews['variety'].value_counts().head(20).plot.bar(
#     ax=axes[1][0], fontsize=12, color='olive'
# )
# axes[1][0].set_title("Wine Varieties", fontsize=18)

# reviews['province'].value_counts().head(20).plot.bar(
#     ax=axes[1][1], fontsize=12, color='olive'
# )
# axes[1][1].set_title("Wine Origins", fontsize=18)

# reviews['price'].value_counts().plot.hist(
#     ax=axes[0][1], fontsize=12, color='forestgreen'
# )
# axes[0][1].set_title("Wine Prices", fontsize=18)
    
# plt.subplots_adjust(hspace=.3)
# sns.lineplot(x='price', y='points',data = reviews[reviews.price <100])
# print(plt.show())
