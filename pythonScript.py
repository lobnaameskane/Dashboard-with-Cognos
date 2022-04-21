import numpy as pd
import numpy as np

#ead in your dataframe
df = pd.read_csv('Rabat.csv') # file path
dfe= pd.DataFrame()
for j in range(0,40):
	for i in range(2,14):
		data={'YEAR' : [df.iloc(j , 1]],
		      'PS':[df.iloc[0,i]],
		      'TS':[df.iloc[40,i]],
		      'WS10M':[df.iloc[80,i]],
		      'WS50M':[df.iloc[120,i]],
		      'PRECTOTCORR':[df.iloc[160,i]],
		     }
		 dfa=pd.Dataframe(data)
		 dfe= dfe.append(dfa)
dfe.to_excel('Rabat.xlsx')
