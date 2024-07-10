import os;

#Since Pandas is a library, it's necessary to import it.
import pandas as pd;

#KNOWING A DATASET 💡

#Then, we read our csv, excel and any files ==> pd.read_x("filepath", sep="separator_type")
#By default the csv separator type is a comma ",".  
dataset = pd.read_csv(os.getcwd() + "/worksheets-datasets/GasPricesinBrazil_2004-2019.csv", sep=";");

#".head(n)" is a function for RETURNING a certain quantity of dataset's rows.
some_rows = dataset.head(5);

#".info()" is a function for PRINTING the dataset's compostion information.
#informations = dataset.info();

#EXPLORING AND CONSTRUCTING A DATAFRAME 💡

#".shape()" is a property which contains the dataframe's dimensions (size).
dataframe_dimensions = dataset.shape;

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

#KNOWING A LITTLE ABOUT SERIES 💡
#A serie is an uni-dimensional array containing the data that composes a DATA ROW or DATA COLUMN.

#==> DATA COLUMNS <==
#For selecting a single COLUMN from a dataframe is possible to select it by like reffering to a index in a python dictionary (Data frames can be constructed using python dictionaries.).
""" print(dataset["ESTADO"])
print(dataset.get("ESTADO")); """

#Also, a single column can be selected like a property (It just work for non spaced name with no accent and no special characters).
""" print(dataset.ESTADO); """

#==>DATA ROWS<==
#"dataset.iloc[n]" (Index Locator) is a property for selecting a single ROW by it's index.
""" print(dataset.iloc[3]); """

#CONSTRUCTING A SERIES 💡
#A series can be constructed by passing a list of elements.
""" grade_one = 6.87;
grade_two = 7;
grade_three = 8.5;
average_grade = (grade_one + grade_two + grade_three) / 3;

series_data = [grade_one, grade_two, grade_three, average_grade]

simple_series = pd.Series(series_data);
print(simple_series)

complex_series = pd.Series(
  series_data, 
  index=["grade 1", "grade 2", "grade 3", "average"], 
  name="Student's Grades")

print(complex_series); """