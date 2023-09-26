#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:03:30 2023

@author: ianstender
"""
import numpy as np

data = np.load('ecg_e0103_half1.npz')
print(data.files)

# def load_data(input_file)
#     np.load(input_file)