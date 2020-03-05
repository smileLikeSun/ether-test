#!/usr/bin/env python
# -*- enconding:utf-8 -*-
# @Author: xsmile
# @Time: 2020/3/3 14:09
import json
import time

from web3 import Web3
from solc import compile_standard

class EthInstance():

    def __init__(self, ip, rpcport):
        # 连接本地以太坊节点
        self.w3 = Web3(Web3.HTTPProvider('http://' + ip + ':' + rpcport, request_kwargs={'timeout': 60}))

    # 返回当前所有账户
    def getAddrs(self):
        return self.w3.eth.accounts

    # 返回指定地址的余额
    def getBalance(self, addr):
        balance = self.w3.fromWei(self.w3.eth.getBalance(addr), 'ether')
        return balance

    # 返回当前节点的 enode 信息
    def getEnode(self):
        return self.w3.geth.admin.node_info()['enode']

    # 返回当前节点数
    def peers(self):
        return self.w3.geth.admin.peers()

    # 当前节点添加节点
    def addPeer(self, enode):
        return self.w3.geth.admin.add_peer(enode)

    # 开始挖矿
    def minerStart(self):
        self.w3.geth.miner.start(1)

    # 结束挖矿
    def minerStop(self):
        self.w3.geth.miner.stop()


def connectNode(ins, ip, rpcport):
    print('ip：{}:{}节点信息：{}'.format(ip, rpcport, ins.getEnode()))
    addrs = ins.getAddrs()
    print('当前账户：{}'.format(addrs))
    for addr in addrs:
        print('{}账户余额(ether)：{}'.format(addr, ins.getBalance(addr)))

    print('****************************************')


def contractCompile(ins):
    compiledSol = compile_standard({
        'language': 'Solidity',
        'sources': {'UserInfo.sol': {
                        'content': '''
                            pragma solidity ^0.6.0;

                            contract UserInfo {
                                 string name;
                                 uint age;
                                 bool gender = true;
                                 constructor() public{
                                     name = 'junweiJun';
                                     age = 18;
                                     gender = true;
                                 }
                                 function setAttr(string memory _name, uint _age, bool _gender) public{
                                     name = _name;
                                     age = _age;
                                     gender = _gender;
                                 }
            
                                 function getAttr() public view returns (string memory, uint, bool) {
                                     return (name, age, gender);
                                 }
                             }
                        
                        '''
                    }
        },
        "settings":
            {
                "outputSelection": {
                    "*": {
                        "*": [
                            "metadata", "evm.bytecode"
                            , "evm.bytecode.sourceMap"
                        ]
                    }
                }
            }
    })
    # 设置默认账户
    # ins.w3.eth.coinbase = ins.getAddrs()[1]
    # 获取 bytecode
    bytecode = compiledSol['contracts']['UserInfo.sol']['UserInfo']['evm']['bytecode']['object']
    # 获取 abi
    abi = json.loads(compiledSol['contracts']['UserInfo.sol']['UserInfo']['metadata'])['output']['abi']

    # 生成合约
    UserInfo = ins.w3.eth.contract(abi=abi, bytecode=bytecode)
    # # 部署合约
    print(ins.w3.eth.defaultAccount)
    ins.w3.eth.defaultAccount = ins.getAddrs()[1]
    print(ins.w3.eth.defaultAccount)
    # 解锁账户
    ins.w3.geth.personal.unlockAccount(ins.getAddrs()[1], 'xsmile', 300)
    # 设置 defaultAccount 并解锁账户，否则会出现 ValueError: {'code': -32000, 'message': 'unknown account'}
    txHash = UserInfo.constructor().transact()
    ins.minerStart()
    # # 等待合约被挖掘
    txReceipt = ins.w3.eth.waitForTransactionReceipt(txHash)
    print('txReceipt:', txReceipt)
    ins.minerStop()
    userInfo = ins.w3.eth.contract(address=txReceipt.contractAddress, abi=abi)
    user = userInfo.functions.getAttr().call()
    print(user)
    pass


def run():
    ip = '127.0.0.1'
    rpcport1, rpcport2 = '8545', '9545'
    ins = EthInstance(ip, rpcport1)
    connectNode(ins, ip, rpcport1)
    contractCompile(ins)

    '''
    try:
        enode2 = ins2.getEnode().split('@')[0] + '@' + ip2 + ':30306'
        print('enode2:{}'.format(enode2))
        ins1.addPeer(enode2)
        print('启动挖矿！')
        ins1.minerStart()
        time.sleep(60)
        print('停止挖矿！')
        ins1.minerStop()
        if peers < len(ins1.peers()):
            print('try 挖矿成功！')
            print('增加节点{}'.format(ins1.peers()))
        else:
            print('try 失败！节点添加失败！')
    except Exception:
        pass
    '''


if __name__ == "__main__":
    run()
    pass
