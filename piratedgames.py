import webbrowser

def menu():
    print("""   ___  _          __         _______                 
  / _ \(_)______ _/ /____ ___/ / ___/__ ___ _  ___ ___
 / ___/ / __/ _ `/ __/ -_) _  / (_ / _ `/  ' \/ -_|_-<
/_/  /_/_/  \_,_/\__/\__/\_,_/\___/\_,_/_/_/_/\__/___/
 ____________________________________________________ 
/___/___/___/___/___/___/___/___/___/___/___/___/___/ 
                                                 
                                                       """)

    print("[1] Required Components")
    print("[2] Repacks")
    print("[3] Trainers")
    print("[4] Exit\n")

menu()

def rc():
        print("[1] DirectX")
        print("[2] Visual C++")
        print("[3] Back")
        reqponents = input(">> ")
        
        if reqponents =='1':
            webbrowser.open('https://www.microsoft.com/en-us/download/details.aspx?id=35')
            rc()
            reqponents = input(">> ")
        
        if reqponents =='2':
            webbrowser.open('https://github.com/abbodi1406/vcredist/releases/tag/v0.58.0')
            rc()
            reqponents = input(">> ")
        
        if reqponents =='3':
            menu()

def repack():
    print("[1] Fitgirl")
    print("[2] Elamigos")
    print("[3] Masquerade")
    print("[4] M4CKD0GE")
    print("[5] Back")
    rpck = input(">> ")

    if rpck =='1':
        webbrowser.open('https://fitgirl-repacks.site')
    
    if rpck =='2':
        webbrowser.open('https://elamigos.site/')

    if rpck =='3':
        webbrowser.open('https://masquerade.site/')
    
    if rpck =='4':
        webbrowser.open('https://m4ckd0ge-repacks.me/')

    if rpck =='5':    
        menu()

def trainers():
    print("[1] Fearless Revoluton")
    print("[2] UnknownCheats")
    print("[3] WeMod")
    print("[4] GameCopyMod")
    print("[5] Back")
    train = input(">> ")

    if train =='1':
        webbrowser.open('https://fearlessrevolution.com/')

    if train =='2':
        webbrowser.open('https://www.unknowncheats.me')

    if train =='3':
        webbrowser.open('https://www.wemod.com/')

    if train =='4':
        webbrowser.open('https://gamecopyworld.com/games/index.php')
    
    if train =='5':
        menu()

while True:
    pilih = input(">> ")

    if pilih =='1':
     rc()

    if pilih =='2':
     repack()

    if pilih =='3':
        trainers()
    
    if pilih=='4':
        exit()
