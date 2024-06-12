#!/usr/bin/python3
import struct

def read_8byte_integers_from_file(file_path):
    integers = []
    with open(file_path, 'rb') as file:
        data = file.read(8) # Size.
        bytes_a = bytearray()
        bytes_a.extend(struct.pack('Q', 90437011)) # NUMBER OF UNIQUE KEYS
        print("Bytes Data", struct.pack('Q', 90437011))
        prev = -1
        count = 0
        while True:
            # Read 8 bytes from the file
            data = file.read(8)
            if not data:
                break  # End of file
            # Unpack bytes into an integer using struct
            integer = struct.unpack('Q', data)[0]  # 'q' stands for 8-byte integer
            if integer == prev:
                continue
            prev = integer
            count = count + 1
            bytes_a.extend(data)
    print(count)
    return bytes_a

def write_bytes_to_file(byte_data, file_path):
    with open(file_path, 'wb') as file:
        file.write(byte_data)


file_path = './data/wiki_ts_200M_uint64'  # Update this with your file path
byte_data = read_8byte_integers_from_file(file_path)
write_bytes_to_file(bytes(byte_data), './data/wiki_ts_200M_uint64')
