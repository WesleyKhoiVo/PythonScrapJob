import pandas as pd
train = pd.read_excel('../../../Result/Data Science and Big Data Viet Nam.xlsx',sheet_name = 0)
train['word_count'] = train['Posts'].apply(lambda x: len(str(x).split(" ")))
train[['Posts','word_count']].head()
