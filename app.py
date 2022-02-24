#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model
import joblib

@app.route("/", methods = ["GET", "POST"])

def index():
    if request.method == "POST":
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        Income = request.form.get("Income")
        print(Age, Loan, Income)
        model = joblib.load("XGBoost")
        pred = model.predict([[float(Income), float(Age), float(Loan)]])
        print(pred)
        if(pred == 1):
            prediction = "Yes"
        else:
            prediction = "No"
        s = "The predicted default is : " + prediction
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Cannot reach"))        


# In[4]:


app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




