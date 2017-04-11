import argparse
import hashlib

def md5(path):
    with open(path, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
def sha1(path):
    with open(path, 'rb') as f:
        m = hashlib.sha1()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
def sha256(path):
    with open(path, 'rb') as f:
        m = hashlib.sha256()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
def sha512(path):
    with open(path, 'rb') as f:
        m = hashlib.sha512()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
def main():

    parser = argparse.ArgumentParser(description = 'To do checksum on files')
    parser.add_argument('path', type=str, help='The file to check')
    parser.add_argument('--md5',help='Calculate md5 of file', action='store_true')
    parser.add_argument('--sha1', help='Calculate sha1 of file', action='store_true')
    parser.add_argument('--sha256', help='Calculate sha256 of file', action='store_true')
    parser.add_argument('--sha512', help='Calculate sha512 of file', action='store_true')
    parser.add_argument('--all', help='Calculate all checksums', action='store_true')
    arguments=parser.parse_args()

    print('File chosen : ' + arguments.path)
    if(arguments.all):
        print('MD5 : ' + md5(arguments.path))
        print('SHA-1 : ' + sha1(arguments.path))
        print('SHA-256 : ' + sha256(arguments.path))
        print('SHA-512 : ' + sha512(arguments.path))
    if(arguments.md5):
        print('MD5 : ' + md5(arguments.path))
    if(arguments.sha1):
        print('SHA-1 : ' + sha1(arguments.path))
    if(arguments.sha256):
        print('SHA-256 : ' + sha256(arguments.path))
    if(arguments.sha512):
        print('SHA-512 : ' + sha512(arguments.path))
    if(not (arguments.md5 or arguments.sha1 or arguments.sha256 or arguments.sha512)):
        print('No option chosen, going with all')
        print('MD5 : ' + md5(arguments.path))
        print('SHA-1 : ' + sha1(arguments.path))
        print('SHA-256 : ' + sha256(arguments.path))
        print('SHA-512 : ' + sha512(arguments.path))
main()