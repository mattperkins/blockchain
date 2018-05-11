# Initialise *blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
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


def get_user_amount():
    """ Returns the input of the user (a new transaction amount) as a float """
    # Capture and transform input data from a string to a float and store it in user_input
    user_input = float(input('Enter your transaction amount: '))
    return user_input

# Get the first transaction input and add the value to the *blockchain list
tx_amount = get_user_amount()
add_value(tx_amount)

# Get the second transaction input and add the value to the *blockchain list
tx_amount = get_user_amount()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

# Get the third transaction input and add the value to the *blockchain list
tx_amount = get_user_amount()
add_value(tx_amount, get_last_blockchain_value())

# Output the blockchain list to the console
# print(blockchain)

for block in blockchain:
    print('Outputting block')
    print(block)

print('Done!')






