
# File transfer server

This is a simple client-server file transfer application written in Python. It allows you to perform various file operations like uploading, downloading, and deleting files on the server using a command-line interface on the client side.

## Features

- **Directory Listing**: View the list of files in the server directory.
- **Upload Files**: Upload files from your local machine to the server.
- **Download Files**: Download files from the server to your local machine.
- **Delete Files**: Remove files from the server directory.

## Prerequisites

- Python 3.x
- The application uses Python's built-in socket library, so no additional packages are required.

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/client-server-file-transfer.git
```

2. Run the server script on the server machine.

```bash
python server.py
```

3. Run the client script on your local machine.

```bash
python client.py
```

4. Follow the on-screen instructions to perform file operations.

## Usage

### Server (`server.py`)

- The server listens on a specified port (default is 6060).
- By default, it serves files from a folder named `server_folder` in the same directory as the script. You can change this by modifying the `folder` variable in the script.
- The server provides directory listing, file download, file upload, and file deletion functionalities.

### Client (`client.py`)

- The client connects to the server by providing the server's IP address and port.
- It provides a menu-driven command-line interface with options for viewing the server directory, uploading files, downloading files, and deleting files.
- Files are transferred between the client and server in chunks for efficiency.

## Contributing

Contributions to this project are welcome! If you find any issues, have suggestions, or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

