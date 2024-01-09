# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:26:49 2024

@author: dragan
"""

import pandas as pd
import pymysql

# Povezava s podatkovno bazo
connection = pymysql.connect(host='localhost', user='root', password='Sheki976!', database='vaja_3_tpb')
query = """
    SELECT calories, avg_heart_rate_element, vrsta_sporta
    FROM dimotherdata
"""

# Izvedba poizvedbe in shranjevanje rezultatov v pandas DataFrame
df = pd.read_sql_query(query, connection)

# Zapiranje povezave
connection.close()

# Shranjevanje rezultatov v CSV datoteko
df.to_csv('dimotherdata.csv', index=False)
