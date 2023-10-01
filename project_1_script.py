#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:07:32 2023

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
plt.plot(trial_time,normal_trials[10], label = 'normal trial')
plt.plot(trial_time,arrhythmic_trials[10], label = 'arrhythmic trial')
plt.xlabel('Time (s)')
plt.ylabel('V')
plt.title('Normal trial vs. Arrhythmic Trial')
plt.grid()
plt.legend()
