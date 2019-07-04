######################
#
# Import World Development Indicators
# and look at the relationship between income
# and health outcomes across countries
# 
######################

# Download World Development Indicators
wdi = read.csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small.csv")

# Get Mortality and GDP per capita for 2015
library(tidyr)
mortality.and.income = wdi[wdi$Indicator.Name == "Mortality rate, under-5 (per 1,000 live births)" | 
                           wdi$Indicator.Name == "GDP per capita (constant 2010 US$)", 
                           c("Country.Name", "X2015", "Indicator.Code")]
mortality.and.income = spread(mortality.and.income, Indicator.Code, X2015)
mortality.and.income$loggdppercap = log(mortality.and.income$NY.GDP.PCAP.KD)

# Plot
library(ggplot2)
ggplot(mortality.and.income, 
       aes(loggdppercap, SH.DYN.MORT)) + 
       geom_point() + 
       geom_label(aes(label=Country.Name)) + 
       geom_smooth()

