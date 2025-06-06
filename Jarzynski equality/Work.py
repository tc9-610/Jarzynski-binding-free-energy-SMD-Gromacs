
import pandas as pd
import numpy as np



df = pd.read_csv('output_f1.csv', sep= '\t', header = None)
col_f = df.drop(df.columns[[1]], axis=1)
#print(col_f)

df = pd.read_csv('output_d1.csv', sep= '\t', header = None)
col_d = df.drop(df.columns[[1]], axis=1)
#print(col_d)

col_f.columns = ['Time', 'Force_1', 'Force_2']
col_f['M_force1'] = (col_f.iloc[:, 1] + col_f.iloc[:, 1].shift(1)) / 2
col_f['M_force2'] = (col_f.iloc[:, 2] + col_f.iloc[:, 2].shift(1)) / 2
#print(col_f)

col_d.columns = ['Time', 'Distance_1', 'Distance_2']
col_f['M_distance1'] = col_d['Distance_1'].diff()
col_f['M_distance2'] = col_d['Distance_2'].diff()
col_con = col_f[['M_force1', 'M_force2', 'M_distance1', 'M_distance2']].dropna()


col_con['Work1'] = col_con['M_force1'] * col_con['M_distance1']
col_con['Work2'] = col_con['M_force2'] * col_con['M_distance2']

t_work1 = col_con['Work1'].sum()
t_work2 = col_con['Work2'].sum()


data1 = {'Simulation' : ['1'], 'Work' : [t_work1]}
data2 = {'Simulation' : ['1'], 'Work' : [t_work2]}

j_rna1 = pd.DataFrame(data1)
j_rna2 = pd.DataFrame(data2)


K_b = 0.008314 # kJ/mol/K
t = 310 #K
e = 2.71828
j_rna1['WKbT'] = (-(j_rna1['Work']/(K_b*t)))
j_rna2['WKbT'] = (-(j_rna2['Work']/(K_b*t)))
print(j_rna1, j_rna2)


