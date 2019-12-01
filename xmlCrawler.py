#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:26:03 2019

@author: victortsai
"""

# https://data.taipei/api/getDatasetInfo/downloadResource?id=bceb2963-d2dd-4f2d-929c-67c1c0d48667&rid=e6831708-02b4-4ef8-98fa-4b4ce53459d9

import requests

params = {'id':'bceb2963-d2dd-4f2d-929c-67c1c0d48667','rid':'e6831708-02b4-4ef8-98fa-4b4ce53459d9'}

response = requests.get('https://data.taipei/api/getDatasetInfo/downloadResource',params=params)

print(response.text)