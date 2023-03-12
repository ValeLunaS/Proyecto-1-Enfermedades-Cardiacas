import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
datos = pd.read_csv("C:/Users/User/Documents/Septimo Semestre/ACTO/Proyecto/processed.cleveland.data")
datos.head()

print(datos.corr())

datos1 = datos
for i in range (0,len(datos1)):
    if datos1["Ca"][i]=="?":
        datos1.drop(i,axis=0,inplace=True)
    elif datos1["Thal"][i]=="?":
        datos1.drop(i,axis=0,inplace=True)
 
print(datos1.dtypes)
datos1[["Ca","Thal"]]=datos1[["Ca","Thal"]].apply(pd.to_numeric)


# Diagrama de regresion
x = [datos1["Num"]]
y = [datos1["Thalach"]]

x = np.array(x).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

x_reg = np.linspace(min(x), max(x), 100).reshape(-1, 1)
y_reg = model.predict(x_reg)

plt.scatter(x, y,color='#92C5FC')
plt.plot(x_reg, y_reg, color='red')

plt.xlabel('Num')
plt.ylabel('Thalach')
plt.title('Regresión lineal Num vs Thalach')

plt.show()

#Grafica de Barras
x = datos1["Num"]
y = datos1["Oldpeak"]

# Crear un gráfico de barras
fig, ax=plt.subplots()
ax.bar(x, y,color='#92C5FC')

# Agregar etiquetas de eje y título
ax.set_xlabel('Num')
ax.set_ylabel('Oldpeak')
ax.set_title('Diagrama de barras Num vs Oldpeak')
ax.set_xticks(x)

# Mostrar el gráfico
plt.show()


scores=["Age","Trestbps", "Chol","Thalach","Oldpeak"]
for i in scores:
    fig = plt.figure()
    x=datos1[i]
    #plt.hist(x,color='#53B8B4')
    plt.hist(x,color='#3CB043')
    plt.title(i + " (Discreta)", fontsize = 18)
    #grafica=x.plot(kind="hist",bins=30,color='#53B8B4')
    #grafica.set_title(i)
    
plt.show()


datos1=datos

#Cambiar los valores de NUM

for i in range (0,302):
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Num"][i]!=0: 
            datos1["Num"][i]=1



#Variables Categoricas

for i in range (0,302):
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Age"][i]>=29 and datos1["Age"][i]<40:
            datos1["Age"][i]=1
        elif datos1["Age"][i]>=40 and datos1["Age"][i]<55:
            datos1["Age"][i]=2
        elif datos1["Age"][i]>=55 and datos1["Age"][i]<65:
            datos1["Age"][i]=3
        elif datos1["Age"][i]>=65 and datos1["Age"][i]<80:
            datos1["Age"][i]=4

   
    
for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287: 
        if datos1["Trestbps"][i]>=94 and datos1["Trestbps"][i]<120:
            datos1["Trestbps"][i]=1
        elif datos1["Trestbps"][i]>=120 and datos1["Trestbps"][i]<130:
            datos1["Trestbps"][i]=2
        elif datos1["Trestbps"][i]>=130 and datos1["Trestbps"][i]<140:
            datos1["Trestbps"][i]=3
        elif datos1["Trestbps"][i]>=140 and datos1["Trestbps"][i]<181:
            datos1["Trestbps"][i]=4
        elif datos1["Trestbps"][i]>=181 and datos1["Trestbps"][i]<=210:
            datos1["Trestbps"][i]=5


for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:     
        if datos1["Chol"][i]>=126 and datos1["Chol"][i]<200:
            datos1["Chol"][i]=1
        elif datos1["Chol"][i]>=200 and datos1["Chol"][i]<301:
            datos1["Chol"][i]=2
        elif datos1["Chol"][i]>=301 and datos1["Chol"][i]<570:
            datos1["Chol"][i]=3

for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:      
        if datos1["Thalach"][i]>=71 and datos1["Thalach"][i]<140:
            datos1["Thalach"][i]=1
        elif datos1["Thalach"][i]>=140 and datos1["Thalach"][i]<170:
            datos1["Thalach"][i]=2
        elif datos1["Thalach"][i]>=170 and datos1["Thalach"][i]<=210:
            datos1["Thalach"][i]=3


for i in range (0,302):    
    if i!=87 and i!=166 and i!=192 and i!=266 and i!=287:      
        if datos1["Oldpeak"][i]<1:
            datos1["Oldpeak"][i]=1
        elif datos1["Oldpeak"][i]>=1 and datos1["Oldpeak"][i]<2:
            datos1["Oldpeak"][i]=2
        elif datos1["Oldpeak"][i]>=2 and datos1["Oldpeak"][i]<=3:
            datos1["Oldpeak"][i]=3
        elif datos1["Oldpeak"][i]>=3:
            datos1["Oldpeak"][i]=4










