import os,sys,time
from datetime import datetime
a = datetime.now().strftime('%Y-%m-%d %H:%M')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.006)

os.system('clear')
jalan("\033[1;34m                       dP   dP")
jalan("\033[1;34m                       88   88")
jalan("\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b.")
jalan("\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88")
jalan("\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88")
jalan("\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP")
jalan("\033[1;34m   88            .88")
jalan("\033[1;34m   dP        d8888P")
print("")
jalan("\033[1;34m   dP    8888b")
jalan("\033[1;37m   88 o  88")
jalan("\033[1;33m   88 dP 88aaa  .d8888b.")
jalan("\033[1;33m   88 88 88     88ooood8")
jalan("\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad\t\033[1;36m"+a)
jalan("\033[1;34m   dP dP dP     `88888P")
print("")


