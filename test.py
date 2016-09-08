# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

zones = pd.ExcelFile("D:/Python_Projects/Training/zones.xlsx")
zones.sheet_names
df = zones.parse('Sheet1')
df.head()