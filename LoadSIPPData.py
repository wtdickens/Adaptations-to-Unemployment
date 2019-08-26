# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:20:39 2019

@author: w.dickens
"""
import pandas as pd
DataPath = "C:\\Users\\w.dickens\\Dropbox\\Adaptations to Unemployment"
DataPath += "\\SIPP Output\\datasets\\data files\\"
DataPath += "SIPP_2008_Monthly_MaleHSOnly.csv"

SIPPData = pd.read_csv(DataPath)
SIPPData