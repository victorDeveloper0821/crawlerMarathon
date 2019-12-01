#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:30:23 2019

@author: victortsai
"""
# 
import requests

myParam = {'id':'3a0e2289-a605-4eac-af30-f4af613f456d','rid':'ac508aeb-9f26-409c-9fb0-20c65a973498'}
response = requests.get('https://data.taipei/api/getDatasetInfo/downloadResource',params=myParam)

print(response.text)