import os 

def menu():

     print(""" 

       d88P   d88P             d8888                        8888888b.                    888                  d88P   d88P 
      d88P   d88P             d88888                        888  "Y88b                   888                 d88P   d88P  
     d88P   d88P             d88P888                        888    888                   888                d88P   d88P   
    d88P   d88P             d88P 888 88888b.  88888b.       888    888  8888b.  .d8888b  88888b.           d88P   d88P    
   d88P   d88P             d88P  888 888 "88b 888 "88b      888    888     "88b 88K      888 "88b         d88P   d88P     
  d88P   d88P             d88P   888 888  888 888  888      888    888 .d888888 "Y8888b. 888  888        d88P   d88P      
 d88P   d88P             d8888888888 888 d88P 888 d88P      888  .d88P 888  888      X88 888  888       d88P   d88P       
d88P   d88P             d88P     888 88888P"  88888P"       8888888P"  "Y888888  88888P' 888  888      d88P   d88P        
                                     888      888                                                                         
                                     888      888                                                                         
                                     888      888  
                                                       Version 1.0                                                                       
Welcome, saint.
""")

     print("------ Applications ------")
     print("1. Spotify")
     print("2. Chrome")
     print("3. Visual Studio Code")
     print("4. MSI AfterBurner")
     print("--------------------------\n")
     print("--------  Game  ----------")
     print("5. PES 2017")
     print("--------------------------\n")
     print("-------- System ----------")
     print("6. Shutdown")
     print("--------------------------\n")
     print("7. Exit")

menu()
pilih = input("Choose : ")


if pilih =='1':
     os.startfile(r"C:\Users\Naufal Zaqie\AppData\Roaming\Spotify\Spotify.exe")
     menu()
     pilih = input("Choose : ")

if pilih =='2':
     os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
     menu()
     pilih = input("Choose : ")

if pilih =='3':
     os.startfile(r"C:\Users\Naufal Zaqie\AppData\Local\Programs\Microsoft VS Code\code.exe")
     menu()
     pilih = input("Choose : ")

if pilih =='4':
     os.startfile(r"C:\Program Files (x86)\MSI Afterburner\MSIAfterburner.exe")
     menu()
     pilih = input("Choose : ")

# Game

if pilih =='5':
     os.startfile(r"C:\Games\Pro Evolution Soccer 2017\PES2017.exe")
     menu()
     pilih = input("Choose : ")

# System

if pilih =='6':
     shutdown = input("Ingin Mematikan Komputer? (Y/N): ") 
     if shutdown == 'n':
          exit()
     
     else:
          os.system("shutdown /s /t 1") # Shutdown input

if pilih =='7':
     exit()


