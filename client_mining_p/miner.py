import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(last_proof):
    print("Starting work on a new proof...")
    proof = 0
    # for block 1, hast (1, p) = 000000x
    while vaild_proof(last_proof, proof) is False:
        proof += 1
    print("Attempting to mine...")
    return proof

def valid_proof(last_proof, proof):
    # build string to hash
    guess = f'{last_proof}{proof}'.encode()
    # use hash function
    guess_hash = hashlib.sha256(guess).hexdigest()
    # check if 6 leading 0's in hash result
    beg = guess_hash[0:6]
    if beg == "000000":
        return True
    else:
        return False

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        
        new_proof =  Proof_of_work(last_proof)

        proof_data = {'proof': new_proof}
        r = requests.post(url = node + '/mine', json = proof_data)
        data = r.json()

        if data.get('message') == "New Block Forged":
            coins_mined += 1
            print("You have: " + str(coins_mined) + " coins")
        print(data.get('message'))
