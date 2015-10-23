import pandas as pd

# Read in the data
data = pd.read_csv('data/data.csv',index_col = 0)

#get the cosine similarity scores from data
def get_cossim_scores(congressman_name):
	for i in data:
		if i == congressman_name:
			return data[i]

# create nodes and edges data frame

def ndf(congressman_name):
	u_cols = ['id','name']
	df = pd.DataFrame(columns=u_cols,index=data.index)
	df['id'] = [data.index.get_loc(i) for i in data.index]
	df['name'] = data.index
	return df







