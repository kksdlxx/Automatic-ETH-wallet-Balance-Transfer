# ERC721 Transfer Functionality

# ABI definition
ERC721_ABI = [
    {"constant": true, "inputs": [{"name": "owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "to", "type": "address"}, {"name": "tokenId", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [{"name": "tokenId", "type": "uint256"}], "name": "ownerOf", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"},
]

from web3 import Web3

class ERC721:
    def __init__(self, contract_address):
        self.web3 = Web3(Web3.HTTPProvider('https://your.ethereum.node'))
        self.contract = self.web3.eth.contract(address=contract_address, abi=ERC721_ABI)

    def balance_of(self, owner):
        """Check the balance of the specified owner."""
        return self.contract.functions.balanceOf(owner).call()

    def transfer(self, from_address, to_address, token_id, private_key):
        """Transfer ownership of a specific NFT."
        nonce = self.web3.eth.getTransactionCount(from_address)
        txn = self.contract.functions.transferFrom(from_address, to_address, token_id).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })
        signed_txn = self.web3.eth.account.signTransaction(txn, private_key)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return self.web3.toHex(txn_hash)

    def owner_of(self, token_id):
        """Get the owner of a specific NFT."""
        return self.contract.functions.ownerOf(token_id).call()

# Example usage:
# erc721 = ERC721('0xYourContractAddress')
# balance = erc721.balance_of('0xOwnerAddress')
# transfer_txn = erc721.transfer('0xFromAddress', '0xToAddress', token_id, 'private_key')
# owner = erc721.owner_of(token_id)
