import hashlib
import string
import random
import pprint

def generate_passwords():
    length = 6
    num_passwords = 1000000

    chars = string.ascii_letters + string.digits
    passwords = {}
    while len(passwords) < num_passwords:
        password = ''.join(random.choices(chars, k=length))
        hashed_password = hashing(password)
        reduced_hash = chain_len(hashed_password, 10)
        passwords[password] = reduced_hash
    return passwords


def hashing(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def reduction(hashed_password, output_length=8):
    hashed_password_bytes = bytes.fromhex(hashed_password)
    least_significant_bytes = hashed_password_bytes[-8:]
    integer_value = int.from_bytes(least_significant_bytes, byteorder='big')
    output = hex(integer_value)[2:]
    if len(output) > output_length:
        output = output[:output_length]
    return output


def chain_len(input_string, num_repetitions):
    if num_repetitions == 0:
        return input_string
    else:
        reduced_hash = reduction(input_string)
        return chain_len(reduced_hash, num_repetitions-1)


def reduce_hash(hash):
    reduced_hash = reduction(hash)
    return reduced_hash


password_dict = generate_passwords()

pprint.pprint(password_dict)


with open("data.txt", "w") as file:
    for password, reduced_hash in password_dict.items():
        hashed_password = hashing(password)
        file.write(f"{password} : {reduced_hash} : {hashed_password}\n")

while True:
    
    hash_input = input("Enter the hash (type 'exit' to quit): ")
    if hash_input == "exit":
        break
    reduced_hash = chain_len(hash_input, 10)
    print("The reduced hash is:", reduced_hash)

    match_found = False
    for password, r_hash in password_dict.items():
        if r_hash == reduced_hash:
            print(f"Match found: Password for hash: {password}")
            match_found = True
            break
    if not match_found:
        print(f"No match found for hash {hash_input}")
