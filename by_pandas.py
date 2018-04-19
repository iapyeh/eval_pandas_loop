#
# 原始檔案取材自：「寫程式是資料分析的必要技能」
# https://medium.com/datainpoint/%E5%AF%AB%E7%A8%8B%E5%BC%8F%E6%98%AF%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90%E7%9A%84%E5%BF%85%E8%A6%81%E6%8A%80%E8%83%BD-9ee15b58cc
#
import sys
import pandas as pd
def get_college_town_list(txt_url):
  df = pd.read_table(txt_url, header=None)
  df.columns = ['StateRegion']
  df['StateFlag'] = df['StateRegion'].str.contains(pat=r'\[edit\]')
  df_states = df[df['StateFlag'] == True]
  # 找出不重複州名 -------------
  States = df_states['StateRegion'].str.replace(pat=r'\[edit\]', repl='').unique()
  StateFlags = df['StateFlag'].values
  j = 0
  StateMatchRegion = [States[j]]
  # 分隔州名與區域名的邏輯 -------------
  for i in range(1, len(StateFlags)):
    if StateFlags[i] == True:
      j += 1
      StateMatchRegion.append(States[j])
    else:
      StateMatchRegion.append(States[j])
  # 清理資料 -------------
  df['StateMatchRegion'] = StateMatchRegion
  df['RegionName'] = df['StateRegion'].str.replace(pat=r'\s\(.*', repl='')
  ans = df[df['StateFlag'] == False]
  ans = ans.drop(['StateRegion', 'StateFlag'], axis=1)
  ans.columns = ['State', 'RegionName']
  ans = ans.reset_index(drop=True)
  return ans

#txt_url = "https://storage.googleapis.com/um_ds_intro/college_towns.txt"
#txt_url = 'college_towns.txt'

# 從命列列讀取輸入檔案名稱與路徑
txt_url = sys.argv[1]
ans = get_college_town_list(txt_url)

import os
folder = os.path.dirname(txt_url)
# 輸出目錄與輸入檔案相同
file_name = os.path.join(folder,'output.by_pandas.tsv')
if os.path.exists(file_name): os.unlink(file_name)
ans.to_csv(file_name, sep='\t')