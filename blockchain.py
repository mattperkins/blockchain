# Initialise *blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) <1:
        return None
    return blockchain[-1]

# This function accepts two args
# One required (transaction_amount) and one *optional (last_transaction)
# *optional because it has a default value of 1
def add_value(transaction_amount, last_transaction=[1]):
    """ Append the new and last value to the blockchain

        Arguments:
            :transaction_amount: The amount that should be added
            :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    # Capture and transform input data from a string to a float and store it in user_input
    user_input = float(input('Enter your transaction amount: '))
    return user_input


def get_user_choice():
    user_input = input("Your choice...")
    return user_input


def print_blockchain_elements():
    # Output blockchain list to console
    for block in blockchain:
        print('Outputting block')
        print(block)
 

# Get the first transaction input and add the value to the *blockchain list
tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print('Please choose:')
    print("1. Add a new transaction value")
    print("2. Output the blockchain blocks")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please choose an option from the menu')
    print('Choice registered')
    
print('Done!')
