#!/usr/bin/env python3
import os,sys
ans = []
current_state = None
current_universities = None
# 從命列列讀取輸入檔案名稱與路徑
txt_url = sys.argv[1]
with open(txt_url,'rb') as fd:
    for row in fd:
        p = row.rfind(b'[edit]')
        if  p > 0:
            current_state = row[:p].rstrip()
            current_universities = []
            ans.append([current_state,current_universities])
        else:
            current_universities.append(row[:row.find(b'(')].rstrip())

# 輸出目錄與輸入檔案相同
counter = 0
folder = os.path.dirname(txt_url)
file_name = os.path.join(folder,'output.by_loop.tsv')
if os.path.exists(file_name): os.unlink(file_name)
with open(file_name,'wb') as fd:
    fd.write(b'\t'.join([b'',b'State',b'RegionName'])+b'\n')
    for state, universities in ans:
        for university in universities:
            fd.write(b'\t'.join([str(counter).encode('ascii'),state,university])+b'\n')
            counter += 1
        