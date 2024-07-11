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
""" only_SE = dataframe.query("ESTADO == 'SERGIPE'"); """
#Notice that, after the filtering the indexes does not starts at 0.
#If you want the indexes for starting at 0, use the command ".reset_index()".
#By the way, if you reset the indexes, a new column containing the original indexes is created.
#If the created column is not desired, set the "drop" (BOOLEAN) parameter at the ".reset_index()" function. 
""" print(only_SE.reset_index(drop=True)); """

#===> FAST CHALLENGE 🔥 <===

#For this challenge, it's necessary to filter the dataframe.
#The filtering should satisfie two requirements:
#=> Only RIO DE JANEIRO's gas station.
#=> PREÇO MÉDIO DE REVENDA should be above R$2.

#Each way of filtering is unique. Only one filter per filter.
#If you want multiple filters at once, use "(FILTER) & (FILTER)".
""" selection = (dataframe["ESTADO"] == "RIO DE JANEIRO") & ~(dataframe["PREÇO MÉDIO REVENDA"] > 2);

filtered_df = dataframe[selection].reset_index(drop=True);
print(filtered_df); """

#===> CHALLENGE END 🏁 <===

#OPERATORS AT FILTERING 💡]

#While filtering, it's necessary, as seen before, to use conditions during the process of filtering.
#For this, there are OPERATORS (&, |, ~) for helping creating logics of conditions.
#The operator "&" means for "AND".
#The operator "|" means for "OR".
#The operator "~" means for "NOT".

#==> AND <==
#Here, only registers where the ESTADO is equal to SERGIPE AND PREÇO MÉDIO REVENDA is greater than 2 'll be selected.
""" aditive_selection = (dataframe["ESTADO"] == "SERGIPE") & (dataframe["PREÇO MÉDIO REVENDA"] >= 2);
filtered_df = dataframe[aditive_selection];
print(filtered_df.iloc[0]) """

#==> OR <==
#Here, only registers where the REGIÃO is equal to SUDESTE OR to NORDESTE 'll be selected.
""" alternative_selection = (dataframe["REGIÃO"] == "SUDESTE") | (dataframe["REGIÃO"] == "NORDESTE");
filtered_df = dataframe[alternative_selection];
print(filtered_df["REGIÃO"].unique()); """

#==> NOT <==
#Here, only the registers where the REGIÃO is NOT equal to SUDESTE AND NOT equal to NORDESTE 'll be selected.
""" adversative_selection = ~(dataframe["REGIÃO"] == "SUDESTE") & ~(dataframe["REGIÃO"] == "NORDESTE");
filtered_df = dataframe[adversative_selection];
print(filtered_df["REGIÃO"].unique()); """

#OPTIMIZING FILTERING 💡

#Using the previous knowledge: 
#While we are executing a filtering using more than one condition, pandas reads the WHOLE dataframe for each condition (3 Conditions => Pandas read the WHOLE dataframe 3 times).
#But, it's possible to be optimized.

#Firstly and inevitablely, the WHOLE original dataframe is readed.
#Then, only the registers where the state feature is equal to SERGIPE is selected.
""" state_selection = dataframe["ESTADO"] == "SERGIPE";
sergipe_registers = dataframe[state_selection]; """

#Next, only the dataframe filtered through the ESTADO column is readed.
#It prevents the original dataframe from being fully readed again.
""" price_selection = sergipe_registers["PREÇO MÉDIO REVENDA"] > 2;
filtered_df = sergipe_registers[price_selection];
print(filtered_df.iloc[0]) """

#This way filtering becomes optimized.

#===> INTERESTING CHALLENGES 🤓🔥 <===

#For this challenge, THREE (3) requirements need to be satisfied:
#=> Only SÃO PAULO OR RIO DE JANEIRO'S gas station;
#=> Only GASOLINA COMUM as the product;
#=> Only PREÇO MÉDIO REVENDA greater than 2;

product_selection = dataframe["PRODUTO"] == "GASOLINA COMUM";
only_gasolina = dataframe[product_selection];

state_selection = (only_gasolina["ESTADO"] == "SAO PAULO") | (only_gasolina["ESTADO"] == "RIO DE JANEIRO");
only_sp_rj = only_gasolina[state_selection];

price_selection = only_sp_rj["PREÇO MÉDIO REVENDA"] > 2;
filtered_dataframe = only_sp_rj[price_selection].reset_index(drop=True);

""" print(filtered_dataframe); """

#===> CHALLENGE 2 🔥 <===

#Now, use previous challenge's result for filtering it by the ANO.
#=> Only 2008, 2010 or 2012;

""" year_selection = (filtered_dataframe["ANO"] == 2008) | (filtered_dataframe["ANO"] == 2010) | (filtered_dataframe["ANO"] == 2012) """

#".isin" is a possible function for be used instead of "dataframe[COLUMN] in [values]" 💡
""" year_selection = filtered_dataframe["ANO"].isin([2008, 2010, 2012]); """

""" years_list = [2008, 2010, 2012];
filtered_by_year_df = filtered_dataframe.query("ANO in @years_list"); """

""" print(filtered_by_year_df["ANO"].unique()); """