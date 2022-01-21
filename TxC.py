Rathu = '\033[1;31m'
Kola = '\033[1;33m'
Kaha = '\033[1;32m'


def banner():
    print("\033[1;33m  __         ___   ")
    print("\033[1;33m |_   |  _  / __|  ")
    print("\033[1;31m   | | \ \/ / | |      ")
    print("\033[1;31m   | |  >  <  | |_   ")
    print("\033[1;33m   || //\_\  \__|ʙʏ ᴍʀ.ᴛʜᴇɴᴜx  ")
    print("")


banner()
basket=0
x=str(input("\033[1;32m Enter the msg :\n")) #thenux
t=str(input("\033[1;32m Enter the letter / number you want to count :\n"))
y=len(x)
for i in range(0,y):
    if (x[i]==t):
        basket=basket+1
        print (basket)
