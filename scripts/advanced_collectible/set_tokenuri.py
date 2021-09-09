from brownie import AdvancedCollectible, network, config, accounts
from scripts.helpful_scripts import get_breed

dog_metadata_dic = {
    "PUG": "https://ipfs.io/ipfs/QmbheuxcuoyoKmqnRdvHwu2S1Djv3RJJgL92txk4mZN2zU?filename=pug.png",
    "SHIBA-INU":"https://ipfs.io/ipfs/QmXCJeWagqwphvXDJ7JTt85hF4wzm43fFNcKZtLFoZAUtJ?filename=shiba-inu.png",
    "ST-BERNARD":"https://ipfs.io/ipfs/Qmb3gkX5ErZiT8hhsoxy2GRgdnzUo8NtFCYupHvUvhcr5a?filename=st-bernard.png"
}

OPENSEA_FORMAT = "https://testnets.opensea.io/assets/{}/{}"

def main():
    print("Working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(
        "The number of tokens you've deployed is: "
        + str(number_of_advanced_collectibles)
    )
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print("Setting tokenURI of {}".format(token_id))
            set_tokenURI(token_id, advanced_collectible,
                         dog_metadata_dic[breed])
        else:
            print("Skipping {}, we already set that tokenURI!".format(token_id))


def set_tokenURI(token_id, nft_contract, tokenURI):
    dev = accounts.add(config["wallets"]["from_key"])
    nft_contract.setTokenURI(token_id, tokenURI, {"from": dev})
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(nft_contract.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')