import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('/workspaces/Introduction_Python_MGIMO/Mall_Customers.csv')

average1 = df['Spending Score (1-100)'].mean()
most_freq = df['Genre'].value_counts().idxmax()
average2 = df['Age'].mean()

print("Средние траты клиента ", average1)
print("Пол клиента ", most_freq)
print("Возраст клиента ", average2)


df['Gender'] = df['Genre'].map({'Male': 0, 'Female': 1})
df.drop('Genre', axis=1, inplace=True)
kmeans = KMeans(n_clusters=5, random_state=0).fit(df)
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=df.columns)
rich_clients = cluster_centers.loc[cluster_centers['Annual Income (k$)'].idxmax()]

labels = kmeans.labels_
rich_clients_df = df.loc[labels == rich_clients.name]

rich_clients_df['Gender'] = rich_clients_df['Gender'].map({0: 'Male', 1: 'Female'})
rich_clients_df

average1 = rich_clients_df['Spending Score (1-100)'].mean()
most_freq = rich_clients_df['Gender'].value_counts().idxmax()
average2 = rich_clients_df['Age'].mean()

print("Средние траты богатого клиента ", average1)
print("Пол богатого клиента ", most_freq)
print("Возраст богатого клиента ", average2)