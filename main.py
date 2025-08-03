from Blockchain import Blockchain
from Block import Block
from Consensus import Consensus

def main():
    counter = 1
    genesis_block = Block("Genesis Block", b'\x00'*32,0)
    blockchain = Blockchain(genesis_block)
    consensus = Consensus(20)
    atributes = {1:"information",2:"nonce",3:"timestamp",4:"difficulty"}

    while(True):
        print(f'                    Menu                    ')
        print(f'Choose one of the following options')
        print(f'1. Add a Block')
        print(f'2. Read a Block')
        print(f'3. Erase Blocks')
        print(f'4. Modify Block')
        print(f'5. Show Blockchain')
        print(f'6. Verify Blockchain')
        print(f'7. Exit')
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            random_information = "Test "+ str(counter)
            previous_block_hash = blockchain.get_last_added_block().block_hash
            counter += 1
            new_block = Block(random_information,previous_block_hash,consensus.difficulty)
            time_to_pass_the_proof = consensus.proof_of_work(new_block)
            consensus.balance(time_to_pass_the_proof)
            blockchain.add_block(new_block)
            print(f'--------- New Block was added ---------\nTime to pass the proof: {time_to_pass_the_proof}\nDetails:\n{new_block}')


        elif option == 2:

            block_hash_to_be_read = input(f'Enter the hexadecimal hash of the block you want to read: ')
            try:
                hash_bytes = bytes.fromhex(block_hash_to_be_read)
                read_block =blockchain.read_block(hash_bytes)
                if read_block is not None:
                    print(read_block)
            except ValueError:
                print("Invalid hash format.")

            

        elif option == 3:

            if blockchain.erase_blocks():
                print(f'------------ Blocks were erased succesfully ------------')
            else:
                print(f'------------The Blockchain does not have any mistakes------------')


        elif option == 4:

            hash_to_be_modified = input(f'Enter the hexadecimal hash of the block you want to modify: ')
            try:
                hash_bytes_to_be_modifed = bytes.fromhex(hash_to_be_modified)
            except ValueError:
                print("Invalid hash format.")

            try:
                atribute_to_be_modified = int(input(f'Enter the atribute number of the block you want to modify: \n1. Information\n2. Nonce\n3. Timestamp\n4. Difficulty\n'))

            except ValueError:
                atribute_to_be_modified = 0
                print(f'Invalid value for the option. It must be an integer.')

            while(atribute_to_be_modified<1 or atribute_to_be_modified>4):
                atribute_to_be_modified = int(input(f'Invalid answer, try again: '))

            
            if atribute_to_be_modified == 2 or atribute_to_be_modified == 4:
                try:
                    value_of_the_atribute = int(input(f'Enter the new value of the atribute: '))
                except ValueError:
                    print(f'Invalid value for difficulty or Nonce. It must be an integer.')
            else: 
                value_of_the_atribute = input(f'Enter the new value of the atribute: ')
                
            blockchain.modify_block(hash_bytes_to_be_modifed,atributes[atribute_to_be_modified],value_of_the_atribute)
        elif option==5:
            print(blockchain)
        elif option==6:
            blockchain.verify_chain() 
        elif option==7:

            break

        else:
            print(f'Invalid option, try again...')


if __name__ == "__main__":
    main()



