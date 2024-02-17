disabler_file = "disable.so"
file = "L.so.gz"
import os
os.system("pkg install wget -y")
os.system("pkg install clang binutils python3 libffi openssl libsodium git iproute2")
os.system("SODIUM_INSTALL=system pip3 install pynacl")
os.system("pip uninstall requests chardet urllib3 idna certifi pycryptodome pycryptodomex -y;pip install chardet urllib3 idna certifi requests pip install  pycryptodome pycryptodomex ")
os.system("pip install pynacl")
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/FILE')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')
  
def install_part(file_name):
  os.system(f"curl -L https://github.com/Ahmed-XD/library/blob/main/{file_name}?raw=true -o {file_name}")

try:os.remove("x3.so")
except Exception:pass
try:os.remove("L.so")
except Exception:pass
if os.path.exists(disabler_file) and os.path.exists(file):
  os.remove(disabler_file)
  os.remove(file)

intro()
install_part(disabler_file)
install_part(file)
os.system(f"gzip -d {file}")
os.system(f"chmod 777 L.so")
os.system("clear")

import disable
import L

