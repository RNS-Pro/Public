import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from DUMP import menu
    menu()
elif bit == '32bit':
    from EXTRACT import menu
    menu()
