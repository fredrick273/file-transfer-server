import socket
import os

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
    fname = os.path.basename(fpath)
    file_size = os.path.getsize(fpath)
    client.send(fname.encode())
    client.send(str(file_size).encode())

    with open(fpath, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client.send(data)
        # Send the "END_OF_FILE" marker to signal the end of the file
        client.send(b'END_OF_FILE')
    
    print("The file has been uploaded")

def download(client):
    fname = input("Enter a file name which is present in the dir: ")
    client.send(fname.encode())
    data = b''
    while True:
        chunk = client.recv(1024)
        if chunk.endswith(b'END_OF_FILE'):
            data += chunk[:-len(b'END_OF_FILE')]
            break
        data += chunk
    if data.decode() == "File not found":
        print("File not found on the server.")
    else:
        with open(fname, "wb") as f:
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

