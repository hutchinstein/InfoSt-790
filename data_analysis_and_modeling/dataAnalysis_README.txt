dataAnalysis_README

Streaming Analytics
Project_DataAnalysis.py

Description:
The purpose of this script is to provide basic visualizations of the data being used.

Reading data:
To read the data, point the “pd.read_csv()” line of code (line 8) towards the directory in which the file is stored. 

Choosing Service:
This script will output two visuals for a certain streaming service that is specified. In order to specify the service that is shown, edit lines 62 and 63 to match which service you would like to create visualizations for.

Output:
As mentioned, this script will output two visuals. Visual one will be the distribution of data for each genre in the data set for the specified streaming service. For example, if we specify Netflix as our streaming service, the visual will show us how many people are interested in Action, Comedy, Drama movies and so on. The second visual will show us the distribution of data for how many people subscribe to other streaming services which also subscribe to the service that was specified. 