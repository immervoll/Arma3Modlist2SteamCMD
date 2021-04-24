import id_scraper
import sys
import os
from colorama import init, Fore, Back, Style
init()

pack_name = input("Pack Name: ")
modfile = input("Path to Modfile: ")
assert os.path.exists(modfile), Fore.RED + f"unable to locate the modlist html at {str(modfile)}"
user = input("Steam User: ")
pw = input("Steam Password: ")

f = open(f"modlistupdater_{pack_name}.txt", "a")
f.write(f"login {user} {pw} \n")
i=0
for id in id_scraper.getIds(modfile):
    i=i+1
    f.write(f"workshop_download_item 107410 {id} \n" )
print (Fore.GREEN + f"FINISHED: added {i} mods to the file.")
f.write("quit")
f.close()
