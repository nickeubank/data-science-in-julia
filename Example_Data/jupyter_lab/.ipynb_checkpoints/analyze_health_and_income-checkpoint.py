######################
#
# Import World Development Indicators
# and look at the relationship between income
# and health outcomes across countries
# 
######################

import pandas as pd
import numpy as np

# Download World Development Indicators
wdi = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small.csv")

# Get Mortality and GDP per capita for 2015


wdi = wdi.rename(columns={'Indicator Name': 'Indicator_Name', 
                          'Country Name': 'Country_Name',
                          'Indicator Code': 'Indicator_Code'})
mortality_and_income = wdi.query("Indicator_Name == 'Mortality rate, under-5 (per 1,000 live births)' | Indicator_Name == 'GDP per capita (constant 2010 US$)'")

mortality_and_income = mortality_and_income[['Country_Name', '2015', "Indicator_Code"]]

# Reshape 
mortality_and_income = mortality_and_income.pivot(index='Country_Name', 
                                                  columns='Indicator_Code', 
                                                  values=['2015'])
mortality_and_income = mortality_and_income.droplevel(0, axis='columns')
mortality_and_income = mortality_and_income.reset_index()


mortality_and_income['loggdppercap'] = np.log(mortality_and_income['NY.GDP.PCAP.KD'])

# Plot
from plotnine import *

(ggplot(mortality_and_income, 
        aes('loggdppercap', 'SH.DYN.MORT')) + 
        geom_point() + 
        geom_label(aes(label='Country_Name'), size=8) + 
        geom_smooth()
    )
