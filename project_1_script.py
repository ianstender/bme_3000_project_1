#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:07:32 2023

@author: ianstender
"""
import numpy as np
from matplotlib import pyplot as plt

import project_1_module as module

file_name = 'ecg_e0103_half1.npz'
ecg_voltage,fs,label_samples,label_symbols,subject_id,electrode,units, ecg_time = module.load_data(file_name)

module.plot_raw_data(ecg_voltage, ecg_time, 'Volts', 'ECG Data')

module.plot_events(label_samples, label_symbols, ecg_time, ecg_voltage)