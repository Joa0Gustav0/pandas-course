import os;
import pandas as pd;

dataset = pd.read_csv(
  os.getcwd() + "/worksheets-datasets/aliexpress_pet_supplies.csv"
);

""" print(dataset.head(5)); """

dataframe_sizes = dataset.shape;
""" print(f"\nThis dataset contains {dataframe_sizes[0]} registers and {dataframe_sizes[1]} columns."); """

#-------------------

dataframe_data = {
  "Product" : ["Coke", "Bread", "Wine", "Butter", "Cereal"],
  "Quantity" : [89, 56, 40, 38, 26],
  "Price" : [1.75, .6, 6.25, .75, 2.45],
  "Available" : [True, True, False, True, False]
}
catalogue_dataframe = pd.DataFrame(dataframe_data);

catalogue_dataframe.rename(columns={"Available" : "Status"}, inplace=True);
catalogue_dataframe.columns = ["Product Name", "Product Quantity", "Product Price", "Product Available"];

print(f"This dataframe's columns are: {"".join(" " + column for column in catalogue_dataframe.columns)}");