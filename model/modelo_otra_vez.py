#!/usr/bin/env python
# coding: utf-8

# # final seguuun

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Evaluacion
from sklearn.metrics import (r2_score, roc_auc_score,
                            classification_report, confusion_matrix,
                            roc_curve, accuracy_score)

#ML
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

#DataViz
import scikitplot as skplt
import seaborn as sns
font = {'family' : 'sans','weight' : 'bold','size'   : 20}
plt.rc('font', **font)
plt.rcParams['xtick.labelsize'] = 16
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['figure.figsize'] = (16,8)


# Biblioteca para dibujar árboles
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score #for cross validation
from sklearn.metrics import confusion_matrix #confusion matrix
from sklearn.metrics import plot_confusion_matrix #to draw a confusion matrix


#support vector machine
from sklearn.preprocessing import scale  #scale and center data
from sklearn.svm import SVC #support vector machine for classification
from sklearn.decomposition import PCA #to perfom PCA to plot the data
from sklearn.model_selection import GridSearchCV #for cross validation


# In[2]:


df = pd.read_excel('copia_base-limpia_para_modelo2.xlsx')


# In[3]:


#variables predictoras
X = df.loc[:, [
    'Edad', 'Educación', 'Estado Civil',
       'Coincidencia INE-Comprobante', 'Tiempo en vivienda',
       'Con quién vive', 'Tipo de vivienda', 'Dependientes Ecónomicos',
       'Ocupación anterior', 'Otra fuente ingresos',
       'Tiempo registrado en plataforma',
       'Tiempo conduciendo continuo', 'Alta en plataforma',
       'A quien le depositaban ganancias', 'Calificacion Plataforma',
       'Expresión del enojo', 'Criterio Violencia',
       'Antecedentes legales o penales', 
       'Control del enojo', 'Tendencia a incumplir', 'Uso de palabras fuertes',
       'Inversión de tiempo y esfuerzo', 'Enojo fácil',
       'Quedarse objetos ajenos', 'Tendencia a robo',
       'Sacar adelante el trabajo', 'Se considera despreocupado',
       'Tendencia a actuar sin pensar', 'Tendencia a mentir',
       'Tendencia a no hacer caso', 'Disfruta la adrenalina',
       'Gusto por manejar a velocidad', 'Manejar a velocidad',
       'Tardó en dar respuestas', 'Perfil estable', 'Perfil pasivo-agresivo',
       'Perfil impulsivo'
              ]]

#variable a predecir
Y = df['Estatus']


# In[4]:


categ = ['Educación', 'Estado Civil',
       'Coincidencia INE-Comprobante', 'Tiempo en vivienda',
       'Con quién vive', 'Tipo de vivienda', 'Dependientes Ecónomicos',
       'Ocupación anterior', 'Otra fuente ingresos',
       'Tiempo registrado en plataforma',
       'Tiempo conduciendo continuo', 'Alta en plataforma',
       'A quien le depositaban ganancias', 'Calificacion Plataforma',
       'Expresión del enojo', 'Criterio Violencia',
       'Antecedentes legales o penales', 
       'Tardó en dar respuestas'
        ]

from sklearn.preprocessing import LabelEncoder

# Encode Categorical Columns
le = LabelEncoder()
X[categ] = X[categ].apply(le.fit_transform)


# In[19]:


#split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 0)

#create a decision tree
arbol = DecisionTreeClassifier(random_state=0)
arbol = arbol.fit(X_train, Y_train)


# In[6]:


arbol.score(X_train, Y_train)


# In[7]:


# plot the tree
plt.figure(figsize=(15, 7.5))
plot_tree(arbol,
          filled = True,
          rounded = True,
          class_names = ['Denegado', 'Aprobado'],
          feature_names = X.columns);


# In[8]:


#plot confusion matrix on the test data
plot_confusion_matrix(arbol, X_test, Y_test, 
                    #  display_labels = ['Denegado', 'Aprobado'], 
                      cmap=plt.cm.Blues)


# In[9]:


#cost complexity pruning
path = arbol.cost_complexity_pruning_path(X_train, Y_train) #determine values for alpha
ccp_alphas = path.ccp_alphas #extract different values for alpha
ccp_alphas = ccp_alphas[:-1] #exclude the maximum value for alpha

arbols = [] #array to put decision trees into

#create a decision tree per value for alpha and store it in the array
for ccp_alpha in ccp_alphas:
    arbol = DecisionTreeClassifier(random_state=0, ccp_alpha = ccp_alpha)
    arbol.fit(X_train, Y_train)
    arbols.append(arbol)


# In[10]:


#graph
train_scores = [arbol.score(X_train, Y_train) for arbol in arbols]
test_scores = [arbol.score(X_test, Y_test) for arbol in arbols]

