import pandas as pd
 
dframe1 = pd.read_csv('Metadata.csv')
dframe2 = pd.read_csv('Test_Clubs_data.csv')
dframe3 = pd.read_csv('Test_Participants_In_Fests.csv')
dframe4 = pd.read_csv('Test_Organisers_In_Fests.csv')
df1=pd.merge(dframe1,dframe2,  right_on="Name",left_on="Name",how="left")

df2=pd.merge(df1,dframe3,  right_on="Name",left_on="Name",how="left")

df3=pd.merge(df2,dframe4,  right_on="Name",left_on="Name",how="left").to_csv('Main.csv')
