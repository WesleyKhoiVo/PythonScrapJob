import re
from pandas import ExcelWriter
import pandas                       as pd
#import xlsxwriter

bang=[]
data = pd.read_excel('../../../Result/Preprocessed Web Data ver1.1.xlsx', skip_blank_lines=True, skipinitialspace=True)
df = pd.DataFrame({'job_description':data.job_description,
                       })
for i in data.job_description:
        email= re.findall(r'[\w\.,]+@[\w\.,]+',i)
        bang.append(email)
df['Email']=bang

writer = ExcelWriter("email.xlsx")
df.to_excel(writer)
writer.save() 
print(bang)