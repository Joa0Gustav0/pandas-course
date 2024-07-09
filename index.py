#Since Pandas is a library, it's necessary to import it.
import pandas as pd;

#KNOWING A DATASET 💡

#Then, we read our csv, excel and any files ==> pd.read_x("filepath", sep="separator_type")
#By default the csv separator type is a comma ",".  
worksheet = pd.read_csv("./worksheets/GasPricesinBrazil_2004-2019.csv", sep=";");

#".head(n)" is a function for RETURNING a certain quantity of dataset's rows.
some_rows = worksheet.head(5);

#".info()" is a function for PRINTING the dataset's compostion information.
#informations = worksheet.info();

#EXPLORING AND CONSTRUCTING A DATAFRAME 💡

#".shape()" is a property which contains the dataframe's dimensions (size).
dataframe_dimensions = worksheet.shape;

"""print(
  "This dataset contains {} rows and {} columns.".format(dataframe_dimensions[0], dataframe_dimensions[1])
);"""

#A dataframe can be constructed.
#"pd.Dataframe" is a method for constructing a dataframe by python dictionary where it's INDEXES ARE COLUMNS and CONTENTS ARE ROWS.
menu_dictionary = {
  "Product"  : ["burger", "french-fries", "coke"],
  "Price" : [5.75, 3, 2.5],
  "Available" : [True, True, False]
}
menu_dataframe = pd.DataFrame(menu_dictionary);

"""print(
  "This is the menu:\n", 
  menu_dataframe,
  f"\nThe menu contains {menu_dataframe.shape[0]} registers and {menu_dataframe.shape[1]} atributes.");"""

#"dataframe.columns" is a property which returns a string array containing the dataframe's columns names. 
"""print(f"The dataframe's columns are: {"".join(column + "; " for column in menu_dataframe.columns)}");"""

#"dataframe.rename" is a method for RETURNING a new dataframe by renaming an old one.
""" new_menu_dataframe = menu_dataframe.rename(columns={"Available" : "Product Status"}); """
""" print(new_menu_dataframe); """
#"inplace" is a possible parameter for renaming the current dataframe without a new one's creation.
""" menu_dataframe.rename(columns={"Available" : "Product-Status"}, inplace=True);
print(menu_dataframe) """
#For RENAMING ALL COLUMNS AT ONCE, it's possible to reach the ".columns" property and pass an array of strings.
"""menu_dataframe.columns=["Product-Name", "Product-Price", "Product-Status"];
print(menu_dataframe);"""