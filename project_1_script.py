#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:07:32 2023

Script for BME3000 Project 1. Calls functions from module_1 in order to plot graphs
Raw data figure is a graph containing data right from the npz file unmanipulated
Trials figure is a graph with one normal trial and one arrhythmic trial plotted on top of one another
Wrapper function figure is a graph of the mean for all normal trials plotted on top of the mean for all arrhythmic trials in addition to the standard deviation of these two data sets

@author: ianstender
"""
import numpy as np
from matplotlib import pyplot as plt

import project_1_module as module

# %% Load data

file_name = 'ecg_e0103_half1.npz'
ecg_voltage,fs,label_samples,label_symbols,subject_id,electrode,units, ecg_time = module.load_data(file_name)



# %% Plot raw data
plt.figure('Raw Data',clear=True)
module.plot_raw_data(ecg_voltage, ecg_time, 'Volts', 'RAW ECG Data')


# %% Plot events
module.plot_events(label_samples, label_symbols, ecg_time, ecg_voltage)

plt.xlim(1910,1912) # limit scope of plot to two normal beats and two arrhythmic beats


# %% Extract Trials

def check_size(trial_data, trial_name, expected_size):
    """
    Checks to see if data is the exact shape that is expected

    Parameters
    ----------
    trial_data : array
        Data who's size is being checked.
    trial_name : string
        Name of data that is being checked.
    expected_size : tuple
        The expected shape of data.

    Returns
    -------
    None.

    """
    if trial_data.shape == expected_size:
        print(f'{trial_name} is correct size.')
        
    else: 
        print(f'{trial_name} is not correct size.')
    

# determine start time and duration of trials
t_start = -0.5
duration = 1

# create time array and figure for trials
trial_time = np.arange(0,250*(1/fs),(1/fs))
plt.figure('Trials', clear = True)



# extract normal trials
normal_samples = label_samples[label_symbols == 'N']

normal_trial_start_samples = normal_samples + int(fs*t_start)

normal_trial_sample_count = int(fs*duration)

normal_trials = (module.extract_trials(ecg_voltage,normal_trial_start_samples,normal_trial_sample_count))


# check if normal trials is correct size
expected_trial_size = (len(normal_trial_start_samples),normal_trial_sample_count)

check_size(normal_trials,'Normal Trials', expected_trial_size)


# extract arrhythmic trials 
arrhythmic_samples = label_samples[label_symbols == 'V']

arrhythmic_trial_start_samples = arrhythmic_samples + int(fs*t_start)

arrhythmic_trial_sample_count = int(fs*duration)

arrhythmic_trials = (module.extract_trials(ecg_voltage,arrhythmic_trial_start_samples,arrhythmic_trial_sample_count))

# check if arrhythmic trials is correct size
trial_size = (len(normal_trial_start_samples),normal_trial_sample_count)

check_size(normal_trials,'Arrythmic Trials', trial_size)


# plot one normal trial and one arrhythmic trial
plt.plot(trial_time,normal_trials[10], label = 'Normal Trial')
plt.plot(trial_time,arrhythmic_trials[10], label = 'Arrhythmic Trial')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (Volts)')
plt.title('Normal trial vs. Arrhythmic Trial')
plt.grid()
plt.legend()





# %% Plot Trial Means


file_name = 'ecg_e0103_half1.npz'


title = 'Plot Trial Means and Standard Deviation'
trial_duration_seconds = 1


symbols, trial_time, mean_trial_signal = module.plot_mean_and_std_trials(ecg_voltage, label_samples, label_symbols, trial_duration_seconds, fs, units, title)

print(symbols)
print(trial_time)
print(mean_trial_signal)
# %% Save files

saved_filename = f'ecg_means_{subject_id}.npz'

module.save_means(symbols, trial_time, mean_trial_signal, saved_filename)

test_data = np.load(saved_filename)

if np.array_equal(test_data['symbols'],symbols):
    print('Symbols data correctly saved')
    
if np.array_equal(test_data['trial_time'],trial_time):
    print('Trial_time data correctly saved')
    
if np.array_equal(test_data['mean_trial_signal'], mean_trial_signal):
    print('mean_trial_signal data correctly saved')
    
