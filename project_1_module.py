#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:03:30 2023

Module containing several functions used to load, manipulate, and graph data

@author: ianstender
"""
import numpy as np
from matplotlib import pyplot as plt



# %% Part 1: Load Data


def load_data(input_file):
    """
    Loads npz file and converts each varible into its own array.

    Parameters
    ----------
    input_file : array
        Npz file converted into array to allow for manipulations.

    Returns
    -------
    ecg_voltage : array
        A 1D array of all voltages sampled in trial.
    fs : array
        A 1D array of the sampling frequency in Hz.
    label_samples : array
        A 1D array listing the time indexes when events occur.
    label_symbols : array
        A 1D array indicating the symbol of each event.
    subject_id : array
        A 1D array of the subject's id.
    electrode : array
        A 1D array saying which elecrode's data was used in the data set.
    units : array
        Units electrode measured in.
    ecg_time : array
        A 1D array for time elapsed throughout trial.

    """
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
    
    '''
    print(f'{type(ecg_voltage)}')
    print(f'{ecg_voltage}')
    print(f'{type(fs)}')
    print(f'{fs}')
    print(f'{type(label_samples)}')
    print(f'{label_samples}')
    print(f'{type(label_symbols)}')
    print(f'{label_symbols}')
    print(f'{type(subject_id)}')
    print(f'{subject_id}')
    print(f'{type(electrode)}')
    print(f'{electrode}')
    print(f'{type(units)}')
    print(f'{units}')
    print(f'{type(ecg_time)}')
    print(f'{ecg_time}')
    '''

    return ecg_voltage,fs,label_samples,label_symbols,subject_id,electrode,units, ecg_time

# %% Part 2: Plot Raw Data
    
def plot_raw_data(signal_voltage, signal_time, units = 'V', title = ''):
    """
    Plots data for voltage without any manipulations

    Parameters
    ----------
    signal_voltage : array
        A 1D array of voltages of the signal throughout the entire trial.
    signal_time : array
        A 1D array of elapsing time during signal.
    units : string, optional
        A string representing the unit that voltage was measured in. The default is 'V'.
    title : string, optional
        A string that will be displayed as the title of the graph. The default is ''.

    Returns
    -------
    None.

    """
    plt.plot(signal_time,signal_voltage, label='Signal')
    plt.xlabel('Time (s)')
    plt.ylabel(f'Signal Voltage ({units})')
    plt.title(title)
    plt.grid()
    plt.legend()
    

# %% Part 3: Plot Events
def plot_events(label_samples, label_symbols, signal_time, signal_voltage):
    """
    Plots a point on each event of a certain symbol

    Parameters
    ----------
    label_samples : array
        A 1D array of all the time values where an event occurs.
    label_symbols : array
        A 1D array listing the symbol of each event in chronological order.
    signal_time : array
        A 1D array of elapsing time during the signal.
    signal_voltage : array
        A 1D array of full set of sampled ecg voltage data.

    Returns
    -------
    None.

    """
    symbol_list = list(np.unique(label_symbols))
    for event_type in symbol_list:
        event_sample = label_samples[label_symbols == event_type]
        plt.scatter(signal_time[event_sample],signal_voltage[event_sample], label=event_type)
        plt.legend(loc='lower right')
        

# %% Part 4: Extract Trials
    
def extract_trials(signal_voltage, trial_start_samples, trial_sample_count):
    """
    Extracts each event from a set of data and created a 2D array with rows being each event and the collumns being the voltages of these events

    Parameters
    ----------
    signal_voltage : array
        A 1D array of voltages of the signal throughout the entire trial.
    trial_start_samples : array
        A 1D array of the times each event occurs.
    trial_sample_count : array
        A 1D array of the total number of samples.

    Returns
    -------
    trials : array
        A 2D array where rows represent each individual sample and columns represent the voltages of each sample.

    """
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
    
    print(f'{type(trials)}')
    print(f'{trials}')
    return trials

# %% Part 5: Plot Trial Means

def plot_mean_and_std_trials(signal_voltage,label_samples,label_symbols,trial_duration_seconds,fs,units = 'V',title = ''):
    """
    Uses previous functions to create a plot of a mean normal signal and a mean arrhythmic signal, along with a shaded in standard deviation of each signal symbol.

    Parameters
    ----------
    signal_voltage : array
        A 1D array of voltages of the signal throughout the entire trial.
    label_samples : array
        A 1D array of all the time values where an event occurs.
    label_symbols : array
        A 1D array indicating the symbol of each event.
    trial_duration_seconds : int
        A number representing the time in seconds that each trial lasts.
    fs : array
        A 1D array of the sampling frequency in Hz.
    units : string, optional
        A string representing the unit that voltage was measured in. The default is 'V'.
    title : string, optional
        A string that will be displayed as the title of the graph. The default is ''.

    Returns
    -------
    symbols : array
        A 1D array containing a string for each symbol.
    trial_time : array
        A 1D array of time values during a trial.
    mean_trial_signal : array
        A 1D array of the mean voltages of each trial.

    """
    
    symbols = np.array(np.unique(label_symbols))
    plt.figure('Wrapper Function', clear = True)
    
    # trial_means = {}
    # trial_stds = {}
    mean_row_count = 0
    
    mean_trial_signal = np.empty((len(symbols),int(fs*(trial_duration_seconds))))
    
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
        
        # trial_means[trial_type] = trial_mean
        # trial_stds[trial_type] = trial_std
                
        trial_time = np.arange(-trial_sample_count*(1/fs)/2,trial_sample_count*(1/fs)/2,(1/fs))
        
        plt.plot(trial_time,trial_mean, label = f'{trial_type} mean', linewidth = 2,)
        plt.fill_between(trial_time, y1 = trial_mean-trial_std, y2 = trial_mean+trial_std, alpha = .4, label = f'{trial_type} mean +/- std')

        mean_trial_signal[mean_row_count] = trial_mean
        mean_row_count += 1
    
    plt.xlabel('Time (s)')
    plt.ylabel(f'Voltage ({units})')
    plt.title(title)
    plt.legend()
    plt.grid()
    
    return symbols, trial_time, mean_trial_signal
        
    
  

# %% Part 6: Save the Arrays and Plots

def save_means(symbols, trial_time, mean_trial_signal, out_filename = 'ecg_means.npz'):
    """
    Saves newly manipulated signals into npz file

    Parameters
    ----------
    symbols : array
        A 1D array containing a string for each symbol.
    trial_time : array
        A 1D array of elapsing time for the signal.
    mean_trial_signal : array
        A 1D array of voltages for mean trial's signal.
    out_filename : string, optional
        This string is used as the file name when it is saved. The default is 'ecg_means.npz'.

    Returns
    -------
    None.

    """
    np.savez(out_filename,symbols = symbols, trial_time = trial_time, mean_trial_signal = mean_trial_signal)
