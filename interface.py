import os,sys,time
from datetime import datetime
a = datetime.now().strftime('%Y-%m-%d %H:%M')

###############################################################
####      To add time, follow this example                  ###
####      print ("python life"+a) <<<<< +a print time ;)    ###
###############################################################

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
########################################################
os.system('clear')
os.system('git pull')
os.system('clear')
########################################################
logo0 = """
\033[1;34m                       dP   dP                         
\033[1;34m                       88   88                         
\033[1;37m   88d888b. dP    dP d8888P 88d888b. .d8888b. 88d888b. 
\033[1;37m   88'  `88 88    88   88   88'  `88 88'  `88 88'  `88 
\033[1;33m   88.  .88 88.  .88   88   88    88 88.  .88 88    88 
\033[1;33m   88Y888P' `8888P88   dP   dP    dP `88888P' dP    dP 
\033[1;34m   88            .88                                   
\033[1;34m   dP        d8888P  
\n         
\033[1;34m   dP    8888b          
\033[1;37m   88 o  88             
\033[1;33m   88 dP 88aaa  .d8888b. 
\033[1;33m   88 88 88     88ooood8 
\033[1;37m   88 88 88     88 \033[1;31m    Created by Riad
\033[1;34m   dP dP dP     `88888P
"""
#################################################################"
logo1 = """
\033[1;92m	
\033[1;97m                      :::!~!!!!!:.
\033[1;97m                  .xUHWH!! !!?M88WHX:.
\033[1;97m                .X*#M@$!!  !X!M$$$$$$WWx:.
\033[1;97m               :!!!!!!?H! :!$!$$$$$$$$$$8X:
\033[1;97m              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
\033[1;97m             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
\033[1;97m             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
\033[1;97m               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
\033[1;91m               ~?WuxiW*`   `"#$$$$8!!!!??!!!
\033[1;91m             :X- M$$$$       `"T#$T~!8$WUXU~
\033[1;91m            :%`  ~#$$$m:        ~!~ ?$$$$$$
\033[1;91m          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
\033[1;97m.....   -~~\033[1;91m:<` !    ~?T#$$@@W@*?$$      /`
\033[1;97mW$@@M!!! .!~~ \033[1;91m!!     .:XUW$W!~ `"~:    :
\033[1;97m#"~~`.:x%`!!  \033[1;91m!H:   !WM$$$$Ti.: .!WUn+!`
\033[1;97m:::~:!!`:X~ .:\033[1;92m ?H.!u "$$$B$$$!W:U!T$$M~
\033[1;97m.~~   :X@!.-~   \033[1;92m?@WTWo("*$$$W$TH$! `
\033[1;97mWi.~!X$?!-~    : \033[1;92m?$$$B$Wu("**$RM!
\033[1;97m$R@i.~~ !     :   \033[1;92m~$$$$$B$$en:``     
\033[1;97m?MXT@Wx.~    :     \033[1;92m~"##*$$$$M~   
\033[1;47m                  \033[1;31mCreated by Riad                 \033[1;0m    
"""

########################################################
logo2 = """
\033[1;32m
         aaaaaa             
        dGGGGMMb                                 
       @p~qp~~qMb--------> \033[1;31mCreated by Riad \033[1;32m    
       M(@)(@) M|   
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM      
   FqM            MMM 
 __|'\ .        |\dS qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--
"""
########################################################
print(logo0)
print("\033[1;31m[1] \033[1;34mSee the user interface")
time.sleep(0.3)
print("\033[1;31m[2] \033[1;34mStart interface")
time.sleep(0.3)
print("\033[1;31m[3] \033[1;34mRemove termux login")
time.sleep(0.3)
print("\033[1;31m[4] \033[1;34mMy instagram")
time.sleep(0.3)
print("\033[1;31m[5] \033[1;34mYouTube")
time.sleep(0.3)
print("\033[1;31m[0] \033[1;34mExit")
time.sleep(0.3)
print("")
######################################################################
choose = input("\033[1;31m[?]\033[1;34mChoose an option : ")
time.sleep(0.3)
########################################################
if choose == '1':
    os.system('clear')
    print(logo0)
    time.sleep(0.3)
    print("\033[1;36m")
    print(a)
    print("")
    print(logo1)
    time.sleep(0.3)
    print("\033[1;36m")
    print(a)
    print("")
    print(logo2)
    time.sleep(0.3)
    print("\033[1;36m")
    print(a)


if choose == '2':
    os.system('cp log.py $HOME')
    os.chdir('/data/data/com.termux/files/usr/etc')
    os.system('rm -rf bash.bashrc')
    os.system('cd $HOME;cd interface/log;cp bash.bashrc /data/data/com.termux/files/usr/etc')
    os.system('clear')
    print(logo0)
    jalan("\033[1;36mRestart the application")
    time.sleep(0.5)
    print("\033[1;36m")
    print(a)
    os.system('exit')
########################################################
elif choose == '3':
    jalan("\033[1;31mplease wait...")
    os.system('cd /data/data/com.termux/files/usr/etc;rm -rf bash.bashrc')
    os.system('cd $HOME;cd login/original ;cp bash.bashrc /data/data/com.termux/files/usr/etc')
    os.system('clear')
    print(logo0)
    print("\033[1;36mRestart the application")
    time.sleep(0.5)
    print("\033[1;36m")
    print(a)
    os.system('exit')
########################################################
elif choose == '4':
    os.system('xdg-open https://www.instagram.com/python.life')
    os.system('clear')
    print(logo0)
    time.sleep(0.3)
    print("\033[1;36m")
    print(a)
    os.system('exit')
########################################################
elif choose == '5':
    os.system('xdg-open https://www.youtube.com/c/pythonlife')
    os.system('clear')
    print(logo0)
    time.sleep(0.3)
    print("\033[1;36m")
    print(a)
    os.system('exit')
########################################################
elif choose == '0':
    os.system('xdg-open https://www.youtube.com/c/pythonlife')
    os.system('clear')
    print(logo0)
    print("\033[1;36m")
    print(a)
    os.system('exit')
########################################################



