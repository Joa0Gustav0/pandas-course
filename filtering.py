import os;
import pandas as pd;

dataset_path = os.getcwd() + "/worksheets-datasets/GasPricesinBrazil_2004-2019.csv";
dataframe = pd.read_csv(dataset_path);

#For selecting DISTINCT (Unique) values from a column, "dataframe[COLUMN].unique()".
#The above command returns a list containing the unique values which remains to the respective column.
""" print(dataframe["ESTADO"].unique());
print(f"The research included {len(dataframe["ESTADO"].unique())} states.") """

#FILTERING USING DIRECT CONDITIONS 💡

#Stating some direct condition is a way of SELECTION.
#Ex.: dataframe[COLUMN] > 10.
#This way of SELECTION returns a BOOLEAN SERIES.
""" only_SE_state = dataframe["ESTADO"] == "SERGIPE"; """
#The same BOOLEAN SERIES can be used for FILTERING the dataframe.
""" print(dataframe[only_SE_state]); """

#FILTERING USING QUERIES 💡

#"dataframe.query(CONDITION)" is a function for FILTERING the results in the dataframe.
#!This function DO NOT return a BOOLEAN SERIES (It's not a selection, it's the real and ready FILTERED RESULTS).
#!Same if the query is a string, the COLUMN - which is a dataframe property - cannot be between quotation marks.
only_SE = dataframe.query("ESTADO == 'SERGIPE'");
#Notice that, after the filtering the indexes does not starts at 0.
#If you want the indexes for starting at 0, use the command ".reset_index()".
#By the way, if you reset the indexes, a new column containing the original indexes is created.
#If the created column is not desired, set the "drop" (BOOLEAN) parameter at the ".reset_index()" function. 
print(only_SE.reset_index(drop=True));