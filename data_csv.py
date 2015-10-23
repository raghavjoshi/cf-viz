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

def edf(congressman_name):
	u_cols = ['source','target','value']
	df = pd.DataFrame(columns=u_cols,index=data.index)
	df['source'] = data.index.get_loc(congressman_name)
	df['target'] = [data.index.get_loc(i) for i in data.index]
	df['value'] = [j for j in get_cossim_scores(congressman_name)]
	return df


def csv():
	for i in data.index:
		temp = ndf(i)
		temp2 = edf(i)
		temp.to_csv('data/csv_data/' + i + '_node.csv')
		temp2.to_csv('data/csv_data/' + i + '_edge.csv')

csv()





