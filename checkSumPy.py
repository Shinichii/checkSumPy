import argparse
import sys
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
def main():
    if(len(sys.argv) != 2): #Verification qu'un path est transmis
        print('Utilisation : python checksumPy.py path')
        sys.exit(0)
    parser = argparse.ArgumentParser(description = 'To do checksum on files')
    parser.add_argument('path', type=str, help='The file to check')
    parser.add_argument('--algo',type=str, help='To indicate what algorithm to use')
    arguments=parser.parse_args()
    print(arguments.path)
    answer = md5(arguments.path)
    print('Result : ' + answer)
main()