fig, ax = plt.subplots()
ax.set_xlabel('alpha')
ax.set_ylabel('accuracy')
ax.set_title('accuracy  vs alpha for training and testing sets')
ax.plot(ccp_alphas, train_scores, marker = 'o', label = 'train', drawstyle = 'steps-post')
ax.plot(ccp_alphas, test_scores, marker = 'o', label = 'test', drawstyle = 'steps-post')
ax.legend()
plt.show()


# In[11]:


#array to store the results of each fold during cross validation
alpha_loop_values = []

# for each candidate value for alpha, we will run 5-fold cross validation
#then we will store the mean and standar deviation of the scores (the accuracy) for each call
#to cross_val_score in alpha_loop_values..

for ccp_alpha in ccp_alphas:
    arbol = DecisionTreeClassifier(random_state = 0, ccp_alpha = ccp_alpha)
    scores = cross_val_score(arbol, X_train, Y_train, cv = 5)
    alpha_loop_values.append([ccp_alpha, np.mean(scores), np.std(scores)])

#now we can drawa graph of the means and standar deviations of the scores
#for each candidate value for alpha
alpha_results = pd.DataFrame(alpha_loop_values,
                             columns = ['alpha', 'mean_accuracy', 'std'])

alpha_results.plot(x = 'alpha',
                   y = 'mean_accuracy',
                   yerr = 'std',
                   marker = 'o',
                   linestyle = '--')


# In[12]:


alpha_results[(alpha_results['alpha']> 0.0036)
              &
              (alpha_results['alpha']< 0.0038)]


# In[13]:


ideal_ccp_alpha = alpha_results[(alpha_results['alpha']> 0.0036)
                  &
                  (alpha_results['alpha']< 0.0038)]['alpha']
ideal_ccp_alpha


# In[14]:


#convert ideal_ccp_alpha from a series to a float
ideal_ccp_alpha = float(ideal_ccp_alpha)
ideal_ccp_alpha


# In[15]:


#Build and train a new decision tree, using the optimal value for alpha
arbol_pruned = DecisionTreeClassifier(random_state = 0,
                                      ccp_alpha = ideal_ccp_alpha)
arbol_pruned = arbol_pruned.fit(X_train, Y_train)


# In[16]:


#nueva matriz de confusión
plot_confusion_matrix(arbol_pruned,
                      X_test,
                      Y_test,
                    #  display_labels = ['Denegado', 'Aprobado'],
                      cmap=plt.cm.Blues
                     )


# In[17]:


plt.figure(figsize = (15, 7.5))
plot_tree(arbol_pruned,
          filled = True,
          rounded = True,
        #  class_names = ['Denegado', 'Aprobado'],
          feature_names = X.columns);


# In[20]:


#Importance of the variables
pd.DataFrame(arbol.feature_importances_,
                     index = X.columns, columns=['Importancia_de_variables'])


# In[21]:


#DF de variables mas importantes
f_imp = pd.DataFrame(arbol.feature_importances_,
                     index=X.columns, columns=['Importancia_de_variables'])
#calculo de importancia relativa
f_imp['importancia_relativa'] = (f_imp/f_imp.max()*100)
#plot de importancia de variables
f_imp.sort_values('importancia_relativa',ascending=True).importancia_relativa.plot.barh(figsize=(6,7),
                                                              title='Importancia de Variables',color='magenta')
plt.xlabel('Importancia relativa');


# In[22]:


print(arbol_pruned.score(X_test, Y_test)) #árbol


# In[23]:


import pickle

modelo_aprobado_denegado = 'modelo_aprobado_denegado.pkl'
pickle.dump(arbol_pruned, open(modelo_aprobado_denegado, 'wb'))


# In[24]:


transf = 'transf.pkl'
pickle.dump(le, open(transf, 'wb'))


# In[25]:


loaded_model = pickle.load(open('modelo_aprobado_denegado.pkl', 'rb'))
modelo = pd.read_pickle('modelo_aprobado_denegado.pkl')


# In[ ]:


prueba = pd.read_excel('prueba_limpia.xlsx')


# In[ ]:


categ = ['Educación', 'Estado Civil',
       'Coincidencia INE-Comprobante', 'Tiempo en vivienda',
       'Con quién vive', 'Tipo de vivienda', 'Dependientes Ecónomicos',
       'Ocupación anterior', 'Otra fuente ingresos',
       'Tiempo registrado en plataforma',
       'Tiempo conduciendo continuo', 'Alta en plataforma',
       'A quien le depositaban ganancias', 'Calificacion Plataforma',
       'Expresión del enojo', 'Criterio Violencia',
       'Antecedentes legales o penales', 
       'Tardó en dar respuestas'
        ]


# In[ ]:


transf = pd.read_pickle('transf.pkl')


# In[ ]:


prueba[categ] = prueba[categ].apply(transf.fit_transform)


# In[ ]:


#p_x_vect = prueba.apply(transf.fit_transform)


# In[ ]:


loaded_model = pickle.load(open('modelo_aprobado_denegado.pkl', 'rb'))
x = loaded_model.predict(prueba)
x


# In[ ]:





# In[26]:





# In[27]:





# In[29]:





# In[ ]:




