import os;
import pandas as pd;

dataframe = pd.read_csv(os.path.join(os.getcwd(), "worksheets-datasets", "catalogo-rs-joias.csv"), sep=";", index_col="Item/Código")

print(dataframe)

dataframe.drop(index="4587E3A", inplace=True);

print(dataframe)