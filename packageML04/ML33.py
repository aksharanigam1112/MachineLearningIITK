# Feature extraction with PCA
# Dimension reduction technique
import pandas as pd
from sklearn.decomposition import PCA

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = pd.read_csv(filename, names=hnames)
array = df.values

x = array[:, 0:8]
y = array[:, 8]

pca = PCA(n_components=3)       # Reduce the dimension to 3
fit = pca.fit(x)                # or we can also use fit_transform(x), Simply fit() first it calculates variance of all x
resultx = pca.transform(x)      # Transform() then reduces the dimension by discarding min variance col
print("\nResult : \n",resultx)

# Summarize the data
print("\nExplained variance %s"%fit.explained_variance_ratio_)  # Always print this bcoz it decides whether we should use PCA or not