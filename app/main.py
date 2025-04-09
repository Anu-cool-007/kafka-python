import socket  # noqa: F401
from uuid import uuid4
import ctypes


def to_int32(val):
    val &= ((1<<32)-1)
    if val & (1<<31): val -= (1<<32)
    return val

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept() # wait for client

    corelation_id = str(ctypes.c_uint32(7).value)
    print(f"Corelation ID: {corelation_id}")
    message_size = len(corelation_id)
    message = f"{message_size}\r\n{corelation_id}"
    connection.sendall(message.encode())


if __name__ == "__main__":
    main()
