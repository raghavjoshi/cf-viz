import pandas as pd

# Read in the data
data = pd.read_csv('data/data.csv',index_col = 0)

#get the cosine similarity scores from data
def get_cossim_scores(congressman_name):
	for i in data:
		if i == congressman_name:
			return data[i]

