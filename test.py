import os;
import pandas as pd;

os.chdir(os.getcwd() + "/worksheets-datasets");
dataframe = pd.read_csv("game-consoles-reviews-dataset.csv");

#To prevent the "Unnamed: 0" column from appearing,
#it's necessary to set the "index_label" parameter to FALSE while saving the dataset. 🚨

""" dataframe.loc["PlayStation4"] = [4.6, 4.75, 4.75, 2536, 0];
dataframe["Price ($)"] = dataframe["Price (R$)"] / 5.42; """