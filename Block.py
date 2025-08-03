import hashlib
import time

class Block:
    def __init__(self,information, previous_block_hash, block_difficulty):
        self.information = information
        self.nonce = 0
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.previous_block_hash = previous_block_hash
        self.block_difficulty = block_difficulty
        self.block_hash = self.generate_hash()

    def generate_hash(self):
        data = f'{self.get_previous_block_hash()}{self.get_information()}{self.get_nonce()}{self.get_timestamp()}{self.get_block_difficulty()}'
        hash = hashlib.sha256(data.encode()).digest()
        return hash
    
    def set_nonce(self):
        self.nonce += 1
    
    def set_information(self,new_information):
        self.information = new_information

    def set_timestamp(self, new_timestamp):
        self.timestamp = new_timestamp
    
    def set_previous_block_hash(self, new_previous_block_hash):
        self.previous_block_hash = new_previous_block_hash

    def set_block_difficulty(self, new_block_difficulty):
        self.block_difficulty = new_block_difficulty

    def set_block_hash(self,new_hash):
        self.block_hash = new_hash

    def get_nonce(self):
        return self.nonce
    
    def get_information(self):
        return self.information

    def get_timestamp(self):
        return self.timestamp
    
    def get_previous_block_hash(self):
        return self.previous_block_hash

    def get_block_difficulty(self):
        return self.block_difficulty

    def get_block_hash(self):
        return self.block_hash
    
    def __str__(self):
        return f'Block Byte Hash: {self.block_hash}\nBlock Hexadecimal Hash: {self.block_hash.hex()}\nPrevious Block Hash: {self.previous_block_hash.hex()}\nInformation: {self.information}\nblock_Difficulty: {self.block_difficulty}\nTimestamp: {self.timestamp}\nNonce: {self.nonce}'