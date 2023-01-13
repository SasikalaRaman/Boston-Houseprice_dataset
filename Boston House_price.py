#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd # pandas library
import openpyxl as xl #to open excel file


# In[101]:


pd.read_csv(r"C:\Users\sasik\Downloads\boston.csv") # read the data set from csv file


# In[102]:


df=pd.read_csv(r"C:\Users\sasik\Downloads\boston.csv") #assign the csv file to one variable


# In[103]:


df[df['CRIM']>=1] #  


# In[104]:


df_1=df[df['CRIM']>=1] #  It used to delete the values in CRIM column which is greater than and equal to 1


# In[105]:


print(df_1) #print the output


# In[106]:


df_1.replace(to_replace={"ZN":{0:1}},value=None) # it replace the value from 0 to 1 in ZN column


# In[107]:


df_2=df_1.replace(to_replace={"ZN":{0:1}},value=None)  # assign to another varible


# In[108]:


print(df_2)


# In[109]:


df_2.round({"NOX":2}) # round the decimal value in NOX column


# In[110]:


df_3=df_2.round({"NOX":2})


# In[111]:


print(df_3)


# In[112]:


df_3.astype(int) #convert all the value in to integer


# In[113]:


df_4=df_3.astype(int)


# In[114]:


print(df_4)


# In[115]:


df_4['AGE'].mask(df_4['AGE'] <= 20 ,"KID"  , inplace=True) # convert  in to kid if values in AGE column <= 20


# In[116]:



print(df_4)


# In[117]:



df_4['AGE'].mask(df_4['AGE'] > 20 ,"Adult"  , inplace=True) # convert  in to adult if values in AGE column > 20


# In[118]:


print(df_4)


# In[119]:


df_4['TAX'] = df_4['TAX'].astype(str).str[:-2].astype(np.int64)  # keeping 1st and removing other digits in TAX column


# In[120]:


print(df_4)


# In[121]:


excel_file=pd.ExcelWriter("newfile_data.xlsx") # write in to excel file


# In[122]:


df_4.to_excel(excel_file) # convert in to excel file


# In[123]:


excel_file.save() # save in to excel


# In[124]:


df_4.to_csv("new.csv") # convert in to csv file


# In[ ]:




