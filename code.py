import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

os.chdir("c:\dataset")

#creating a data-frame of csv file
data=pd.read_csv("Toyota.csv",index_col=0,na_values=['?','??','???','????'])

print(data.isnull().sum())

#removes missing values
data.dropna(axis=0,inplace=True)

'''data['KM']=pd.to_numeric(data['KM'], errors='coerce')
data['Price']=pd.to_numeric(data['Price'], errors='coerce')
data['Age']=pd.to_numeric(data['Age'], errors='coerce')
data['HP']=pd.to_numeric(data['HP'], errors='coerce')
data['CC']=pd.to_numeric(data['CC'], errors='coerce')
data['Automatic']=pd.to_numeric(data['Automatic'],errors='coerce')
data['MetColor']=pd.to_numeric(data['MetColor'],errors='coerce')

meanKM=data['KM'].median()
meanPrice=data['Price'].median()
meanAge=data['Age'].median()
meanHP=data['HP'].median()
meanCC=data['CC'].median()
meanMetColor=data['MetColor'].median()

# Replace NaNs in column S2 with the
# mean of values in the same column
data['KM'].fillna(value=meanKM, inplace=True)
data['Price'].fillna(value=meanPrice, inplace=True)
data['Age'].fillna(value=meanAge, inplace=True)
data['HP'].fillna(value=meanHP, inplace=True)
data['CC'].fillna(value=meanCC, inplace=True)
data['FuelType'].fillna(value='CNG', inplace=True)
data['MetColor'].fillna(value=meanMetColor, inplace=True)'''

print(data.isnull().sum())
#Verbal Analysis 
print(data.head(20))

#Statistical data analysis
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)
print(data.describe(include='all'))
print()

#Frequency tables
#print(pd.crosstab(columns='count'index=data['FuelType']))
print()
print(pd.crosstab(index=data['Automatic'],columns='count'))
print()
print(pd.crosstab(index=data['MetColor'],columns='count'))
print()
print(pd.crosstab(index=data['Doors'],columns='count'))
print()

#Two-way Tables
print(pd.crosstab(index=data['FuelType'],columns='Automatic'))
print()
print(pd.crosstab(index=data['FuelType'],columns='MetColor'))
print()
print(pd.crosstab(index=data['MetColor'],columns='Automatic'))
print()



#Non-Verbal Analysis

#Scatter plots
sns.set(style="darkgrid")
sns.regplot(x=data['Age'],y=data['Price'],fit_reg=False)
plt.title('SCATTER PLOT PRICE VS AGE')
plt.show()

