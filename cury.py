# Author : Satria Andhika Adi Saputro
# Codename : ./ExGeneralTz
# Lang : Python2 And Pythin3

# Modul Yang Harus Di Install
from uncompyle6.main import decompile
import marshal
import time
import sys
import os
import code
import random
import requests

#Banner-Program
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

# Def Ini Sebagai License User
def lisensi():
        os.system('clear')
        mengetik('#####################################')
        mengetik('#### \t</> \033[31;1mLICENSE LOGIN \033[37;1m</>    ####')
        mengetik('#####################################')
        username = raw_input("[*] Username : ")
        passw = raw_input("[*] Password : ")
        r = requests.get("https://pastebin.com/wGWY2A3T").text
        if passw =="":
                print"\033[1;91m[!] U/P Salah!!!"
                keluar()
        elif len(passw) < 10:
                print "\033[1;91m[!] Silakan Beli Licensi Terlebih Dahulu Sebelum Memakai Toolsnya :)"
                keluar()
        elif passw in r:
                print '\033[1;91mLogin Succesfully'
                time.sleep(1)
                
# Mengaktifkan Def Lisensi
lisensi()

# Def Ini Berfungsi Sebagai decompile Code python3
def Py3():
        print('Decompile code python3')
        c= raw_input('> File : ')
        print('')
        x=marshal.loads(code.py3)
        xx=decompile(3.7,x,sys.stdout)
        xxx="# Python 3.7.x\n# Decompile Code by ./ExGeneralTz\n"+xx.text
        with open(c+".py","w") as f:
                f.write(xxx)
        print("\n\n[]Saved] file : \033[32m%s.py"%(c))
        print('')

# Def ini berfungsi sebagai decompile code python2
def Py2():
        print('Decompile code python2')
        c= raw_input('> File : ')
        print('')
        x=marshal.loads(code.py2)
        xx=decompile(2.7,x,sys.stdout)
        xxx="# Python 2.7.x\n# Decompile Code by ./ExGeneralTz\n"+xx.text
        with open(c+".py","w") as f:
                f.write(xxx)
        print("\n\n[Saved] file : \033[32m%s.py"%(c))
        print('')

try:
        os.system('clear')
        mengetik('#####################################')
        mengetik('#### </> \033[31;1mProgram Information \033[37;1m</> ####')
        mengetik('#####################################')
        mengetik('- Author       : ./ExGeneralTz')
        mengetik('- Name Program : Decompile Marshall 2.7.x And 3.7.x')
        mengetik('- Created Date : 23-09-2019')
        print('')
        if sys.version[0] in '3':
                Py3()
        elif sys.version[0] in '2':
                Py2()
except Exception as F:
        print("Err: %s"%(F))
