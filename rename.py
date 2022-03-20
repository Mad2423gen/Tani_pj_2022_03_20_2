# 文字化けファイル対策、utf-8のファイルを新しく作成する

import glob
import os
import time

path = os.getcwd()
target_dir = path + "/data2" #コピーしたいファイルのディレクトリ
new_dir = path + "/data2" #新しく作るファイルのディレクトリ

def rewrate_blank(file_name):
    with open(file_name,"w",encoding="utf-8") as of:
        of.write("")

# コピー元ファイルの処理
os.chdir(target_dir)
file_lists = glob.glob("*.txt")
# コピー先ファイルの処理
os.chdir(new_dir)
for file in file_lists:
    rewrate_blank(file)
    print("ファイル名" + file + "作成済み")
    time.sleep(0.5) #あまりにも早くできるのでウェイトをもたせた







