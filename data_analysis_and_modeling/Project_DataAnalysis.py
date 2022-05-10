import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# read data from csv file
data = pd.read_csv('~/Downloads/data.csv')

# drop columns "name" and "phone_number"
data = data.drop(columns=['name', 'phone_number'])

# creating lists of service names and genres
services = ['Amazon', 'Disney+', 'HBO Max', 'Hulu', 'Netflix', 'Paramount+']
genres = ['Action', 'Comedy', 'Drama', 'Family', 'Horror', 'Thriller']


# Preliminary Analysis - Visualizations

# creating data frame for Amazon subscribers
amazon = pd.DataFrame(
    data[data['Amazon'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()

# creating data frame for Disney+ subscribers
disney = pd.DataFrame(
    data[data['Disney+'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()

# creating data frame for HBO Max subscribers
hbo = pd.DataFrame(
    data[data['HBO Max'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()

# creating data frame for Hulu subscribers
hulu = pd.DataFrame(
    data[data['Hulu'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()

# creating data frame for Netflix subscribers
netflix = pd.DataFrame(
    data[data['Netflix'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()

# creating data frame for Paramount+ subscribers
paramount = pd.DataFrame(
    data[data['Paramount+'] == 1].sum(numeric_only=True, axis=0)
    , columns=['value']
).reset_index()


# Genre and Service Plots

# defining which service to make plots for.
# plot_service must be a data frame for a service listed above
# plot_text should be corresponding text associated with the data frame being used
plot_service = paramount
plot_text = "Paramount+"


# creating a plot showing genre interests for the streaming platform above.
genres_plot = sns.barplot(
    x='index',
    y='value',
    data=plot_service[plot_service['index'].isin(genres)].sort_values(['value'], ascending=False),
    color='royalblue'
)
genres_plot.bar_label(genres_plot.containers[0])
genres_plot.set(xlabel=plot_text, ylabel='Subscribers', title=str(plot_text + " Subscribers by Genre Interest"))
plt.show()

services_plot = sns.barplot(
    x='index',
    y='value',
    data=plot_service[plot_service['index'].isin(services)].sort_values(['value'], ascending=False),
    color='royalblue'
)
services_plot.bar_label(services_plot.containers[0])
services_plot.set(xlabel=plot_text, ylabel='Subscribers', title=str(plot_text + " Subscribers by Streaming Service"))
plt.show()
