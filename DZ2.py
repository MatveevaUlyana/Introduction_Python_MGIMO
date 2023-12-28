import pandas as pd
from sklearn.cluster import KMeans

# Чтение датасета
df = pd.read_csv('/workspaces/Introduction_Python_MGIMO/Mall_Customers.csv')

average1 = df['Spending Score (1-100)'].mean()
most_freq = df['Genre'].value_counts().idxmax()
average3 = df['Age'].mean()

print("Средние траты клиента ", average1)
print("Пол клиента ", most_freq)
print("Возраст клиента ", average3)


df['Gender'] = df['Genre'].map({'Male': 0, 'Female': 1})
df.drop('Genre', axis=1, inplace=True)
kmeans = KMeans(n_clusters=5, random_state=0).fit(df)
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=df.columns)
rich_clients = cluster_centers.loc[cluster_centers['Annual Income (k$)'].idxmax()]

labels = kmeans.labels_
rich_clients_df = df.loc[labels == rich_clients_label]