sns.lmplot(x='Age',y='Price',data=data,fit_reg=False,hue='FuelType',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS AGE WITH HUE AS FUELTYPE')
plt.show()

sns.lmplot(x='KM',y='Price',data=data,fit_reg=False,hue='FuelType',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS KM WITH HUE AS FUELTYPE')
plt.show()

sns.lmplot(x='Weight',y='Price',data=data,fit_reg=False,hue='FuelType',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS WEIGHT WITH HUE AS FUELTYPE')
plt.show()

sns.lmplot(x='KM',y='Price',data=data,fit_reg=False,hue='Automatic',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS KM WITH HUE AS AUTOMATIC')
plt.show()

sns.lmplot(x='KM',y='Price',data=data,fit_reg=False,hue='MetColor',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS KM WITH HUE AS MET-COLOR')
plt.show()

sns.lmplot(x='HP',y='Price',data=data,fit_reg=False,hue='FuelType',legend=True,palette='Set1')
plt.title('SCATTER PLOT PRICE VS KM WITH HUE AS FUELTYPE')
plt.show()


#Histograms for frequency distribution 
sns.distplot(data['Price'],kde=False,bins=10)
plt.title('HISTOGRAM FOR PRICE DISTRIBUTION')
plt.show()

sns.distplot(data['Age'],kde=False,bins=10)
plt.title('HISTOGRAM FOR AGE DISTRIBUTION')
plt.show()

sns.distplot(data['KM'],kde=False,bins=10)
plt.title('HISTOGRAM FOR KM DISTRIBUTION')
plt.show()

sns.distplot(data['HP'],kde=False,bins=10)
plt.title('HISTOGRAM FOR HP DISTRIBUTION')
plt.show()

sns.distplot(data['CC'],kde=False,bins=10)
plt.title('HISTOGRAM FOR CC DISTRIBUTION')
plt.show()

sns.distplot(data['Weight'],kde=False,bins=10)
plt.title('HISTOGRAM FOR WEIGHT DISTRIBUTION')
plt.show()


#Bar Plots
sns.countplot(x='FuelType',data=data)
plt.title('BAR-PLOT FOR FUEL-TYPE DISTRIBUTION')
plt.show()

sns.countplot(x='MetColor',data=data)
plt.title('BAR-PLOT FOR METCOLOR DISTRIBUTION')
plt.show()

sns.countplot(x='Automatic',data=data)
plt.title('BAR-PLOT FOR AUTOMATIC DISTRIBUTION')
plt.show()

sns.countplot(x='FuelType',data=data,hue='Automatic')
plt.title('GROUPED BAR-PLOT FOR FUELTYPE & AUTOMATIC DISTRIBUTION')
plt.show()

sns.countplot(x='FuelType',data=data,hue='MetColor')
plt.title('GROUPED BAR-PLOT FOR FUELTYPE & METCOLOR DISTRIBUTION')
plt.show()

df=data
df.head(20)

#df['KM']=int(df['KM'])
#df['DataFrame Column'] = pd.to_numeric(df['DataFrame Column'], errors='coerce')
'''df['KM']=pd.to_numeric(df['KM'], errors='coerce')
df['Price']=pd.to_numeric(df['Price'], errors='coerce')
df['Age']=pd.to_numeric(df['Age'], errors='coerce')
df['HP']=pd.to_numeric(df['HP'], errors='coerce')
df['CC']=pd.to_numeric(df['CC'], errors='coerce')
df['Automatic']=pd.to_numeric(df['Automatic'],errors='coerce')
meanKM=df['KM'].mean()
meanPrice=df['Price'].mean()
meanAge=df['Age'].mean()
meanHP=df['HP'].mean()
meanCC=df['CC'].mean()
  
# Replace NaNs in column S2 with the
# mean of values in the same column
df['KM'].fillna(value=meanKM, inplace=True)
df['Price'].fillna(value=meanPrice, inplace=True)
df['Age'].fillna(value=meanAge, inplace=True)
df['HP'].fillna(value=meanHP, inplace=True)
df['CC'].fillna(value=meanCC, inplace=True)

df[['KM','HP','CC','Age']].head(20)'''

X = df[['KM','HP','CC','Age']]
y = df['Price']
L=X

from sklearn.preprocessing import StandardScaler

#fit = -1 to 1
S=StandardScaler().fit(X)
#tranform performs operation on the dataset
X=S.transform(X)

from sklearn.decomposition import PCA
pca = PCA()
X_reduced = pca.fit_transform(X)

#y=StandardScaler().fit_transform(y.reshape(-1,1))

#np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
#print(X)
#t=[[46900.0,90.0,2000.0,23.0],[900.0,90.0,2000.0,23.0]]
#t=S.transform(t)
X_reduced
#print(X_reduced)
#print(pca.transform(t))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_reduced[:,0:3], y, test_size=0.33, random_state=42)

from sklearn import linear_model

regression=linear_model.LinearRegression()
regression.fit(X_train,y_train)

print("Test Accuracy:",regression.score(X_test, y_test))

#plt.scatter(X_train[:,0], y_train, color = "red")
plt.scatter(X_test[:,0],y_test, color = "green")
plt.scatter(X_test[:,0],regression.predict(X_test),color="red")
plt.title("COST VS COMPONENT 1")
plt.xlabel("COMPONENT 1")
plt.ylabel("PRICE")
plt.show()

plt.scatter(X_test[:,1],y_test, color = "green")
plt.scatter(X_test[:,1],regression.predict(X_test),color="red")
plt.title("COST VS COMPONENT 2")
plt.xlabel("COMPONENT 2")
plt.ylabel("PRICE")
plt.show()

plt.scatter(X_test[:,2],y_test, color = "green")
plt.scatter(X_test[:,2],regression.predict(X_test),color="red")
plt.title("COST VS COMPONENT 3")
plt.xlabel("COMPONENT 3")
plt.ylabel("PRICE")
plt.show()

#plt.scatter(X_test[:,2],y_test, color = "green")
'''plt.scatter(df['Age'],df['Price'],color="red")
plt.title("COST VS COMPONENT 3")
plt.xlabel("COMPONENT 3")
plt.ylabel("PRICE")
plt.show()'''

"""#PLOTTING THE CLUSTERS WITH PRINCIPLE COMPONENTS

colors=['blue','red','green']
plt.xlabel("Component 1")
plt.ylabel("Component 2")
plt.title('Cluster visualisation using PCA', fontsize = 20)

for x in range(0,len(df_final['cluster'])):
  plt.scatter(df_final['1'][x],df_final['2'][x],c=colors[df_final['cluster'][x]])
"""

t=[[46900.000000,90.000000,2000.000000,23.000000],[900.000000,90.000000,2000.000000,23.000000]] #Enter the data to be predicted
tdf = pd.DataFrame(t, columns=['KM', 'HP','CC','Age'])
print(type(tdf))

# to scale from -1 to 1 (STANDARD)
tdf=S.transform(tdf)

#after PCA stored in tdf_reduced
# regression is var name
tdf_reduced=pca.transform(tdf)
print(tdf_reduced)
print(regression.predict(tdf_reduced[:,0:3]))
