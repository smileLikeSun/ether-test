#!/usr/bin/env python
# -*- enconding:utf-8 -*-
# @Author: xsmile
# @Time: 2020/3/3 13:40
import os


def start_node(db='D:/eth-test/db/', port='30303', rpcport='8545'):
    cmdOrder = 'geth --datadir ' + db + ' --rpc --rpcapi "eth,net,web3,personal,admin,txpool,debug,miner"' \
              ' --port ' + port + ' --rpcport ' + rpcport + ' --nodiscover --rpccorsdomain "*" --allow-insecure-unlock' \
              ' --ipcdisable'
    os.system(cmdOrder)


def run():
    port = '30306'
    rpcport = '9545'
    db = 'D:/eth-test/node1/'
    # start_node(db=db, port=port, rpcport=rpcport)
    start_node()


if __name__ == "__main__":
    run()

    pass
