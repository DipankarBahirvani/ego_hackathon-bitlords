library(shiny)
shinyUI(fluidPage(
  sidebarLayout(
    sidebarPanel(
              
                sliderInput('mileage', 'Mileage', min=200, max=51000, step = 100, value = 250),
                radioButtons('cyl', 'Battery loading capacity', c(10,12,14)),
                radioButtons('make', 'Make', c('e.Go Life','e.Go Mover')),
                radioButtons('leather', 'Central locking system', c('Yes','No')), 
                radioButtons('type', 'Car Type', c('sport','comfort','Eco')),
                actionButton('predictprice', 'Predict Price'))
    ,
  mainPanel(
    h3("Predicting Resale Price of used Cars"),
    tabsetPanel(
                tabPanel("Read Me", verbatimTextOutput('readme')),
                tabPanel('Predicted Price in USD', verbatimTextOutput('prediction')),
                tabPanel('Prediction Model Summary', verbatimTextOutput('summary')),
                tabPanel('Plots', plotOutput('plot'))
               )
   )
)))