blockchain = [[1]]

def add_value(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)

add_value(14.3)
add_value(2.125)
add_value(19.55)