# Imports
import os
from dotenv import load_dotenv
from web3 import Web3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
from bip44 import Wallet
from web3 import Account
from web3.auto import w3

load_dotenv()



load_dotenv()

################################################################################
# Wallet functionality

from eth_account import Account
Account.enable_unaudited_hdwallet_features()

# Initialize the Web3 instance
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Fetch mnemonic from the environment variable.
    mnemonic = os.getenv("MNEMONIC")
    # Create a Wallet Object
    wallet = w3.eth.account.from_mnemonic(mnemonic)

    # Return the Ethereum account
    return wallet

def get_balance(w3, address):
    """Using an Ethereum account address, access the balance of Ether."""
    # Get the balance of the address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether using w3.fromWei
    ether_balance = w3.fromWei(wei_balance, 'ether')

    # Return the value in ether
    return ether_balance


def send_transaction(w3, account, to, wage):
    """Send an authorized transaction to the Ganache blockchain."""
    # Set the gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert the ETH amount to Wei
    value = w3.toWei(wage, "ether")

    # Calculate the gas estimate
    gas_estimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Set your desired maxFeePerGas value (e.g., 100 Gwei)
    max_fee_per_gas = w3.toWei(100, 'gwei')

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gas_estimate,
        "gasPrice": max_fee_per_gas,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

    # Sign the raw transaction with the Ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transaction
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    """Send an authorized transaction to the Ganache blockchain."""
    # Set the gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert the ETH amount to Wei
    value = w3.toWei(wage, "ether")

    # Calculate the gas estimate
    gas_estimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx ={
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gas_estimate,
         "gasPrice": max_fee_per_gas,  # Set your desired maxFeePerGas value
        "nonce": w3.eth.getTransactionCount(account.address),
    }

    # Sign the raw transaction with the Ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transaction
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
