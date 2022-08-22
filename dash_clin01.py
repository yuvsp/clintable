#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import flask
from flask_table import Table, Col, LinkCol
from flask import Flask, redirect, url_for, render_template, request,flash,Markup


from dash.dependencies import Input, Output, State
import dash
import dash_bootstrap_components as dbc


# In[2]:


# pip install dash_bootstrap_components


# In[3]:


df = pd.read_excel('clin.xlsx',header=0).fillna("")


# In[4]:


# df


# In[5]:


server = Flask(__name__)
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',dbc.themes.BOOTSTRAP]
# app = dash.Dash(__name__,external_stylesheets=external_stylesheets,server=server, prevent_initial_callbacks=True)


# app.run()


# In[6]:


@server.route('/')
def leview():
    try:              
        df = pd.read_excel('clin.xlsx',header=0).fillna("")
        return render_template('clin.html',data=df.T.to_dict().values(),
                               column_names=df.columns.values,row_data=list(df.values.tolist()),link_column="",
                               zip=zip,msg='',unreachable_txt='',num_not_reachable='', status_title = '')                       
    except Exception as e:
        print("ERROR")
        print(e)


# In[7]:


# leview()


# In[ ]:


if __name__ == '__main__':
     server.run(debug=False)


# In[ ]:




