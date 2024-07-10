import os;
import pandas as pd;

dataset = pd.read_csv(os.getcwd() + "/worksheets-datasets/GasPricesinBrazil_2004-2019.csv", sep=";");

#When a column is selected, a series is returned. But, this same series IS NOT A COPY. IT'S A REAL REFERENCE to the existent column.💡
#"dataframe[COLUMN].copy()" is a function that REALLY return a series as a COPY.
#Copies are used as backups.
#ATTENTION FOR NOT LOSING DATAS! 🚨

#Here, I printed the original values and MADE A COPY(BACKUP).
""" print(dataset.head(3));
df_column_copy = dataset["REGIÃO"].copy(); """

#Here, I ATTATCHED A CONSTANT VALUE for the REGIÃO Column.
""" dataset["REGIÃO"] = "NORDESTE";
print(dataset.head(3)); """

#Here, I RECUPERATED THE ORIGINAL VALUES for the REGIÃO Column.
""" dataset["REGIÃO"] = df_column_copy;
print(dataset.head(3)); """

#===> FAST CHALLENGE 🔥 <===
#In this challenge, you should attatch a new constant value model to a column.
#The new constant value model should satisfie the sequent pattern: "REGIÃO" + Index (Ex.: "REGIÃO 33");

""" print(dataset.head(5));
region_column_copy = dataset.get("REGIÃO").copy(); """

df_rows, df_columns = dataset.shape;
#!Instead of using lambda function, could've used [f"REGIÃO {number}" for number in range(df_rows)].
""" new_column_values = list(map(lambda number: f"REGIÃO {number}", range(df_rows)))

dataset["REGIÃO"] = new_column_values;
print(dataset.head(5));

dataset["REGIÃO"] = region_column_copy;
print(dataset.head(5)); """

#===> CHALLENGE END 🏁 <===

#INSERTING NEW COLUMNS 💡
#For inserting a new column, it's possible to reffer to a NON existent key in our dataframe variable.
#Then, just insert the values, constant value or model of values.
#Ex.: dataframe["NON-EXISTENT-KEY"] = constant_value; 
""" print(dataset.head(5));

dataset["FORNECEDOR"] = [f"POSTO {index}" for index in range(dataset.shape[0])];
print(dataset.head(5)) """

#It's also possible to create a new column which is dependent of another.
#Ex.: dataframe["NON-EXISTENT-KEY"] = dataframe["EXISTENT-KEY"] + "-test";
""" print(dataset.head(5)); """

#Here, it is a small example of a new column created by the transformation of a pre-existent column of prices from REAL to DOLAR.
""" dataset["PREÇO MÉDIO REVENDA DÓLAR"] = dataset["PREÇO MÉDIO REVENDA"] / 5.42;

print(dataset["PREÇO MÉDIO REVENDA"]);
print("\n");
print(dataset["PREÇO MÉDIO REVENDA DÓLAR"]); """

#KNOWING ABOUT INDEXES 💡

#"dataset.index" is a property which contains the dataframe's indexes.
""" print(list(dataset.index)); """

#Also, indexes can be strings (labels).

df_dict = {
  "Graphics" : [4.9, 4.75, 4.5],
  "Sounds" : [4.6, 4.85, 4.55],
  "Satisfaction" : [4.9, 4.8, 4.95],
  "Price (R$)" : [2347, 3599.26, 1899]
}
dataframe = pd.DataFrame(df_dict, index=["XboxOne S", "PlayStation5", "Nintendo Switch"]);
dataframe["Price ($)"] = dataframe["Price (R$)"] / 5.42;

df_indexes = dataframe.index

print(dataframe);
print("\nThe above dataframe reffers to the analisys between: " + "".join(f"{console}; " for console in df_indexes));
