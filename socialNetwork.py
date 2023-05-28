import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('graph.csv')

grouped = df.groupby('group')
print(grouped.ngroups)

G = nx.Graph()
print(grouped.first())

for group_num, group_df in grouped:
    if(group_num == 20):
        print(group_num)
        print(group_df)
        #exit()
    individuals = group_df['ID'].tolist()
    
    for other_group_num, other_group_df in grouped:
        if group_num != other_group_num:
            shared_individuals = list(set(individuals) & set(other_group_df['ID'].tolist()))
            if shared_individuals:
                G.add_edge(group_num, other_group_num)
                
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

print("degree of \'173\': ", G.degree[20])


unique_values, frequencies = np.unique(G.degree, return_counts=True)
for value, frequency in zip(unique_values, frequencies):
    print(f"Value: {value}, Frequency: {frequency}")


# Get the degree histogram
#hist = nx.degree_histogram(G)

# Print the degree distribution
#for i, freq in enumerate(hist):
    #print(f"Degree {i}: {freq}")

clustering = nx.average_clustering(G)
print(f"Clustering coefficient: {clustering}")

#degree_sequence = sorted([d for n, d in G.degree()], reverse=True)

plt.hist(G.degree, edgecolor='black')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

nx.draw(G, with_labels=True)
plt.show()