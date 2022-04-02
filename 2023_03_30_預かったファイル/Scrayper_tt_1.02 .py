import subprocess
import os

print("""
************************************************************

Scyatper_tt　メインメニュー

スクレイピング開始
Scrayper_tt"の終了は　Ctrl ＋　C　で終了します。

************************************************************
""")

import time


def main():
    t = 2500
    for i in range(t):
        print("\r{1}/{2}".format(
            "="*(i+1)+"-"*(t-i-1) , i+1, t), end="")
        time.sleep(1)
    print("")


i = 0
while i < 5:
    command = ["py", "mn.py"]
    proc = subprocess.Popen(command)  # ->コマンドが実行される(処理の終了は待たない)
    result = proc.communicate()
    print("""
    次の起動まで
    """)
    main()







