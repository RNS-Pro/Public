import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from crak import Main
    Main()
elif bit == '32bit':
    from crak import Main
    Main()
