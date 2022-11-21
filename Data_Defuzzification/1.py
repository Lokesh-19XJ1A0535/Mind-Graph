import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dframe2 = pd.read_csv('Metadata.csv')
dframe1 = pd.read_csv('Clubs_data.csv')
# dframe1 = pd.read_csv('Organisers_In_Fests.csv')
# dframe1 = pd.read_csv('Participants_In_Fests.csv')

mat1 = []
mat2 = []
p = []

list1 = dframe1['Name'].tolist()
list2 = dframe2['Name'].tolist()


threshold = 50

for i in list1:
	mat1.append(process.extractOne(
	i, list2, scorer=fuzz.token_set_ratio))
dframe1['RealName'] = mat1

for j in dframe1['RealName']:
	if j[1] >= threshold:
		p.append(j[0])
	mat2.append(",".join(p))
	p = []


dframe1['RealName'] = mat2
print("\nDataFrame after Fuzzy matching using token_set_ratio():")
dframe1
dframe1 = dframe1.replace(r'^s*$', float('NaN'), regex = True) 
dframe1.dropna(inplace = True)  

dframe1.to_csv('Test_Clubs_data.csv.csv')
# dframe1.to_csv('Test_Participants_In_Fests.csv.csv')
# dframe1.to_csv('Test_Organisers_In_Fests.csv')
