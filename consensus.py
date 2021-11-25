import requests
...
class BlockChain(object):
    ...
    def valid_chain(self, chain):
        
        # determine if a given blockchain is valid
        last_block = chain[0]
        current_index = 1
        
        while current_index < len(chain):
            block = chain[current_index]
            # check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block)
                return False
            # check that the proof of work is correct
            if not self.valid_proof(last_block['proof'], block['proof'])
                return False
        
            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        # this is our Consensus Algorithm, it resolves conflicts by replacing
        # our chain with the longest one in the network.

        neighbours = self.nodes
        new_chain = None

        # we are only looking for the chains longer than ours
        max_length = len(self.chain)

        # grab and verify chains from all the nodes in our network
        for node in neighbours:

            # we utilize our own api to construct the list of chains :)
            response = request.get(f'http://{node}/chain')

            if response.status_code == 200:

                length = response.json()['length']
                chain = response.json()['chain']
                
                # check if the chain is longer and whether the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain
        
        # replace our chain if we discover a new longer valid chain
        if new_chain:
            self.chain = new_chain
            return True

        return False
