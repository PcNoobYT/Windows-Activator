import os
from colorama import *

init(convert=True)

M = Fore.LIGHTMAGENTA_EX
B = Fore.LIGHTBLUE_EX
R = Fore.LIGHTRED_EX
Y = Fore.LIGHTYELLOW_EX
G = Fore.LIGHTGREEN_EX
D = Fore.LIGHTBLACK_EX
C = Fore.RESET

os.system("cls")

print(M + "[1]" + C + " Activate windows")
print(Y + "[2]" + C + " Remove watermark")
print(G + "[3]" + C + " Upgrade windows edition" + D + " (Only for windows 11)")
print(B + "[4]" + C + " Delete current activation key")
print(R + "[5]" + " Exit")
choice = int(input(B + "[" + C + ">" + B + "] " + C))

if choice == 1:
    os.system("cls")
    print("Please choose windows version:")
    print(M + "[1]" + C + " Windows 11")
    print(Y + "[2]" + C + " Windows 10")
    print(R + "[3]" + C + " Windows 8.1")
    edition = int(input(B + "[" + C + ">" + B + "] " + C))
    if edition == 1:
        os.system("cls")
        print("Please select edition:")
        print(M + "[1]" + C + " Home/Core")
        print(Y + "[2]" + C + " Pro")
        print(R + "[3]" + C + " Enterprise")
        choice2 = int(input(B + "[" + C + ">" + B + "] " + C))
        if choice2 == 1:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice2 == 2:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice2 == 3:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
    if edition == 2:
        os.system("cls")
        print("Please select edition:")
        print(M + "[1]" + C + " Home/Core")
        print(Y + "[2]" + C + " Pro")
        print(R + "[3]" + C + " Enterprise")
        choice3 = int(input(B + "[" + C + ">" + B + "] " + C))
        if choice3 == 1:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice3 == 2:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice3 == 3:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
    if edition == 3:
        os.system("cls")
        print("Please select edition:")
        print(M + "[1]" + C + " Home/Core")
        print(Y + "[2]" + C + " Pro")
        print(R + "[3]" + C + " Enterprise")
        choice4 = int(input(B + "[" + C + ">" + B + "] " + C))
        if choice4 == 1:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk M9Q9P-WNJJT-6PXPY-DWX8H-6XWKK")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice4 == 2:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk GCRJD-8NW9H-F2CDX-CCM8D-9D6T9")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
        if choice4 == 3:
            os.system("cls")
            print(Y + "Activating windows...")
            os.system("slmgr /ipk MHF9N-XY6XB-WVXMC-BTDCT-MKKG7")
            os.system("slmgr /skms kms8.msguides.com")
            os.system("slmgr /ato")
            os.system("cls")
            print(G + "activation complete!")
if choice == 2:
    os.system("cls")
    print(Y + "Resetting activation period...")
    os.system("slmgr -rearm")
    os.system("cls")
    print(G + "Reset!")
if choice == 3:
    os.system("cls")
    print("Please select desired windows edition:")
    print(M + "[1]" + C + " Windows 11 Home")
    print(Y + "[2]" + C + " Windows 11 Pro")
    print(R + "[2]" + C + " Windows 11 Enterprise" + D + "( Please research before upgrading to Enterprise)")
    choice5 = int(input(B + "[" + C + ">" + B + "] " + C))
    if choice5 == 1:
        os.system("cls")
        print(Y + "Upgrading to Windows 11 Home...")
        os.system("slmgr /ipk YTMG3-N6DKC-DKB77-7M9GH-8HVX7")
        os.system("slmgr /ato")
        os.system("cls")
        print(G + "Upgrade successful! please restart pc")
    if choice5 == 2:
        os.system("cls")
        print(Y + "Upgrading to Windows 11 Pro...")
        os.system("slmgr /ipk VK7JG-NPHTM-C97JM-9MPGT-3V66T")
        os.system("slmgr /ato")
        os.system("cls")
        print(G + "Upgrade successful! please restart pc")
    if choice5 == 3:
        os.system("cls")
        print(Y + "Upgrading to Windows 11 Enterprise...")
        os.system("slmgr /ipk XGVPP-NMH47-7TTHJ-W3FW7-8HV2C")
        os.system("slmgr /ato")
        os.system("cls")
        print(G + "Upgrade successful! please restart pc")
if choice == 4:
    os.system("cls")
    print("Deleting current activation key...")
    os.system("slmgr /upk")
    os.system("cls")
    print(G + "Key deleted!")
if choice == 5:
    quit()
