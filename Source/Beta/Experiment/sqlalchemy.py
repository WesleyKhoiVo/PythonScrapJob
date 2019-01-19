import pyodbc
from sqlalchemy import create_engine
import urllib

params = urllib.quote_plus(r'DRIVER={SQL Server};SERVER=bidept;DATABASE=BIDB;Trusted_Connection=yes')
### For python 3.5: urllib.parse.quote_plus 
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine = create_engine(conn_str)
reload(sys)
sys.setdefaultencoding('utf8')

df.to_sql(name='Test',con=engine, if_exists='append',index=False)