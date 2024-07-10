import os;
import pandas as pd;

dataset = pd.read_csv(os.getcwd() + "/worksheets-datasets/wine_catalogue.csv");

""" print(dataset.head()); """

""" dataset.info(); """

df_sizes = dataset.shape;
#Index 0 = Rows ; Index 1 = Columns;

""" print(f"Rows: {df_sizes[0]} ; Columns: {df_sizes[1]}"); """

#-------------
#==>CONSTRUCTORS<==
#==> DataFrame <==
catalogue_dict = {
  "Product" : ["Guitar", "Flute", "Piano"],
  "Price" : [98, 12, 570],
  "Quantity" : [12, 26, 3],
  "Available" : [True, True, False]
}

catalogue_df = pd.DataFrame(catalogue_dict);

#Remember columns are a parameter inside the rename function.
catalogue_df.rename(columns={"Product" : "Instrument", "Available" : "Is Available"}, inplace=True);

""" print(catalogue_df); """

#==> Series <==
""" print(catalogue_df["Instrument"]); """
""" print(catalogue_df.iloc[1]); """

movie_avaliation = [4.6, 4.2, 5];
avaliation_series = pd.Series(movie_avaliation, name="Avaliation Grade", index=["Movie 1", "Movie 2", "Movie 3"]);

""" print(avaliation_series) """
