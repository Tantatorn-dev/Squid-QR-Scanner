from modules.scanner import scan_qr
from time import sleep

def main():
    
    control_flag = True
    print("Welcome to Squid Payment System!")
    
    while control_flag: 
        output = scan_qr()
        print(output)
        sleep(1)
    

if __name__ == "__main__":
    main()
