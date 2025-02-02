
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 15:49:24 2022

@author: EED
"""


#%%
import pandas as pd
import re
import numpy as np
import os

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(_nsre, s)]

time_vec = 80
para = 6

# Define the directory containing the files
ABCG_dir = 'E:\received_data.xlsx'

# Get the list of all files in the directory
ABCG_data = os.listdir(ABCG_dir)

# Sort the files naturally
ABCG_data.sort(key=natural_sort_key)

# Function to process the files based on their filename endings
def x_data1():
    x_data = np.ndarray((len(ABCG_data), time_vec, para), dtype=np.float32)
   
    for i, name in enumerate(ABCG_data):
        print(i, name)
        signal = pd.read_excel(ABCG_dir + name, "Sheet1")
        signal = np.array(signal, dtype='float32')

        if name.endswith('0.05.xlsx'):
            x_data[i] = signal[240:320, :]
        elif name.endswith('0.05139.xlsx'):
            x_data[i] = signal[246:326, :]
        elif name.endswith('0.0527.xlsx'):
            x_data[i] = signal[253:333, :]
        elif name.endswith('0.054.xlsx'):
            x_data[i] = signal[259:339, :]
        elif name.endswith('0.0554.xlsx'):
            x_data[i] = signal[266:346, :]
        elif name.endswith('0.0568.xlsx'):
            x_data[i] = signal[272:352, :]
        elif name.endswith('0.0589.xlsx'):
            x_data[i] = signal[282:362, :]
        elif name.endswith('0.06.xlsx'):
            x_data[i] = signal[288:368, :]
        elif name.endswith('0.06139.xlsx'):
            x_data[i] = signal[294:374, :]
        elif name.endswith('0.0627.xlsx'):
            x_data[i] = signal[301:381, :]
        elif name.endswith('0.064.xlsx'):
            x_data[i] = signal[307:387, :]
        elif name.endswith('0.0654.xlsx'):
            x_data[i] = signal[314:394, :]
        else:
            print(f"Filename pattern not recognized for {name}")
   
    return x_data, signal

# Call the function to process the files
x_1, signal = x_data1()

# Assign the processed data to a variable
x_ABCG = x_1  

# Save the processed data as a .npy file
np.save('x_AB.npy', x_ABCG)
#%%



#%%

import pandas as pd
import re
import numpy as np
import glob
import os

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]  
    
time_vec = 80
para = 6

#%%%
ABCG_dir='E:\\MATLAB Microgrid\\Clubbed_Data\\CG\\'
ABCG_data = os.listdir(ABCG_dir)
ABCG_data.sort(key=natural_sort_key)



def x_data1():
    x_data = np.ndarray((len(ABCG_data),time_vec,para), dtype=np.float32)
    for i, name in enumerate(ABCG_data ):
        print(i,name)
        signal = pd.read_excel(ABCG_dir + name, "Sheet1")
        
        signal =np.array(signal ,'float32')
        
        x_data[i] = signal[240:240+80,:]
        
         
    return x_data,signal


# def x_data2():
#     x_data = np.ndarray((len(ABCG_data),time_vec,para), dtype=np.float32)
#     for i, name in enumerate(ABCG_data ):
#         print(i,name)
#         signal = pd.read_excel(ABCG_dir + name, "Sheet2")
        
#         signal =np.array(signal ,'float32')
        
#         x_data[i] = signal[103:103+34,:]
        
         
#     return x_data,signal


x_1,signal = x_data1()
#x_2,signal = x_data2()
x_ABCG = x_1  
np.save('x_CG.npy',x_ABCG)


#%%
#x_ABCG = x_ABCG[:,:,1:7]
#x1 = x[0:230160,:,:]
import numpy as np
x_AG = np.load('x_AG.npy')
x_BG = np.load('x_BG.npy')
x_CG = np.load('x_CG.npy')
x_AB = np.load('x_AB.npy')
x_BC = np.load('x_BC.npy')
x_AC = np.load('x_AC.npy')
x_ABG = np.load('x_ABG.npy')
x_BCG = np.load('x_BCG.npy')
x_ACG = np.load('x_ACG.npy')
x_ABC = np.load('x_ABC.npy')

#x_14 = np.load('x_14.npy')
#x_15 = np.load('x_15.npy')
#x_97 = np.load('x_97.npy')
#x_97 = np.load('x_97.npy')

x_data = np.vstack((x_AG,x_BG,x_CG,x_AB,x_BC,x_AC,x_ABG,x_BCG,x_ACG,x_ABC))
np.save('x_data.npy',x_data)
#%%
import numpy as np
y_AG = 0*np.ones(2520)
y_BG = 1*np.ones(2520)
y_CG = 2*np.ones(2520)
y_AB = 3*np.ones(2520)
y_BC = 4*np.ones(2520)
y_AC = 5*np.ones(2520)
y_ABG = 6*np.ones(2520)
y_BCG = 7*np.ones(2520)
y_ACG = 8*np.ones(2520)
y_ABC = 9*np.ones(2520)
#y_14 = 14*np.ones(840)
#y_15 = 15*np.ones(840)
#y_97 = 97*np.ones(840)
#y_97 = 97*np.ones(840)

y_data = np.hstack((y_AG,y_BG,y_CG,y_AB,y_BC,y_AC,y_ABG,y_BCG,y_ACG,y_ABC))
np.save('y_data.npy',y_data)
#%%
# x_new = np.vstack((x,x_ABCG))



# np.save('x_data12.npy',x_new)


#%%


x = np.load('x_data10.npy')
y = np.load('y_data10.npy')


#%%
import numpy as np
b = np.arange(1,98,6)
y_AG = np.zeros(17)
y_BG = 1*np.ones(17)
y_CG = 2*np.ones(17)
y_AB = 3*np.ones(17)
y_BC = 4*np.ones(17)
y_AC = 5*np.ones(17)
y_ABG = 6*np.ones(17)
y_BCG = 7*np.ones(17)
y_ACG = 8*np.ones(17)
y_ABC = 9*np.ones(17)

y_regAG = np.zeros(17)
y_regBG = np.zeros(17)
y_regCG = np.zeros(17)
y_regAB = np.zeros(17)
y_regBC = np.zeros(17)
y_regAC = np.zeros(17)
y_regABG = np.zeros(17)
y_regBCG = np.zeros(17)
y_regACG = np.zeros(17)
y_regABC = np.zeros(17)

for i in range(0,17):
    y_regAG[i] = y_AG[i] + b[i]*0.01
    y_regBG[i] = y_BG[i] + b[i]*0.01
    y_regCG[i] = y_CG[i] + b[i]*0.01
    y_regAB[i] = y_AB[i] + b[i]*0.01
    y_regBC[i] = y_BC[i] + b[i]*0.01
    y_regAC[i] = y_AC[i] + b[i]*0.01
    y_regABG[i] = y_ABG[i] + b[i]*0.01
    y_regBCG[i] = y_BCG[i] + b[i]*0.01
    y_regACG[i] = y_ACG[i] + b[i]*0.01
    y_regABC[i] = y_ABC[i] + b[i]*0.01
    
    
y_regAG =np.repeat(y_regAG, 12)
y_regBG =np.repeat(y_regBG, 12)
y_regCG =np.repeat(y_regCG, 12)
y_regAB =np.repeat(y_regAB, 12)
y_regBC =np.repeat(y_regBC, 12)
y_regAC =np.repeat(y_regAC, 12)
y_regABG =np.repeat(y_regABG, 12)
y_regBCG =np.repeat(y_regBCG, 12)
y_regACG =np.repeat(y_regACG, 12)
y_regABC =np.repeat(y_regABC, 12)

y_regAG = np.hstack((y_regAG,y_regAG,y_regAG,y_regAG,y_regAG,y_regAG,y_regAG))
y_regBG = np.hstack((y_regBG,y_regBG,y_regBG,y_regBG,y_regBG,y_regBG,y_regBG))
y_regCG = np.hstack((y_regCG,y_regCG,y_regCG,y_regCG,y_regCG,y_regCG,y_regCG))
y_regAB = np.hstack((y_regAB,y_regAB,y_regAB,y_regAB,y_regAB,y_regAB,y_regAB))
y_regBC = np.hstack((y_regBC,y_regBC,y_regBC,y_regBC,y_regBC,y_regBC,y_regBC))
y_regAC = np.hstack((y_regAC,y_regAC,y_regAC,y_regAC,y_regAC,y_regAC,y_regAC))
y_regABG = np.hstack((y_regABG,y_regABG,y_regABG,y_regABG,y_regABG,y_regABG,y_regABG))
y_regBCG = np.hstack((y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG))
y_regACG = np.hstack((y_regACG,y_regACG,y_regACG,y_regACG,y_regACG,y_regACG,y_regACG))
y_regABC = np.hstack((y_regABC,y_regABC,y_regABC,y_regABC,y_regABC,y_regABC,y_regABC))

y_regdata = np.hstack((y_regAG,y_regBG,y_regCG,y_regAB,y_regBC,y_regAC,y_regABG,y_regBCG,y_regACG,y_regABC))
np.save('y_regdata.npy',y_regdata)


#%%
(unique, counts) = np.unique(y_data,return_counts=True)

#%%


y_classdata = [int(i) for i in y_regdata]
(unique, counts) = np.unique(y_classdata,return_counts=True)



#%%


import numpy as np
b = np.arange(1,98,6)


y_regAG = np.zeros(17)
y_regBG = np.zeros(17)
y_regCG = np.zeros(17)
y_regAB = np.zeros(17)
y_regBC = np.zeros(17)
y_regAC = np.zeros(17)
y_regABG = np.zeros(17)
y_regBCG = np.zeros(17)
y_regACG = np.zeros(17)
y_regABC = np.zeros(17)

for i in range(0,17):
    y_regAG[i] =  b[i]
    y_regBG[i] =  b[i]
    y_regCG[i] = b[i]
    y_regAB[i] = b[i]
    y_regBC[i] =  b[i]
    y_regAC[i] =  b[i]
    y_regABG[i] =  b[i]
    y_regBCG[i] = b[i]
    y_regACG[i] =  b[i]
    y_regABC[i] =  b[i]
    
    
y_regAG =np.repeat(y_regAG, 12)
y_regBG =np.repeat(y_regBG, 12)
y_regCG =np.repeat(y_regCG, 12)
y_regAB =np.repeat(y_regAB, 12)
y_regBC =np.repeat(y_regBC, 12)
y_regAC =np.repeat(y_regAC, 12)
y_regABG =np.repeat(y_regABG, 12)
y_regBCG =np.repeat(y_regBCG, 12)
y_regACG =np.repeat(y_regACG, 12)
y_regABC =np.repeat(y_regABC, 12)

y_regAG = np.hstack((y_regAG,y_regAG,y_regAG,y_regAG,y_regAG,y_regAG,y_regAG))
y_regBG = np.hstack((y_regBG,y_regBG,y_regBG,y_regBG,y_regBG,y_regBG,y_regBG))
y_regCG = np.hstack((y_regCG,y_regCG,y_regCG,y_regCG,y_regCG,y_regCG,y_regCG))
y_regAB = np.hstack((y_regAB,y_regAB,y_regAB,y_regAB,y_regAB,y_regAB,y_regAB))
y_regBC = np.hstack((y_regBC,y_regBC,y_regBC,y_regBC,y_regBC,y_regBC,y_regBC))
y_regAC = np.hstack((y_regAC,y_regAC,y_regAC,y_regAC,y_regAC,y_regAC,y_regAC))
y_regABG = np.hstack((y_regABG,y_regABG,y_regABG,y_regABG,y_regABG,y_regABG,y_regABG))
y_regBCG = np.hstack((y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG,y_regBCG))
y_regACG = np.hstack((y_regACG,y_regACG,y_regACG,y_regACG,y_regACG,y_regACG,y_regACG))
y_regABC = np.hstack((y_regABC,y_regABC,y_regABC,y_regABC,y_regABC,y_regABC,y_regABC))

y_locdata = np.hstack((y_regAG,y_regBG,y_regCG,y_regAB,y_regBC,y_regAC,y_regABG,y_regBCG,y_regACG,y_regABC))
np.save('y_locdata.npy',y_locdata)

(unique, counts) = np.unique(y_locdata,return_counts=True)
#%%
