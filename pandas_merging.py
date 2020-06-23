import numpy as np
import pandas as pd

#merging two df by key/keys.(may be used in database)
#simple example

left = pd.DataFrame ({'key':['K0','K1','K2','K3'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3']})

right = pd.DataFrame ({'key':['K0','K1','K2','K3'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})

##print(left)
##print(right)

res = pd.merge(left,right, on='key')
print(res)


#consider two keys
left1 = pd.DataFrame ({'key1':['K0','K0','K1','K2'],
                       'key2':['K0','K1','K0','K1'],
                      'A':['A0','A1','A2','A3'],
                      'B':['B0','B1','B2','B3']})

right1 = pd.DataFrame ({'key1':['K0','K1','K1','K2'],
                        'key2':['K0','K0','K0','K0'],
                      'C':['C0','C1','C2','C3'],
                      'D':['D0','D1','D2','D3']})
print(left1)
print(right1)
res1 = pd.merge (left1,right1, on = ['key1','key2'],how = 'inner')
print(res1)

#how = ['left','right','outer','inner']
