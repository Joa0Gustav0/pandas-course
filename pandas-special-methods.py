import os;
import pandas as pd;
from functools import reduce

""" dataframe = pd.DataFrame({
  "A" : [1, 2, 3],
  "B" : [10, 20, 30],
  "C" : [100, 200, 300]
}, index=["Row 1", "Row 2", "Row 3"]) """


#".apply(function, axis=0 or 1)" is a dataframe function which applies a "def" function based on the dataframe context.
#This function, at the end, returns a new dataframe.
#Also, this function contains the "axis" parameter.
#The "axis" parameter accepts two possible arguments. They are the numbers 0 or 1.
#For 0, the vertical axis is choosed.
#For 1, the horizontal axis is choosed.

#In the following code, the function "sum_values" is applied to the dataframe at the horizontal axis.
#So, this function returns a new dataframe containing the result sum between the values that composes the horizontal axis from the original dataframe.
""" def sum_values(values_line) :
  return reduce(lambda previous, next: previous + next, values_line);

result_sum = dataframe.apply(sum_values, axis=0) """

#Also, a new column can be created to attatch the values returned from the function application.
""" dataframe["SUM"] = result_sum.values;
print(dataframe); """

#===> INTERESTING CHALLENGE 🤓🔥 <===
#At this challenge, you should create a new column and a new row.
#For the row, you need to attach the sums of all numbers vertically.
#For the column, you need to attatch the sums of all number horizontally.

""" def sum_series_values(series) :
  return series.sum();

vertical_sum = dataframe.apply(sum_series_values, axis=0);
dataframe.loc["Row 4"] = vertical_sum.values;

horizontal_sum = dataframe.apply(sum_series_values, axis=1);
dataframe["D"] = horizontal_sum;

print(dataframe) """

#===> CHALLENGE END 🏁 <===

#".map()" is also another special function from the series.
#This function walks through all the elements of a series.
#This is a returning function so it returns a new series.

""" raised_numbers = dataframe["A"].map(lambda element: element**2);

print(raised_numbers) """

#===> INTERESTING CHALLENGES 🤓🔥 <===
#For this challenge, you should "refill" the whole dataframe.
#Then, each value should match a certain pattern.
#The pattern is: "COLUMN LABEL" + "ROW NUMBER" + " RAISED NUMBER";
#Ex.: If the value 3 is at the ROW 3 at the COLUMN A => "A3 9"

""" rows = dataframe.index.to_list();
columns = dataframe.columns.to_list(); """

#Only using FOR LOOP:
""" for column in columns :
  for row in rows :
    dataframe.loc[row, column] = f"{column}{rows.index(row) + 1} {dataframe.loc[row, column]**2}"

print(dataframe); """

#Using FOR LOOP and MAP:
""" for column in columns :
  dataframe[column] = dataframe[column].map(
    lambda element: f"{column}{dataframe[column].values.tolist().index(element) + 1} {element**2}"
); """

""" print(dataframe); """

#===> CHALLENGE 2 👿 <====

#=> DATAFRAME:

os.chdir("worksheets-datasets")
challenge_df = pd.read_csv(os.getcwd() + "/GasPricesinBrazil_2004-2019.csv")

#For this challenge, you need to provide a new dataframe from the gave one.
#This dataframe should contain the mean price for each PRODUTO for each REGIÃO.

regions = challenge_df["REGIÃO"].unique();
dataframe = pd.DataFrame(index=regions, columns=challenge_df["PRODUTO"].unique());

for region in regions :
  #filter per region
  region_selection = challenge_df["REGIÃO"] == region;
  region_dataframe = challenge_df[region_selection];

  #unique products
  unique_region_products = region_dataframe["PRODUTO"].unique();
  products_mean_prices = list();

  for product in unique_region_products :
    #filter per product
    product_selection = region_dataframe["PRODUTO"] == product;
    product_dataframe = region_dataframe[product_selection];

    mean_price = product_dataframe.describe()["PREÇO MÉDIO REVENDA"].mean();
    products_mean_prices.append(
      pd.Series(mean_price, name=product)
    );

  for mean_price in products_mean_prices :
    dataframe.loc[region, mean_price.name] = mean_price.values[0]
    
#===> CHALLENGE END 🏁 (Solved in 26 min:09 s [PS.: I have not studied about GROUPING]) <===




  

