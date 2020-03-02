#!/usr/bin/env python
# -*- enconding:utf-8 -*-
# @Author: xsmile
# @Time: 2020/2/20 17:44
import time

import web3
from web3 import Web3


def connectNode():
    # 连接本地以太坊节点
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545', request_kwargs={'timeout': 60}))
    # 输出当前账户
    print(w3.eth.accounts, type(w3.eth.accounts))
    users = w3.eth.accounts
    # 打印第二、三个账户余额
    print('user2:{}, user3:{}'.format(w3.fromWei(w3.eth.getBalance(users[1]), 'ether'),
                                      w3.fromWei(w3.eth.getBalance(users[2]), 'ether')))
    # 解锁第二个账户，即汇款人账户，参数为 账户地址、私钥，解锁时长（s）
    w3.geth.personal.unlockAccount(users[1], 'xsmile', 60)
    # 发生交易，即第二个账户向第三个账户转账 10 个以太币
    transAction = w3.eth.sendTransaction({"from": users[1], "to": users[2], "value":w3.toWei(10, 'ether')})
    print(transAction)
    # 开始挖矿
    w3.geth.miner.start(1)
    time.sleep(10)
    # 停止挖矿
    w3.geth.miner.stop()
    # 查看第二第三账户余额
    print('user2:{}, user3:{}'.format(w3.fromWei(w3.eth.getBalance(users[1]), 'ether'),
                                      w3.fromWei(w3.eth.getBalance(users[2]), 'ether')))
    # web3.Web3.geth.shh()
    pass


if __name__ == "__main__":
    print(web3.__version__)
    connectNode()
    pass