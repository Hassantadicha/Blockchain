from hashlib import sha256

x = 5
y = 0 # we do not know what y should be yet
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0": y+1

print(f'The solution is y = {y})
      
      
      #implementin proof of work
      
 import hashlib
import json

from time import time
from uuid import uuid4

class BlockChain(object):
    ...
    def proof_of_work(self, last_proof):
        # simple proof of work algorithm
        # find a number p' such as hash(pp') containing leading 4 zeros where p is the previous p'
        # p is the previous proof and p' is the new proof
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    @staticmethod
    def validate_proof(last_proof, proof):
        # validates the proof: does hash(last_proof, proof) contain 4 leading zeroes?
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
