import socket  # noqa: F401
from uuid import uuid4
import ctypes


def to_int32(val: int):
    return val.to_bytes(length=4, byteorder="big", signed=False)

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept() # wait for client

    corelation_id = to_int32(7)
    print(f"Corelation ID: {corelation_id}")
    message_size = to_int32(7)
    message = bytearray(message_size)
    message.extend(corelation_id)
    print(f"Message: {message}")
    connection.sendall(message)


if __name__ == "__main__":
    main()
