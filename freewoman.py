import requests
import os
import time as t
URL = "https://api.mojang.com/users/profiles/minecraft/"




def main():
    clear()
    free = ["no names found"]
    banner()
    input("Press Enter to continue")
    clear()
    inputString = input("Input your Names you want to check:\n")
    inputString = inputString.split()
    count = 0
    for name in inputString:
        
        free,count = httpsRequest(name,count,free)
        
        t.sleep(1)
    clear()
    banner()
    c1 = 0
    for x in free:
        print(x, end = "        ")
        if c1 >= 6: 
            print("\n")
            c1 = 0
        c1 += 1
    restart()


def httpsRequest(name, count ,free):
    r = requests.get(url=URL+name)
    print(name + " Statuscode: " + str(r.status_code))
    if r.status_code == 204:
        if count == 0:
            free.remove("no names found")
        free.append(name)
        count += 1
    return free, count;
        


def clear(): os.system('cls')


def banner():
    logo = '''
    ___________                        __      __                             
    \_   _____/______   ____   ____   /  \    /  \____   _____ _____    ____  
      |    __) \_  __ \_/ __ \_/ __ \  \   \/\/   /  _ \ /     \\__  \  /    \\
      |     \   |  | \/\  ___/\  ___/   \        (  <_> )  Y Y  \/ __ \|   |  \\
      \___  /   |__|    \___  >\___  >   \__/\  / \____/|__|_|  (____  /___|  /
          \/                \/     \/         \/              \/     \/     \/ 
    '''
    print(logo)

def restart():
    input("\nPress Enter to continue")
    main
    main()
main()