class index :
	def __init__ (self,red,green,yellow,blue,purple,cyan,BGred,BGgreen,BGyellow,BGblue,BGpurple,BGcyan,nc):
		self.red=red
		self.green=green
		self.yellow=yellow
		self.blue=blue
		self.purple=purple
		self.cyan=cyan
		self.BGred=BGred
		self.BGgreen=BGgreen
		self.BGyellow=BGyellow
		self.BGblue=BGblue
		self.BGpurple=BGpurple
		self.BGcyan=BGcyan
		self.nc=nc
colors = index("\033[0;31m","\033[0;32m","\033[0;33m","\033[0;34m","\033[0;35m","\033[0;36m","\033[0;41m","\033[0;42m","\033[0;43m","\033[0;44m","\033[0;45m","\033[0;46m","\033[0;37m")