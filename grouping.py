import os;
import pandas as pd;

os.chdir("worksheets-datasets");
dataframe = pd.read_csv(os.getcwd() + "/GasPricesinBrazil_2004-2019.csv", low_memory=False);

#Any dataframe contains a function for dealing with datas grouping.
#".groupby(COLUMNS)" is a returning function which returns an object.
""" grouping = dataframe.groupby("REGIÃO"); """

#This object contains "groups". 
#"groups" are also a property which is dictionary.
#For the dictionary: 
#INDEXES are categories.
#CONTENTS are the indexes for the registers which match the category.

#".groups" and ".indices" are the same thing.
""" indexes = grouping.groups["NORDESTE"];
indexes = grouping.indices["NORDESTE"]; """

#".get_group(INDEX)" is a function which returns a dataframe.
#This dataframe is filtered for the passed"groups/indices" dictionary's INDEX.
#In the following example, INDEX is equals to NORDESTE.
#Then, only registers where REGIÃO is NORDESTE will appear.
""" print(grouping.get_group("NORDESTE")); """

#===> REFACTORING THE PREVIOUS CHALLENGE 🛠🔥 <===

#For this challenge, you need to provide a new dataframe.
#This dataframe should contain the mean price for each PRODUTO for each REGIÃO.

#For grouping by more than one category:
#Simply, group by a list of categories.
#Ex.: dataframe.groupby(["REGIÃO", "ESTADO"]);

grouping = dataframe.groupby(["REGIÃO", "PRODUTO"]);
print(grouping.describe());