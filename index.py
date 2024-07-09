#Since Pandas is a library, it's necessary to import it.
import pandas as pd;

#KNOWING A DATASET 💡

#Then, we read our csv, excel and any files ==> pd.read_x("filepath", sep="separator_type")  
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

print(
  "This is the menu:\n", 
  menu_dataframe,
  f"\nThe menu contains {menu_dataframe.shape[0]} registers and {menu_dataframe.shape[1]} atributes.");
