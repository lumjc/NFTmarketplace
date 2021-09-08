# deploy to rinkby testnet chain
from brownie import AdvancedCollectible, accounts, network, config
from scripts.helpful_scripts import fund_advanced_collectible

def main():
    # added a metamask account
   dev = accounts.add(config["wallets"]["from_key"])
   publish_source = False
   advanced_collectible = AdvancedCollectible.deploy(
       config['networks'][network.show_active()]['vrf_coordinator'],
       config['networks'][network.show_active()]['link_token'],
       config['networks'][network.show_active()]['keyhash'],
    #    deploying from my metamask address
       {"from": dev},
       publish_source=publish_source
   )
   fund_advanced_collectible(advanced_collectible)
   return advanced_collectible