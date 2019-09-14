#!/usr/bin/python3.xx
#code name : Khairul
try:
    import requests, os, re, optparse
except ImportError as err:
    print(err)
    
# ctrl + z for stop the program
os.system("clear")

class Colors(object):

    p='\033[0;35m'       # Purple
    c='\033[0;36m'         # Cyan
    w='\033[0;37m'      #white
    co='\033[0m'        #close

class Banner(Colors):

    print(f"""   
    ________ 
   /  _____/ 
  /   \  ___ 
  \    \_\  | {Colors.c}Transalate{Colors.co}
   \______  /
          \/ 
    """)

class Transalate(Banner):

    def __init__(self, frm, to, text):
        self.frm = frm
        self.to = to
        self.text = text

    def run(self):
        try:
            req = requests.get(f"https://translate.google.com/m?hl=id&sl={self.frm}&tl={self.to}&ie=UTF-8&prev=_m&q={self.text}", timeout=5.3).text
            # regular expresion
            result = re.findall(r'class="t0">(.*?)</div>', str(req))
            print(f"Result: {Colors.c}{result[0]}{Colors.co}")
        except ConnectionError as err:
            print(err)
        except requests.Timeout as err:
            print(err)
        except Exception as err:
            print(err)





#Calling function
if __name__ == "__main__":
    while(True):
        frm = input("[*]From: ")
        to = input('[*]To: ')
        text = input("[*]Text: ")
        Transalate(frm, to, text).run()
        