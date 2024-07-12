import pandas as pd;

dataframe = pd.DataFrame({
  "Nome" : ["João", "Maria", "José", "Alice"],
  "Idade" : [20, 21, 19, 20],
  "Nota Final" : [5, 10, 6, 10]
})

#".sort_values(by=COLUMNS)" is the function for sorting the dataframes order.
#The "by" parameter asks for the columns(categories) you wanna make relevant while sorting.
#The "by" parameter accepts strings or strings list.
#Strings list is passed as argument when the sort bases in multiple categories.
#Also, there's the "ascending" parameter. 
#For the "ascending" parameter, the dataframe will be shown on a order based on the boolean argument.

dataframe.sort_values(by=["Idade", "Nota Final"], ascending=False, inplace=True)

print(dataframe)
