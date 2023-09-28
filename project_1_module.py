#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:03:30 2023

@author: ianstender
"""
import numpy as np
from matplotlib import pyplot as plt




def load_data(input_file):
    data = np.load(input_file)
    print(data.files)
    ecg_voltage = data['ecg_voltage']
    fs = data['fs']
    label_samples = data['label_samples']
    label_symbols = data['label_symbols']
    subject_id = data['subject_id']
    electrode = data['electrode']
    units = data['units']
    ecg_time = np.arange(0,len(ecg_voltage)*(1/fs),(1/fs))

    return ecg_voltage,fs,label_samples,label_symbols,subject_id,electrode,units, ecg_time
    
    
    
def plot_raw_data(signal_voltage, signal_time, units = 'V', title = ''):
    plt.figure(1,clear=True)
    plt.plot(signal_time,signal_voltage)
    plt.xlabel('Time (s)')
    plt.ylabel(units)
    plt.title(title)
    plt.grid()
    
def plot_events(label_samples, label_symbols, signal_time, signal_voltage):
    symbol_list = np.unique(label_symbols)
    print(symbol_list)
    for event_type in symbol_list:
        event_sample = label_samples[label_symbols == event_type]
        plt.scatter(signal_time[event_sample],signal_voltage[event_sample])
    