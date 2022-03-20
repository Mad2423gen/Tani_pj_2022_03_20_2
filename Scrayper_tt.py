import time
import os
import sys


print("""
************************************************************

Scyatper_tt　メインメニュー

スクレイピング開始
Scrayper_tt"の終了は　Ctrl ＋　C　で終了します。

************************************************************
""")

import time
import mn
import subprocess




def main():
    for i in range(2000):
        print("\r{1}/{2}".format(
            "="*(i+1)+"-"*(2000-i-1) , i+1, 2000), end="")
        time.sleep(1)
    print("")


def run():
    command = ["python3", "mn.py"]
    proc = subprocess.Popen(command)  # ->コマンドが実行される(処理の終了は待たない)
    result = proc.communicate()  # ->終了を待つ



i = 0
while i < 5:
    run()
    print("""
    次の起動まで
    """)
    main()







