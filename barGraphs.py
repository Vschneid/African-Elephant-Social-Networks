import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('graph.csv')
data['Datetime'] = pd.to_datetime(data['Datetime'])
data['Month'] = data['Datetime'].dt.month

group_sizes = data.groupby('group').size()
valid_groups = group_sizes[group_sizes > 1].index
filtered_data = data[data['group'].isin(valid_groups)]

average_group_size = filtered_data.groupby('Month')['group'].count() / filtered_data.groupby('Month')['group'].nunique()

plt.figure(figsize=(10, 6))
average_group_size.plot(kind='bar')
plt.xlabel('Month')
plt.ylabel('Average Group Size per Observation')
plt.title('Average Group Size per Observation, by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

average_age = filtered_data.groupby('Month')['age'].mean()

plt.figure(figsize=(10, 6))
plt.bar(average_age.index, average_age)
plt.xlabel('Month')
plt.ylabel('Average Age')
plt.title('Average Age of Elephants per Month (Excluding Groups of One Elephant)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


data = pd.read_csv('graph.csv')
data['Datetime'] = pd.to_datetime(data['Datetime'])
data['Month'] = data['Datetime'].dt.month
adolescent_age_range = range(0, 30)

solo_elephant_observations = data[data['group'].duplicated(keep=False)].groupby('Month')['group'].count()
multi_elephant_observations = data[data['group'].duplicated(keep=False) == False].groupby('Month')['group'].count()

total_observations = data.groupby('Month')['group'].count()

percentage_solo_elephant = (solo_elephant_observations / total_observations) * 100
percentage_multi_elephant = (multi_elephant_observations / total_observations) * 100

filtered_data = data[data['group'].duplicated(keep=False) == False]

percentage_adolescents_solo = (filtered_data[filtered_data['age'].isin(adolescent_age_range)].groupby('Month')['group'].count() / solo_elephant_observations) * 100
percentage_adolescents_multi = (filtered_data[filtered_data['age'].isin(adolescent_age_range)].groupby('Month')['group'].count() / multi_elephant_observations) * 100

plt.figure(figsize=(10, 6))
plt.bar(percentage_solo_elephant.index, percentage_solo_elephant)
plt.xlabel('Month')
plt.ylabel('Percentage of Observations')
plt.title('Percentage of Observations with Solo Elephant Groups, by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(percentage_multi_elephant.index, percentage_multi_elephant)
plt.xlabel('Month')
plt.ylabel('Percentage of Observations')
plt.title('Percentage of Observations with Multi-Elephant Groups, by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(percentage_adolescents_solo.index, percentage_adolescents_solo)
plt.xlabel('Month')
plt.ylabel('Percentage of Adolescents')
plt.title('Percentage of Adolescents within Solo Elephant Groups, by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(percentage_adolescents_multi.index, percentage_adolescents_multi)
plt.xlabel('Month')
plt.ylabel('Percentage of Adolescents')
plt.title('Percentage of Adolescents within Multi-Elephant Groups, by Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
