import pandas as pd 
import scipy.spatial.distance import cosine

#open file
data = pd.read_csv('data/sen_113_cosp.csv')

# Remove bill column temporarily and check to see if it worked
temp_data = data.drop('Unnamed: 0',1)
data.head(6)
temp_data.head(6)