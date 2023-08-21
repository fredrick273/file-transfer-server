import socket
import os

folder = "server_folder"
print("The server ip is",socket.gethostbyname(socket.gethostname()))

HOST = socket.gethostname()

PORT = 6060

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen()

print("Listening for connections...")

folder_location = os.getcwd()+"\\"+folder
os.chdir(folder_location)

def change_dir(conn):
    directory = os.listdir()
    print(directory)
    dirstr = ""
    for i in directory:
        dirstr = dirstr + "\n" + i

    if len(dirstr)>0:
        conn.send(dirstr.encode())
    else:
        conn.send("No files found".encode())
    print("Sent contents of dir")

def download(client):
    fname = client.recv(1024).decode()
    try:
        with open(fname, "rb") as f:
            data = f.read(1024)
            while data:
                client.send(data)
                data = f.read(1024)
    except FileNotFoundError:
        client.send(b'File not found')
    finally:
        # Send the "END_OF_FILE" marker to indicate the end of the file transfer
        client.send(b'END_OF_FILE')
    print("File sent")



def upload(client):
    fname = client.recv(1024).decode()
    fsize = int(client.recv(1024).decode())
    print(f"Receiving {fname} of size {fsize} from client")

    with open(fname, "wb") as f:
        while True:
            data = client.recv(1024)
            if not data:
                break
            if data.endswith(b'END_OF_FILE'):
                f.write(data[:-len(b'END_OF_FILE')])
                break
            else:
                f.write(data)

    print("File received successfully")


def delete(client):
    fname = client.recv(1024).decode()
    os.remove(fname)
    client.send("File deleted".encode())
    print("File removed")

while (1):
    conn , addr = server.accept()
    print(f"Connection received from {addr}")
    while (1):
        #directory = os.getcwd()
        conn.send((socket.gethostname()+f"\\{folder}>").encode())
        choice = conn.recv(1024).decode()
        if choice.startswith("dir"):
            change_dir(conn)
        elif choice == "download":

            download(conn)
        elif choice == "delete":
            delete(conn)
        elif choice == "upload":
            upload(conn)
        elif choice == "help":
            continue
        elif choice == "exit":
            break
    
    conn.close()
    print("Connection closed")
    break
