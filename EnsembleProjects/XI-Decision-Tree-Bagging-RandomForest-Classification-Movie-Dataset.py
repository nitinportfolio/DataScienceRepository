#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In the movie dataset we will try to classify whether movie recieved any Oscar or not using Decision Tree


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree


from sklearn.metrics import (confusion_matrix, accuracy_score, plot_roc_curve,
                            ConfusionMatrixDisplay, auc, classification_report, f1_score)


# In[3]:


try:
    # See #1137: this allows compatibility for scikit-learn >= 0.24
    from sklearn.utils import safe_indexing
except ImportError:
    from sklearn.utils import _safe_indexing


# In[4]:


import yellowbrick


# In[5]:


from yellowbrick.classifier import ROCAUC


# In[6]:


data = pd.read_csv('./data/Movie_classification.csv')


# In[7]:


data.shape


# In[8]:


data.head()


# In[9]:


data['Start_Tech_Oscar'].value_counts()


# In[10]:


data.info()


# In[11]:


data['Time_taken'].fillna(data['Time_taken'].mean(), inplace=True)


# In[12]:


data.isnull().sum().sum()


# In[13]:


# Creating Dummy Variables


# In[14]:


data = pd.get_dummies(data, columns=['Genre','3D_available'],drop_first=True)


# In[15]:


X_train, X_test, y_train, y_test = train_test_split(data.drop(labels=['Start_Tech_Oscar'],axis = 1), data['Start_Tech_Oscar'],
                                                   test_size=0.3, random_state=42)


# ## Building Decision Tree Classifier

# In[16]:


clftree = DecisionTreeClassifier(max_depth=3)
clftree.fit(X_train,y_train)


# ### Predicting Values

# In[17]:


y_train_pred = clftree.predict(X_train)
y_test_pred = clftree.predict(X_test)


# ### Evaluating Model Performance

# In[18]:


# Confusion Matrix for training data
cm = confusion_matrix(y_train, y_train_pred)
cm


# In[19]:


# Confusion Matrix for test data
cm = confusion_matrix(y_test, y_test_pred)
cm


# In[20]:


# Training data accuracy

accuracy_score(y_train,y_train_pred)


# In[21]:


# Test data accuracy

accuracy_score(y_test,y_test_pred)


# ### Plotting Decision Tree
# 

# In[22]:


fig = plt.figure(figsize=(35,30))
_ = plot_tree(clftree, filled=True, feature_names=X_train.columns)


# In[23]:


### Controlling Tree Growth


# In[24]:


clftree = DecisionTreeClassifier(max_depth=4, min_samples_leaf=20 )
clftree.fit(X_train,y_train)


# In[25]:


y_train_pred = clftree.predict(X_train)
y_test_pred = clftree.predict(X_test)


# In[26]:


# Confusion Matrix for test data
cm = confusion_matrix(y_test, y_test_pred)
cm


# In[27]:


# Test data accuracy

accuracy_score(y_test,y_test_pred)


# ## Using Bagging

# In[28]:


from sklearn.ensemble import BaggingClassifier


# In[29]:


bag_clf = BaggingClassifier(base_estimator=clftree, n_estimators=1000, bootstrap=True, n_jobs=-1, random_state=0)


# In[30]:


bag_clf.fit(X_train, y_train)


# In[31]:


cm =  confusion_matrix(y_test, bag_clf.predict(X_test))
cm
                       


# In[32]:


accuracy_score(y_test, bag_clf.predict(X_test))


# ## Using Random Forest

# In[33]:


from sklearn.ensemble import RandomForestClassifier


# In[34]:


rf_clf = RandomForestClassifier(n_estimators=1000, n_jobs = 1, random_state=0)


# In[35]:


rf_clf.fit(X_train, y_train)


# In[36]:


cm =  confusion_matrix(y_test, rf_clf.predict(X_test))
cm
     


# In[37]:


accuracy_score(y_test, rf_clf.predict(X_test))


# ## Grid SearchCV

# In[38]:


from sklearn.model_selection import GridSearchCV


# In[39]:


rf_clf = RandomForestClassifier(n_estimators=250, random_state=0)


# In[40]:


param_grid = {
    'max_features':[4,5,6,7,8,910],
    'min_samples_split':[2,3,10]
}


# In[49]:


grid_search = GridSearchCV(rf_clf, param_grid, n_jobs = -1, cv = 5, scoring='accuracy')


# In[50]:


grid_search.fit(X_train, y_train)


# In[43]:


grid_search.best_estimator_


# In[44]:


grid_search.best_params_


# In[45]:


cvrf_clf = grid_search.best_estimator_


# In[46]:


accuracy_score(y_test, cvrf_clf.predict(X_test))


# ### Plot ROC AUC CUrve

# In[47]:


rf_plot = plot_roc_curve(cvrf_clf, X_test,y_test )


# ### Yellow Brick
# 

# In[51]:


visualizer = ROCAUC(cvrf_clf, classes = [0,1])
visualizer.fit(X_train,y_train)
visualizer.score(X_test, y_test)
visualizer.show()


# In[52]:


def myrf_model():
    rf_clf = RandomForestClassifier(n_estimators=1000, n_jobs = 1, random_state=0)
    
    


# In[ ]:




