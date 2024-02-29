import sys ,os
from cryptography.fernet import Fernet
from colorama import Fore as color
#NOTE => kindely set $PATH as per your system in line 26

def print_Logo():
    print('\x1b[37;36m                        Script [ KESHAV RAJ ]             \x1b[37;36m')
    print('\x1b[37;0m')
    print('\t\t\t+-------------------------------------------------------------------------+ ')
    print('\t\t\t|  _ __ ___   __ _  __| | ___   | |__  _   _     | | / /      | |]]|]     | ')
    print("\t\t\t| | '_ ` _ \ / _` |/ _` |/ _ \  | '_ \| | | |    | |/ /       | | - |     |")
    print('\t\t\t| | | | | | | (_| | (_| |  __/  | |_) | |_| |    | | /   ===  | |___|     | ')
    print('\t\t\t| |_| |_| |_|\__,_|\__,_|\___|  |_.__/ \__, |    | |\ \       | |\ \      | ')
    print('\t\t\t|                                      |___/     |_| \_\      |_| \_\     |')
    print('\t\t\t+-------------------------------------------------------------------------+ ')
    print('\x1b[37;0m')
 
def option():
    print(color.CYAN,f'''
* Press [{color.GREEN}1{color.CYAN}] for encrypt message.
* Press [{color.GREEN}2{color.CYAN}] for decrypt message.
* Press [{color.YELLOW}3{color.CYAN}] for en-decrypt message from {color.WHITE}(*.txt){color.CYAN} file.
* Press [{color.RED}4{color.CYAN}] for exit.
          ''',color.WHITE)

def message_encryption(val,message,key=None,PATH='/home/blackshark/Desktop/mess.txt'): # val 1 for encrypt and 2 for de-crypt
    if val == 1:
        new_key = Fernet.generate_key()
        fernet = Fernet(new_key)
        encrpt_messhage = fernet.encrypt(message.encode())
        with open (PATH,'w') as f:
            f.write('KEY => ' + str(new_key) + '\nMESSAGE => ' + str(encrpt_messhage))
        return { # here return type is dict
            'key':new_key,
            'message':encrpt_messhage
        }
    elif val==2:
        try :
            fernet = Fernet(key)
            decrpt_messhage = fernet.decrypt(message).decode()
            return str(decrpt_messhage)
        except Exception as e:
            return f'{color.MAGENTA} *└─> Not A Valid Key Or Message *.{color.WHITE}'
        

if __name__=='__main__':
    print_Logo()
    option()
    choise = int(input('└─>'))
    final_result = None
    match choise:
        case 1:
            print('\t \t \t ) MESSAGE ENCRYPT BOX (\n')
            message = input(f'{color.GREEN} └─ {color.YELLOW}')
            final_result=message_encryption(val=1,message=message)
            pass
        
        case 2:
            print('\t \t \t ) MESSAGE DECRYPT BOX (\n')
            key = input(f'{color.RED} Key└─ {color.RED}')
            message = input(f'{color.GREEN} \tEncrypted-Mess└─ {color.YELLOW}')
            final_result=message_encryption(val=2,message=message,key=key)
            pass
        
        case 3:
            os.system('clear')
            print(color.GREEN,'''
* Press 1 for en-crypt.
* Press 2 for de-crypt.
* Press else for exit.
                  ''',color.WHITE)
            choise = (input('└─>'))
            try :
                choise = int(choise)
            except:
                print(color.RED,'Scrpit exited.')
                sys.exit()
                
            if choise==1:
                print('\t \t \t ) MESSAGE ENCRYPT BOX FROM FILE (\n')
                file = input('Swipe or Enter Path Of File \n   └─>')
                file = file.replace("'","")
                text = None
                with open(file,'r') as f:
                    text=f.read()
                final_result=message_encryption(val=1,message=text) 
                
            elif choise==2:
                print('\t \t \t ) MESSAGE DECRYPT BOX FROM FILE (\n')
                key = input('KEY -> ')
                file = input('Swipe or Enter Path Of File \n   └─>')
                file = file.replace("'","")
                text = None
                with open(file,'r') as f:
                    text=f.read()
                final_result=message_encryption(val=2,message=text,key=key)

            else:
                print('Wrong input')
                exit(0)
            pass
        
        case 4:
            try:
                sys.exit()
            finally:
                print(color.RED,'Scrpit exited.')
    final_result = str(final_result)
    final_result = final_result.replace(',','\n')
    print('\n' ,color.RED, final_result)
    pass
