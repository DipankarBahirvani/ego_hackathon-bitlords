# Shiny-App-Predicting-the-resale-price-of-cars-Multi-Linear-Regression

The objective of this project is to create an interactive web page that predicts the price of used car based on the inputs selected by the user.

# https://thanujhaa.shinyapps.io/regression_model_for_predicting_price_of_used_cars/


![capture 1](https://user-images.githubusercontent.com/35156789/41756938-010188e0-75ad-11e8-81c8-989dd0843967.JPG)


# Why use Shiny and R?

R is a popular and the most preferred tool for Data Science and Analytic exercises. However, it lacks a GUI experience. With Shiny, now R developers can generate interactive web pages directly with many prebuilt widgets available as R functions.

# Installation
Shiny can be installed in R using standard package installation using:
install.packages("shiny")  
Shiny has two components: ui and server.

# Structure
The shiny applications execute the following steps:
1.	The interface is generated by ui.R.
2.	The input is passed to server.R ,the data is processed in server.R, and it returns the output which is displayed back in the browser.

# Dataset
The caret package in R (short for Classification And Regression Training) package contains dataset
install.packages('caret')
Resale data for 2005 model year GM cars Kuiper (2008) collected data on Kelly Blue Book resale data for 804 GM cars (2005 model year).

data(cars)

str(cars)

'data.frame':    804 obs. of  18 variables:

$ Price      : num  22661 21725 29143 30732 33359 ...

$ Mileage    : int  20105 13457 31655 22479 17590 23635 17381 27558 25049 17319 ...

$ Cylinder   : int  6 6 4 4 4 4 4 4 4 4 ...

$ Doors      : int  4 2 2 2 2 2 2 2 2 4 ...


