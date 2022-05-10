dataModeling_README

Streaming Analytics
Project_DataModeling.py

Description:
The purpose of this script is to build a model that can be used to make streaming service recommendations to users.

Reading data:
To read the data, point the “pd.read_csv()” line of code (line 11) towards the directory in which the file is stored. 

Output:
The script will automatically read the data, build a model, make recommendations, output the new data with recommendations to a .csv and then display two visuals. Visual one will show the number of potential subscribers by service and visual two will show the number of current subscribers who may unsubscribe as their interests do not align with the service.

Output Data Frame:
The data frame that is created with recommendations will automatically be written to the project directory folder (likely the folder where the script is stored). To change where the data is exported to, change the file path in line 68.