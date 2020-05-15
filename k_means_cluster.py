#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import sys
import os


# In[ ]:


"""
Mean DF --> [K]x[Cols] --> Mean[i][j] = mean of ith cluster and jth feature 
Mean[i] --> mean_vector of ith cluster
Siddharth Vadgama
1001397508
"""
def recalculate_mean(clusters,training_df):
    mean_df=pd.DataFrame(0.0,columns=[i for i in range(1,cols)],index=[i for i in range(1,k+1)])
    for i in range(1,k+1):
        for j in range(1,cols):
            mean_df.loc[i][j]=float(sum(training_df.iloc[clusters[i]][j]))/float(len(training_df.iloc[clusters[i]][j]))
    return mean_df

def dist_E(mean, obj):
    dist=[]
    for i in range(1,k+1):
        dist.append(np.linalg.norm(np.subtract(list(mean.loc[i]), obj), ord = 2))
    return dist

training_file_path=sys.argv[1]
training_file=os.path.basename(training_file_path)
ins = open(training_file, "r" )
data = [[float(n) for n in line.split()] for line in ins]
rows,cols=np.shape(data)
col_vec=[i for i in range(1,cols+1)]
training_dataframe=pd.DataFrame(data,columns=col_vec)
test_df=training_dataframe
training_df=training_dataframe.drop([cols],axis=1)

#initial assignment of objects in K clusters
iterations=int(sys.argv[3])
k=int(sys.argv[2])
clusters={}
for i in range(1,k+1):
    clusters[i]=[]
for i in range(rows):
    clusters[np.random.randint(1, k+1)].append(i)
mean_df=recalculate_mean(clusters,training_df)
"""
Main Loop
"""
for it in range(iterations):
    total_distance=0.0
    for i in range(1,k+1):
        clusters[i]=[]
    for x in range(rows):
        #distance= list = distance of obj to each clusters
        distance=dist_E(mean_df,list(training_df.loc[x]))
        total_distance+=distance[np.argmin(distance)]
        clusters[np.argmin(distance)+1].append(x)
    if it == 0:
        print('After initialization: error = %.4f' % (total_distance))
    else:
        print('After iteration %d: error = %.4f' % (it, total_distance))
    #recalc mean
    mean_df=recalculate_mean(clusters,training_df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




