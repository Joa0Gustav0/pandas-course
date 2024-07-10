import os;
import pandas as pd;

os.chdir(os.getcwd() + "/worksheets-datasets");
dataset = pd.read_csv("GasPricesinBrazil_2004-2019.csv", sep=";");

#SELECTING DATA BY INDEX 💡

#For selecting a single row, it's possible to use "dataframe.iloc[INDEX(n)]" (.iloc is a property!);
""" print(dataset.iloc[1]); """
#For selecting multiple rows, it's possible to still using "dataframe.iloc[n]" but using the SLICES system.
#Ex.: dataframe.iloc[:6];
""" print(dataset.iloc[:6]); """
#Ex.: Indexes from 10 to 15:
""" print(dataset.iloc[10:16]); """
#For selecting multiples indexes which do not follow an order, it's possible to pass a list of indexes inside the ".iloc[]":
""" print(dataset.iloc[[0, 3, 8, 12, 18]]); """

#The "dataframe.iloc[]" property works following the system of coordinates XY. (dataframe.iloc[Y, X]) 💡 
#Here, I' ve selected the fifth COLUMN's (X = 5) data - which reffers to "PRODUTO" - 
#From the 1, 5 and 10th ROWS (X = 1, 5, 10).
""" print(dataset.iloc[[1, 5, 10], 5]); """

#SELECTING DATA BY LABELS/NAMES 💡

""" df_dict = {
  "Graphics" : [4.9, 4.75, 4.5],
  "Sounds" : [4.6, 4.85, 4.55],
  "Satisfaction" : [4.9, 4.8, 4.95],
  "Price (R$)" : [2347, 3599.26, 1899]
}
dataframe = pd.DataFrame(df_dict, index=["XboxOne S", "PlayStation5", "Nintendo Switch"]);
dataframe["Price ($)"] = dataframe["Price (R$)"] / 5.42; """

#Numerical indexes always exists. They are just implicite.
#So, same in a dataframe with only labels, ".iloc" can be used for selecting data by numerical indexes.
""" print(dataframe.iloc[1,2]); """

#By the way, since we now have labels/names, a new property can be used for selecting data by name indexes (labels).
#"dataframe.loc[]" is a property that works like ".iloc". However, ".loc" asks for labels, and not for numerical indexes.
""" print(dataframe.loc[["PlayStation5", "Nintendo Switch"], "Satisfaction"]); """

#Selecting all rows. But also, only the "Graphics" and "Sounds" columns (Using ".loc").
""" print(dataframe.loc[dataframe.index,["Graphics", "Sounds"]])
print(dataframe.loc[:,["Graphics", "Sounds"]]) """

#SELECTING COLUMNS 💡

#A common way of selecting a single column is by passing it's name as the key of our dataset.
""" print(dataset["ESTADO"]); """
#Also, it's possible to select multiple columns is by passing a list containing the wished columns's names as the key of our dataset.
""" print(dataset[["ESTADO", "REGIÃO"]]);  """

#REMOVING COLUMNS 💡

#"del SELECTED_COLUMN" is used for removing a column (It is a inplace action 🚨).
""" print(dataset.head(3));
del dataset["Unnamed: 0"];
print(dataset.head(3)); """

#SAVING THE DATASET 💡

#"dataset.to_csv()" is the command for saving the dataset.
#The above command provide some parameters (Path; Index; Sep).
#PATH is the parameter for setting the path where the dataset should be saved.
#INDEX is the parameter (Boolean value) for setting the need (OR NOT) of the creation of a NEW COLUMN with indexes. (Normally, the argument for this is FALSE);
#SEP is the parameter for setting the separator type required for the dataset opening.
""" dataset.to_csv("GasPricesinBrazil_2004-2019.csv", index=False, sep=";") """

print(dataset.head(3));