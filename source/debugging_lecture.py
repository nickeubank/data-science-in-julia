# Starter code for debugging exercises

import pandas as pd
gdppercap = pd.Series([34605, 34493, 12393, 44200, 10041, 
                       58138, 4709, 49284, 10109, 42536],
                      index=['Bahrain', 'Belgium', 'Bulgaria',
                             'Ireland', 'Macedonia', 'Norway', 
                             'Paraguay', 'Singapore', 
                             'South Africa', 'Switzerland']
                      )                   


avg_growth = pd.Series([-0.29768835, 0.980299584, 4.52991925, 
                        3.686556736, 2.621416804, 0.775132075, 
                        2.015489468, 3.345793635, 1.349993318, 
                        0.982775018],
                       index=['Bahrain', 'Belgium', 'Bulgaria', 
                              'Ireland', 'Macedonia', 'Norway', 
                              'Paraguay', 'Singapore', 
                              'South Africa', 'Switzerland']
                      )
