import sys
import binascii
import tarfile
import io

input_file = sys.stdin.read()
file_as_string = ''.join(input_file.split())
tar_bytes = binascii.unhexlify(file_as_string)

with io.BytesIO(tar_bytes) as tar_file:
    with tarfile.open(fileobj=tar_file, mode='r') as tar:
        total_size, file_count = 0, 0
        
        for member in tar.getmembers():
            if member.isfile():
                file_count += 1
                total_size += member.size
        
        print(total_size, file_count)
