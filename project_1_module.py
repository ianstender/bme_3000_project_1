#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:03:30 2023

@author: ianstender
"""
import numpy as np
from matplotlib import pyplot as plt



# %% Part 1: Load Data


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

# %% Part 2: Plot Raw Data
    
def plot_raw_data(signal_voltage, signal_time, units = 'V', title = ''):
    plt.plot(signal_time,signal_voltage, label='signal')
    plt.xlabel('Time (s)')
    plt.ylabel(units)
    plt.title(title)
    plt.grid()
    plt.legend()
    

# %% Part 3: Plot Events
def plot_events(label_samples, label_symbols, signal_time, signal_voltage):
    symbol_list = list(np.unique(label_symbols))
    for event_type in symbol_list:
        event_sample = label_samples[label_symbols == event_type]
        plt.scatter(signal_time[event_sample],signal_voltage[event_sample], label=event_type)
        plt.legend(loc='lower right')
        

# %% Part 4: Extract Trials
    
def extract_trials(signal_voltage, trial_start_samples, trial_sample_count):
    # Initialize an empty 2D array to store trials
    trials = np.empty((len(trial_start_samples), trial_sample_count)) # creates empty array to hold trials

    event_index = 0 # creates counter for row number in trial arrays
    
    # parse each row in trials, filling trial data in 
    for row in trials:
        start = trial_start_samples[event_index]
        end = start + trial_sample_count
        row_length = len(signal_voltage[start:end])
        
        # fills in complete rows 
        if row_length == trial_sample_count:
            trials[event_index,:] = signal_voltage[start:end]
        
        # fills in remaining values in row with nan values 
        else: 
            trials[event_index,:row_length] = signal_voltage[start:end]
            trials[event_index,row_length:(trial_sample_count-row_length)] = np.nan
        event_index +=1
        
    return trials

# %% Part 5: Plot Trial Means

def plot_mean_and_std_trials(signal_voltage,label_samples,label_symbols,trial_duration_seconds,fs,units,title):
    
    symbols = list(np.unique(label_symbols))
    
    plt.figure('Wrapper Function', clear = True)
    


    
    trial_means = {}
    trial_stds = {}
    
    for trial_type in symbols:
        
        # create input variables for extract_trial function
        trial_samples = label_samples[label_symbols == str(trial_type)]
        trial_start_samples = trial_samples - int(fs*(trial_duration_seconds/2))
        trial_sample_count = int(fs*(trial_duration_seconds))
        # extract trial
        trial = extract_trials(signal_voltage, trial_start_samples, trial_sample_count)
        
        # find mean and std of trial
        trial_mean = np.nanmean(trial,0)
        trial_std = np.nanstd(trial,0)
        
        trial_means[trial_type] = trial_mean
        trial_stds[trial_type] = trial_std
        
        trial_time = np.arange(0,trial_sample_count*(1/fs),(1/fs))
        plt.plot(trial_time,trial_mean, label = f'{trial_type} mean', linewidth = 2,)
        plt.fill_between(trial_time, y1 = -trial_std, y2 = trial_std, alpha = .4)
        plt.grid()
        plt.legend()
        
    
    return trial_means,trial_stds
    
  

