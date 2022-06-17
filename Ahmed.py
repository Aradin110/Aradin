import os,time,requests,subprocess

logo="""
\033[1;32m███    ███  ██████  ██   ██ ███████ ██ ███    ██ 
\033[1;33m████  ████ ██    ██ ██   ██ ██      ██ ████   ██ 
\033[1;34m██ ████ ██ ██    ██ ███████ ███████ ██ ██ ██  ██ 
\033[1;35m██  ██  ██ ██    ██ ██   ██      ██ ██ ██  ██ ██ 
\033[1;36m██      ██  ██████  ██   ██ ███████ ██ ██   ██
••••••••••••••••••••••••••••••••••••••••••••••••••••••
              \033[1;32m Mohsin Badshah
              \033[1;33m Faisalabadi Coder
              \033[1;36m Student Of Ahmad
••••••••••••••••••••••••••••••••••••••••••••••••••••••"""
def Subscription():
			os.system('clear')
			print(logo)
			print("\033[1;0m\033[1;37m[✓]•••••••••••••••••••••••••••••••••••••••••••")
			print("\033[1;32m[1] File Cloning\n\033[1;33m[2] Create File   (Super Fire)\n\033[1;36m[3] WhatsApp Group\n\033[1;36m[0]\033[1;91m Exit Programming");print("\033[1;37m[✓]•••••••••••••••••••••••••••••••••••••••••••");key = input("[•]\033[1;32m Choose Option\033[1;37m : \033[1;37m")
			if key in [""]:
				print(" (!) Please Select Correct Option")
				exit()
			elif key in ["1", "01"]:
				mk185.__chigoue__().chi(id)
			elif key in ["2","02"]:
				_login()
			elif key in ["3","0","00","E","e"]:
				print('\033[1;9m[>] Thank You ❤ ')
				exit()
			else:
				print('[×] Choose Correct Option');time.sleep(1);MrAking()
if __name__=='__main__':
	Subscription()