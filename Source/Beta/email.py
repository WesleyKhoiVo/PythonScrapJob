import re
from pandas import ExcelWriter
import pandas as pd

website = []
tencongty = []
tencongviec = []
diachi = []
motacongviec = []
yeucaucongviec =[]
loiich=[]
tienluong=[]
ngaypost=[]
ngayend=[]
phonenumber=[]
data = pd.read_excel('../../../Result/Preprocessed Web Data ver1.1.xlsx', skip_blank_lines=True, skipinitialspace=True)

#print(data.iloc[:,0])
for i in range (0,len(data.iloc[:,0])) :
    phone_number= re.findall(r'(\+84|84|0)([0-9]{8,10})\b',data['Detail'].iloc[i])
    phonenumber.append(phone_number)
    website.append(data['Website'].iloc[i])
    tencongty.append(data['Name'].iloc[i])
    tencongviec.append(data['Title'].iloc[i])
    tienluong.append(data['Salary'].iloc[i])
    diachi.append(data['Location'].iloc[i])
    motacongviec.append(data['Detail'].iloc[i])
    yeucaucongviec.append(data['Requirement'].iloc[i])
    loiich.append(data['Benefits'].iloc[i])
    ngaypost.append(data['Date Post'].iloc[i])
    ngayend.append(data['End Date'].iloc[i])
        
df = pd.DataFrame({'Website':website,
                    'Company':tencongty,
                   'Job Title':tencongviec,
                   'Salary':tienluong,
                   'Location':diachi,
                   'Detail':motacongviec,
                   'Requirement':yeucaucongviec,
                   'Phone Number':phonenumber,
                   'Post Date':ngaypost,
                   'End Date':ngayend
                   })
writer = ExcelWriter("../../../Result/Preprocessed Web Data ver1.2(Email added).xlsx")
df.to_excel(writer)
writer.save()