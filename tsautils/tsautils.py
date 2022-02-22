#!/usr/bin/env python
# coding: utf-8
# Disclaimer
# This Library can't be used without the permission of the first developer and proper credits.
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import traceback
import pandas as pd


def create_dir(PATH): # function to create output directories
    if os.path.exists(PATH):
        print(PATH + 'is present!!')
    else:
        print(PATH + 'is not found, creating')
        os.makedirs(PATH)

def file_grab(LOCATION, type = 'csv'):
    file_list = []
    for root, _, files in os.walk(LOCATION): #collecting all csv files in input dir
        for file in files:
            if file.endswith('.csv'):
                path = os.path.join(root, file)
                file_list.append(path)
    return file_list

def output_f(df, last_value): # function to determine the user's final choice/output
    arr = []
    for i in range(1,len(df)):
        if df.GazeOnElementId.iloc[-i] == last_value:
            arr.append(last_value)
        else:
            break
    return arr

def Conversion(var = 'Auto'): #Conversion Function for labeling the plots
    if var == 'Auto':
        values = ['No_Line_of_Sight','Co01', 'Co02','Co03','Co04','Co05','Co06']
        conversion = {}
        for value, i in zip(values,range(0,len(values))):
            conversion[value] = i
        return conversion
    else:
        values = [var +'_Co0', var +'_Co1',
                var +'_Co2', var +'_Co3', var +'_Co4', var +'_Co5', var +'_Co6']
        conversion = {}
        for value, i in zip(values, range(0, len(values))):
            conversion[value] = i
        return conversion
def last_value_grab(df):
    last = df.GazeOnElementId.iloc[-1]
    kk = 0
    for i in range(len(df)):
        if df.GazeOnElementId.iloc[-1-i]==last:
            last = last
            
        else:
            last = df.GazeOnElementId.iloc[-1-i]
            kk = i
            break
    return kk

def MatplotlibClearMemory(): # Clear Matplotlib to prevent memory issues
    allfignums = plt.get_fignums()
    for i in allfignums:
        fig = plt.figure(i)
        fig.clear()
        plt.close(fig)
        plt.cla()
        plt.clf()

def plot_f(df,arr, name, OUT_FIG_DIR): # Function to plot the data
    perc = len(df) + len(arr)
    fig, ax = plt.subplots(figsize=(30, 12))
    title_format = {'fontsize': 17, 'fontweight': 'bold'}
    label_format = {'fontsize': 13, 'fontweight': 'bold'}
    conversion = Conversion()
    ax.yaxis.grid()
    plt.plot(np.arange(0, len(df)), df, color="b",label="Input")
    plt.plot(np.arange(len(df), perc), arr, color="r", marker = 'x',label="Choice")
    xs = np.linspace(1, 21, 6)
    plt.vlines(x=len(df), ymin=0, ymax=len(xs), colors='g',ls=':', lw=2, label='Separating line')
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=perc))
    plt.xticks((np.arange(0,perc,step =100)),rotation=45)
    ax.set_title(f"Prediction Graph of {name[-31:-15]}", **title_format)
    ax.set_yticks(list(conversion.values()))
    ax.set_yticklabels(list(conversion.keys()), **label_format)
    ax.set_xlabel('percentage of time', **label_format)
    ax.set_ylabel('color of choice', **label_format)
    ax.xaxis.set_ticks(np.linspace(0, perc, 6), **label_format)
    plt.legend()
    plt.savefig(OUT_FIG_DIR + "plot_of_" + name[-31:-15]+".jpg")
    MatplotlibClearMemory()

def plot_step2(df,df1,df2,conversion_X,conversion_Y, name, kk, STEP_2_FIG_DIR):
    fig, ax = plt.subplots(2, figsize = (12,6) )
    label_format = {'fontsize': 12, 'fontweight': 'bold'}
    title_format = {'fontsize': 16, 'fontweight': 'bold'}
    #ax[0].plot(np.arange(0, len(df)), df1, color="blue",label="Input")
    ax[0].plot(np.arange(0, len(df)-kk), df1[0:-kk], color="red",label="Input")
    ax[0].plot(np.arange(len(df)-kk, len(df)), df1[-kk:], color="blue",label="Input")
    #ax[1].plot(np.arange(0, len(df)), df2, color="Blue",label="Choice")
    ax[1].plot(np.arange(0, len(df)-kk), df2[0:-kk], color="blue",label="Output")
    ax[1].plot(np.arange(len(df)-kk, len(df)), df2[-kk:], color="green",label="Output")
    ax[0].yaxis.grid()  # horizontal lines
    ax[1].yaxis.grid()
    xs = np.linspace(0, 6, 6)
    ax[0].vlines(x=len(df)-kk, ymin=0, ymax=len(xs), colors='black', ls='dotted', label='separating line')
    ax[1].vlines(x=len(df)-kk, ymin=0, ymax=len(xs), colors='black', ls='dotted', label='separating line')
    ax[0].set_xlabel('percantage of time')
    ax[1].set_xlabel('percentage of time')
    ax[0].set_ylabel('Colors')
    ax[1].set_ylabel('Colors')
    #ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=total_count))
    ax[0].xaxis.set_major_formatter(mtick.PercentFormatter(xmax = len(df), decimals=False,symbol='%', is_latex=True))
    ax[1].xaxis.set_major_formatter(mtick.PercentFormatter(xmax = len(df), decimals=False,symbol='%', is_latex=True))
    ax[0].set_yticks(list(conversion_X.values()))
    ax[0].set_title("Input Data", **label_format)
    ax[0].set_yticklabels(list(conversion_X.keys()))
    ax[0].xaxis.set_ticks(np.linspace(0, len(df), 6))
    ax[1].set_yticks(list(conversion_Y.values()))
    ax[1].set_yticklabels(list(conversion_Y.keys()))
    ax[1].xaxis.set_ticks(np.linspace(0, len(df), 6))
    ax[1].set_title("Output Data", **label_format)
    plt.suptitle("Output_Input_Comparism_Plot_of_" + name[-31:-15] , **title_format)
    fig.tight_layout()
    plt.savefig(STEP_2_FIG_DIR + "Output_Input_Comparism_Plot_of_" + name[-31:-15] + ".jpg")
    plt.close()
    plt.cla()
    plt.clf()
    MatplotlibClearMemory()

def step2(df,df1,df2, name, kk, dir):
    try:
        row_dict = {'GazeOnElementId': [0]}
        z_data = pd.DataFrame (row_dict)
        while len(df1) < len(df):
            df1 = df1.append(z_data, ignore_index = True)
        while len(df2) < len(df):
            df2 = pd.concat([z_data, df2], ignore_index = True)
        conversion_X = Conversion('X')
        conversion_Y = Conversion('Y')
        plot_step2(df,df1,df2,conversion_X,conversion_Y, name, kk, dir)
    except:
        traceback.print_exc()





