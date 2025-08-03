import time

class Consensus:
    def __init__(self,difficulty):
        self.difficulty = difficulty

    def set_difficulty(self,new_difficulty):
        self.difficulty = new_difficulty
    
    def get_difficulty(self):
        return self.difficulty
    
    def proof_of_work(self,block):
        start_time = time.time()
            
        while(not self.is_valid(block)):
            block.set_nonce()
            block.set_block_hash(block.generate_hash())
        end_time = time.time()
        time_to_pass_the_proof = end_time - start_time
        return time_to_pass_the_proof
    
    def is_valid(self, block):
        block_hash = block.get_block_hash()
        bytes_to_compare =block.get_block_difficulty() // 8 # Bytes which are fully zeros
        additional_bits_to_compare = block.get_block_difficulty() % 8

        for i in range(bytes_to_compare):
            if block_hash[i] != 0:
                return False
        
        if additional_bits_to_compare != 0:
            next_byte = block_hash[bytes_to_compare]
            mask = 0xFF << (8 - additional_bits_to_compare) & 0xFF

            if (next_byte & mask) != 0:
                return False

        return True
        
    def balance(self, time):
        if time > 15 and self.difficulty > 1:
            self.difficulty -= 1
        elif time < 15:
            self.difficulty +=1

