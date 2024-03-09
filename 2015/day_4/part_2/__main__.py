import hashlib

def main():
    print(find_num_for_santa("ckczppom"))

def find_num_for_santa(cle_secrete, nb_zeros=6):
    num = 0
    while True:
        chain = f"{cle_secrete}{num}".encode()
        md5_hash = hashlib.md5(chain).hexdigest()
        if md5_hash.startswith("0" * nb_zeros):
            return num
        num += 1

if __name__ == "__main__":
    main()