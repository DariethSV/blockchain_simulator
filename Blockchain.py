class Blockchain:

    def __init__(self, genesis_block):
        self.chain = [genesis_block]
    
    def get_chain(self):
        return self.chain

    def add_block(self, new_block):
        self.chain.append(new_block)

    def get_last_added_block(self):
        return self.chain[-1]
    
    def verify_chain(self):
        invalid_block_index = self.get_index_invalid_block()
        if invalid_block_index:
            print(f'The Blockchain is broken at the {invalid_block_index} position. \n Details: \n Correct Hash: {self.chain[invalid_block_index+1].get_previous_block_hash().hex()} \n______________________________________________________\n{self.chain[invalid_block_index]}')
            return False
        else:
            print(f'The Blockchain was verified succesfully.')
            return True
        
    def get_index_invalid_block(self):
        for i in range(len(self.chain)-1):
            if self.chain[i+1].previous_block_hash != self.chain[i].block_hash:
                return i
        else:
            return None

    def read_block(self, hash_bytes):
        for block in self.chain:
            if block.block_hash == hash_bytes:
                return block
        else:
            print(f'The block with the hash {hash_bytes} was not found')
            return None
    

    def modify_block(self, hash, attribute, value):

        block = self.read_block(hash)
        if not block:
            return block
        
        setattr(block,attribute,value)
        self.recalculate_block_hash(block)
        
        print(f'The block {hash} was modified. \n {block}')

    def recalculate_block_hash(self,block):
        block.set_block_hash(block.generate_hash())
        
    def erase_blocks(self):
        if self.verify_chain():
            return False
        print("______________________________________________________\n")
        invalid_block_index = self.get_index_invalid_block()
        print(f'The next blocks will be erased:\n')
        for block in self.chain[invalid_block_index:]:
            print(f'{block}\n______________________________________________________\n')

        self.chain=self.chain[:invalid_block_index]
        return True

    def __str__(self):
        blockchain_string = ""
        for block in self.get_chain():
            blockchain_string += str(block) + "\n______________________________________________________\n"
        return blockchain_string
