import os;
import pandas as pd;

os.chdir(os.getcwd() + "/worksheets-datasets");
dataframe = pd.read_csv("GasPricesinBrazil_2004-2019.csv");

#DATA TYPE COERSION 💡

#In Pandas, there are several data types.
#Each of them reffer and behave on a unique mode.
#They can be separated by: Dates, Numeric Datas and Objects 
#OBJECTS are a generic datatype, commonly, reffered to STRINGS.

#In Pandas, for executing a data type coersion, the commands follow a certain pattern.
#Parsing to DATES: "pd.to_datetime()";
#Parsing to NUMERIC DATAS: "pd.to_numeric";

#PARSING TO DATE DATA TYPE:
""" for atribute in ["DATA INICIAL", "DATA FINAL"] :
  dataframe[atribute] = pd.to_datetime(dataframe[atribute]); """

#PARSING TO NUMERIC DATA TYPE:

#"pd.to_numeric()" contains a important parameter.
#The "erros" parameter requires an argument for deciding what to do in case of errors during coersion.
#There are 2 possible arguments:
#"coerce" is used to set the target datas as NaN in case of coersion error.
#"raise" is used to throw an exception in case of coersion error.

""" for atribute in dataframe.columns[13:18] :
  dataframe[atribute] = pd.to_numeric(dataframe[atribute], errors="coerce");

dataframe.info(); """

#After the numeric coersion, it's notable the presence of some datas which were marked as NaN/Null.
#At data cleasing, it's necessary to deal with Null Values.

#".isnull()" is a function which returns a boolean series based on the verification of Null/Not-Null values.
""" null_selection = dataframe["PREÇO MÉDIO DISTRIBUIÇÃO"].isnull(); """

#".fillna()" is a function for filling the cells which contains null values with a choosed DEFAULT VALUE.
#Also, if wou need different values for different columns, ".fillna()" contains the "value" parameter.
#For "value" parameter, you can attatch a python dictionary. 
#For the dictionary's indexes, you asign the columns name.
#For the disctionary's indexes's contents, you asign the new DEFAULT VALUE.
""" dataframe.fillna(0, inplace=True); """

""" dataframe.fillna(value={
  "PREÇO MÁXIMO DISTRIBUIÇÃO" : 0,
  "DESVIO PADRÃO DISTRIBUIÇÃO" : "NÃO INFORMADO"
},inplace=True); """

#Also, it's possible to simply delete all the registers/rows which contain null values.
#".dropna()" is a function that can do this.
#If this command is used carelessly, it's possible to lose some relevant datas! 🚨

""" dataframe.dropna(inplace=True); """
