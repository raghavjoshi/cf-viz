import pandas as pd 
from scipy.spatial.distance import cosine

#open file
data = pd.read_csv('data/sen_113_cosp.csv')

# Remove bill column temporarily and check to see if it worked
temp_data = data.drop('Unnamed: 0',1)
data.head(6)
temp_data.head(6)

#create temporary data frame without the indices

new_data = pd.DataFrame(index=temp_data.columns,columns=temp_data.columns)

for i in range(0,len(new_data.columns)):
	for j in range(0,len(new_data.columns)):
		new_data.ix[i,j] = 1-cosine(temp_data.ix[:,i],temp_data.ix[:,j])
		

new_data.to_csv('data/data.csv')