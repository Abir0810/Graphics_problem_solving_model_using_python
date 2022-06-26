#!/usr/bin/env python
# coding: utf-8

# # Radar plot using Python

# In[7]:


import plotly.express as px
import pandas as pd
data=pd.DataFrame(dict(keys=[10,20,30,40], values=["Labour cost","Manufacturing cost","Promotion cost","Sellling cost"]))
figure=px.line_polar(data, r='keys', theta='values',line_close=True)
figure.update_traces(fill="toself")
figure.show()


# In[ ]:




