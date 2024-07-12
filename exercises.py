import os;
import pandas as pd;

os.chdir("worksheets-datasets");
dataset_filename = "GasPricesinBrazil_2004-2019_preprocessado_final.csv";
dataframe = pd.read_csv(os.getcwd() + "/" + dataset_filename, low_memory=False);

#Remove all the registers where the ANO is 2019.
""" ANO_selection = dataframe["ANO"] != 2019;
dataframe = dataframe[ANO_selection] """

#Each PRODUTOs registers quantity for each REGIÃO
""" grouping = dataframe.groupby("PRODUTO");

print(grouping["REGIÃO"].value_counts()) """

#How much do the GASOLINA COMUM prices variated in 2018 at SÃO PAULO?
""" year_selection = dataframe["ANO"] == 2018;
only_2018 = dataframe[year_selection];

state_selection = only_2018["ESTADO"] == "SAO PAULO";
only_sp_2018 = only_2018[state_selection];

product_selection = only_sp_2018["PRODUTO"] == "GASOLINA COMUM";
only_sp_2018_gasolina = only_sp_2018[product_selection];

print(only_sp_2018_gasolina["PREÇO MÉDIO REVENDA"].std()) """

#How much do the GASOLINA COMUM and the ETANOL prices variated in 2018 at SÃO PAULO?
""" gasolina_etanol_sp_2018 = dataframe.query("ANO == 2018 and ESTADO == 'SAO PAULO' and (PRODUTO == 'GASOLINA COMUM' or PRODUTO == 'ETANOL HIDRATADO')");

grouping = gasolina_etanol_sp_2018.groupby("PRODUTO");
print(grouping["PREÇO MÉDIO REVENDA"].describe()) """
