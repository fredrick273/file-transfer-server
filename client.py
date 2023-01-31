import socket
import os

#HOST = "10.4.241.100"
HOST = input("Enter the server ip:")
PORT = 6060

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((HOST,PORT))

print(f"Connected to {HOST}")

help_text = """dir = Display the files present in the directory
upload = Upload files to server
download  = Download file from server
help = Display this msg
exit = Close the connection
"""

def getdir(client):
    directory = client.recv(1024).decode()
    print(directory)
    print("\n")

def upload(client):
    fpath = input("Enter the file path:")
    fname = (fpath.split("\\")[-1])
    file_size = os.path.getsize(fpath)
    client.send(fname.encode())
    # progress = tqdm.tqdm(range(file_size),f"Sending {fname}", unit="8", unit_scale=True, unit_divisor=1024)
    with open(fpath, "r") as f:

        data = f.read()
    client.send(data.encode())
    
    print("The file has been uploaded")
    #       progress.update(len(bytes_read))

def download(client):
    fname = input("Enter a file name which is present in the dir: ")
    client.send(fname.encode())
    file_size = client.recv(1024).decode()
    print(f"The file is of {file_size} and is downloading")
    data = client.recv(8075).decode()
    with open(fname, "w") as f:
        f.write(data)
    print("The file has been downloaded")


def deletefile(client):
    fname = input("Enter the file name to be deleted: ")
    client.send(fname.encode())
    print(client.recv(1024).decode())
    

while (1):
    
    directory = client.recv(1024).decode()
    choice = input(f"{directory}: ")
    client.send(choice.encode())
    if choice == "dir":
        getdir(client)
    elif choice == "upload":
        upload(client)
    elif choice == "download":
        download(client)
    elif choice == "delete":
        deletefile(client)
    elif choice == "help":
        print("\n",help_text,sep="")
    elif choice == "exit":
        print("Exiting....")
        client.close()
        break

