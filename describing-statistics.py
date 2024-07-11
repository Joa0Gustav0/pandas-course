import os;
import pandas as pd;

dataset_name = "GasPricesinBrazil_2004-2019.csv";
os.chdir("worksheets-datasets");
dataframe = pd.read_csv(os.getcwd() + f"/{dataset_name}");

#".describe()" is a method which returns the describing statistics according to a dataframe.

#Ex.: Select the minimum PREÇO MÉDIO REVENDA value.
""" minimum_value = dataframe["PREÇO MÍNIMO REVENDA"].describe().min();
print(minimum_value); """

#Ex.: Select the average and the standard deviation from PREÇO MÍNIMO REVENDA.
""" selection = dataframe["PREÇO MÍNIMO REVENDA"].describe();
average = selection.mean();
standard_deviation = selection.std();

print(f"For PREÇO MÍNIMO REVENDA: \nThe average value is: {average} \nThe standard deviation is: {standard_deviation}"); """

#If you want to verificate the countage of appearence for each values of a column:
#".value_counts()" is a method for doing it.
#Ex.: Count how many times each state appeared at the records.
""" states = dataframe["ESTADO"];
print(states.value_counts()) """