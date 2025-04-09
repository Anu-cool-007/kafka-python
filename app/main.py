import socket  # noqa: F401
from uuid import uuid4

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept() # wait for client

    corelation_id = str(uuid4().int & (1<<32)-1)
    message_size = len(corelation_id)
    message = f"{message_size}\r\n{corelation_id}"
    connection.sendall(message.encode())


if __name__ == "__main__":
    main()
