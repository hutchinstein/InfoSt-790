import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier


pd.options.mode.chained_assignment = None

data = pd.read_csv('~/Downloads/data.csv')

model_data = data.drop(columns=['name', 'phone_number'])

services = ['Amazon', 'Disney+', 'HBO Max', 'Hulu', 'Netflix', 'Paramount+']
genres = ['Action', 'Comedy', 'Drama', 'Family', 'Horror', 'Thriller']


# target matrix
y = model_data.iloc[:, 0:6].to_numpy()

# predictor matrix
x = model_data.iloc[:, 6:12].to_numpy()


model = MultiOutputClassifier(
    RandomForestClassifier(random_state=1)
    , n_jobs=-1
).fit(x, y)

results = model.predict_proba(x)


for n in range(0, 6):
    col_name = str(services[n] + '_prob')
    class_name = str(services[n] + '_class')
    data[col_name] = results[n][:, 1]
    data[class_name] = results[n][:, 1].round()


probs = ['Amazon_prob', 'Disney+_prob', 'HBO Max_prob', 'Hulu_prob', 'Netflix_prob', 'Paramount+_prob']
classes = ['Amazon_class', 'Disney+_class', 'HBO Max_class', 'Hulu_class', 'Netflix_class', 'Paramount+_class']
results = ['Amazon_result', 'Disney+_result', 'HBO Max_result', 'Hulu_result', 'Netflix_result', 'Paramount+_result']

result_data = data


# for result columns:
#    1 = 'is subscribed, but shouldn't be'
#   -1 = 'is not subscribed, but should be'
#    0 = 'has correct subscription status'


for n in range(0, 6):
    sub_name = str(services[n] + ' pot sub')
    unsub_name = str(services[n] + ' pot unsub')
    result_data[sub_name] = np.where(
        (result_data[services].iloc[:, n] - result_data[classes].iloc[:, n]) == -1, 1, 0)
    result_data[unsub_name] = np.where(
        (result_data[services].iloc[:, n] - result_data[classes].iloc[:, n]) == 1, 1, 0)

subs = ['Amazon pot sub', 'Disney+ pot sub', 'HBO Max pot sub', 'Hulu pot sub',
        'Netflix pot sub', 'Paramount+ pot sub']
unsubs = ['Amazon pot unsub', 'Disney+ pot unsub',
          'HBO Max pot unsub', 'Hulu pot unsub',
          'Netflix pot unsub', 'Paramount+ pot unsub']

result_data.to_csv('~/Downloads/790_Project_Output.csv')

exit()
# Everything below this exit() function is just chart creation for insights.


# Creating data frame for graph data
graph_data_pot_sub = pd.DataFrame(
    result_data[subs].sum(numeric_only=True, axis=0)
    , columns=['potential_subs']
).reset_index()

graph_data_pot_unsub = pd.DataFrame(
    result_data[unsubs].sum(numeric_only=True, axis=0)
    , columns=['potential_unsubs']
).reset_index()


graph_data_pot_sub['index'] = graph_data_pot_sub['index'].str.replace(' pot sub', '')
graph_data_pot_unsub['index'] = graph_data_pot_unsub['index'].str.replace(' pot unsub', '')


graph_data_pot_unsub = pd.merge(
    graph_data_pot_unsub,
    (pd.DataFrame(result_data[services].sum(numeric_only=True, axis=0), columns=['total_subs']).reset_index()),
    left_on="index",
    right_on="index"
)

graph_data_pot_unsub['unsub_percent'] = graph_data_pot_unsub['potential_unsubs'] / graph_data_pot_unsub['total_subs']


# Charts for potential subscribers and potential un-subscribers by streaming service
sub_plot = sns.barplot(
    x='index',
    y='potential_subs',
    data=graph_data_pot_sub.sort_values(['potential_subs'], ascending=False),
    color='royalblue'
)
sub_plot.bar_label(sub_plot.containers[0])
sub_plot.set(xlabel="Streaming Service",
             ylabel='Potential Subscribers',
             title="Potential Subscribers by Streaming Service")
plt.show()


unsub_plot = sns.barplot(
    x='index',
    y='potential_unsubs',
    data=graph_data_pot_unsub.sort_values(['potential_unsubs'], ascending=False),
    color='royalblue'
)
unsub_plot.bar_label(unsub_plot.containers[0])
unsub_plot.set(xlabel="Streaming Service",
               ylabel='Potential Un-Subscribers',
               title="Potential Un-Subscribers by Streaming Service")
plt.show()


total_plot = sns.barplot(
    x='index',
    y='total_subs',
    data=graph_data_pot_unsub.sort_values(['total_subs'], ascending=False),
    color='royalblue'
)
total_plot.bar_label(total_plot.containers[0])
total_plot.set(xlabel="Streaming Service",
               ylabel='Total Subscribers',
               title="Total Subscribers by Streaming Service")
plt.show()


exit()
