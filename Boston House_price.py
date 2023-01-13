import pandas as pd # pandas library
import openpyxl as xl #to open excel file

pd.read_csv(r"C:\Users\sasik\Downloads\boston.csv") # read the data set from csv file

df=pd.read_csv(r"C:\Users\sasik\Downloads\boston.csv") #assign the csv file to one variable

df[df['CRIM']>=1] #  

df_1=df[df['CRIM']>=1] #  It used to delete the values in CRIM column which is greater than and equal to 1

print(df_1) #print the output

df_1.replace(to_replace={"ZN":{0:1}},value=None) # it replace the value from 0 to 1 in ZN column

df_2=df_1.replace(to_replace={"ZN":{0:1}},value=None)  # assign to another varible

print(df_2)

df_2.round({"NOX":2}) # round the decimal value in NOX column

df_3=df_2.round({"NOX":2})

print(df_3)

df_3.astype(int) #convert all the value in to integer

df_4=df_3.astype(int)

print(df_4)

df_4['AGE'].mask(df_4['AGE'] <= 20 ,"KID"  , inplace=True) # convert  in to kid if values in AGE column <= 20

print(df_4)

df_4['AGE'].mask(df_4['AGE'] > 20 ,"Adult"  , inplace=True) # convert  in to adult if values in AGE column > 20

print(df_4)

df_4['TAX'] = df_4['TAX'].astype(str).str[:-2].astype(np.int64)  # keeping 1st and removing other digits in TAX column

print(df_4)

excel_file=pd.ExcelWriter("newfile_data.xlsx") # write in to excel file

df_4.to_excel(excel_file) # convert in to excel file

excel_file.save() # save in to excel

df_4.to_csv("new.csv") # convert in to csv file


# In[ ]:




