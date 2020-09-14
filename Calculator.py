# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

# Mean-Variance-Standard Deviation Calculator

import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  x = np.array(list).reshape(3, 3)
  calculations = {
    k: [func(x, axis=ax).tolist()
      for ax in [0, 1, None]] 
      for (k, func) 
      in zip(["mean", "variance", "standard deviation", "max", "min", "sum"], 
             [np.mean, np.var, np.std, np.max, np.min, np.sum])
  } 


  return calculations

try:
    calculate([1,2,3,4,5,6,7,8,9])
except ValueError as error:
    print(error)
