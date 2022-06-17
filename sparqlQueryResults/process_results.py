import pandas as pd
import os

# current directory
# files_list = [f for f in os.listdir() if not f.startswith('.')]
# print(files_list)

# df_total = pd.DataFrame()
# # Total files 5
# for item in range(1, 6):
#     print(item)
#     df_partial = pd.read_csv("Q{}_sparql.csv".format(str(item)))
#     df_total = df_total.append(df_partial)
#
# df_total.info()
# df_total = df_total.sort_values(by=['id'], ascending=True)
# df_total.drop_duplicates(keep='first', inplace=True)
# df_total.to_csv('TOTAL_biography.csv', index=False)
#
# df_total.info()

# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 33399 entries, 0 to 8998
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   s       33399 non-null  object
#  1   id      33399 non-null  int64

# TODO:
#  update code to read new file with total biographies
files_download = [f for f in os.listdir("../dataset/") if not f.startswith('.')]
df_download = pd.DataFrame(files_download, columns=['file_name'])
df_download['file_name'] = df_download['file_name'].str.replace('.txt', '')

df_total = pd.read_csv('TOTAL_biography.csv')
df_total['id'] = df_total['id'].astype(str)
df_download = df_download.merge(df_total, left_on=["file_name"], right_on=["id"], how="inner")
df_download.drop('file_name', inplace=True, axis=1)
df_download.info()
df_download.to_csv('TOTAL_download_biographies.csv', index=False)
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 33309 entries, 0 to 33308
# Data columns (total 2 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   s       33309 non-null  object
#  1   id      33309 non-null  object