import socket
from tkinter import *

def init_gui(server_address):
    root = Tk()

    label_text = 'starting up on {} port {}'.format(*server_address)
    w = Label(root, text=label_text)
    w.pack()

    w.mainloop()

def main():
    server_address = ('10.204.56.155', 10000)
    init_gui(server_address)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)


    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))

                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break

        finally:
            # Clean up the connection
            connection.close()


if __name__ == "__main__":
    main()