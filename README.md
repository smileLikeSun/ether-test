# ether-test
初探以太坊，在服务器上经历了很长时间的失败，没有 mac ，转移到自己的 windows 上来，一切似乎变得简单起来

使用记录，以供参考。windows上面安装很简单就略过了。。。

## 初始化创世区块
{
  "config": {
    "chainId": 666,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip150Hash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "ethash": {}
  },
  "nonce": "0x0",
  "timestamp": "0x5ddf8f3e",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x47b760",
  "difficulty": "0x00002",
  "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": { },
  "number": "0x0",
  "gasUsed": "0x0",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
}
PS D:\eth-test> geth --datadir ".\db" init .\genesis.json                                                               INFO [03-02|17:47:24.159] Maximum peer count                       ETH=50 LES=0 total=50
INFO [03-02|17:47:24.360] Allocated cache and file handles         database=D:\\eth-test\\db\\geth\\chaindata cache=16.00MiB handles=16
INFO [03-02|17:47:24.388] Writing custom genesis block
INFO [03-02|17:47:24.392] Persisted trie from memory database      nodes=0 size=0.00B time=0s gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
INFO [03-02|17:47:24.419] Successfully wrote genesis state         database=chaindata                         hash=d3d6bb…c5304a
INFO [03-02|17:47:24.426] Allocated cache and file handles         database=D:\\eth-test\\db\\geth\\lightchaindata cache=16.00MiB handles=16
INFO [03-02|17:47:24.442] Writing custom genesis block
INFO [03-02|17:47:24.445] Persisted trie from memory database      nodes=0 size=0.00B time=0s gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
INFO [03-02|17:47:24.468] Successfully wrote genesis state         database=lightchaindata                         hash=d3d6bb…c5304a

## 启动节点
PS D:\eth-test> geth --datadir ./db/ --rpc --rpcapi "eth,net,web3,personal,admin,txpool,debug,miner" --nodiscover console --dev --dev.period 1 --allow-insecure-unlock                                                                          INFO [03-02|17:48:55.482] Maximum peer count                       ETH=50 LES=0 total=50
INFO [03-02|17:48:59.088] Using developer account                  address=0xdb11B7d7d6D52d01D169e497f290c9392dB1C4E5
INFO [03-02|17:48:59.104] Starting peer-to-peer node               instance=Geth/v1.9.11-stable-6a62fe39/windows-amd64/go1.13.8
INFO [03-02|17:48:59.112] Allocated trie memory caches             clean=256.00MiB dirty=256.00MiB
INFO [03-02|17:48:59.117] Allocated cache and file handles         database=D:\\eth-test\\db\\geth\\chaindata cache=512.00MiB handles=8192
INFO [03-02|17:48:59.191] Opened ancient database                  database=D:\\eth-test\\db\\geth\\chaindata\\ancient
INFO [03-02|17:48:59.199] Persisted trie from memory database      nodes=11 size=1.66KiB time=0s gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
Fatal: Error starting protocol stack: database contains incompatible genesis (have d3d6bb893a6e274cab241245d5df1274c58d664fbb1bfd6e59141c2e0bc5304a, new 831157ae460a95c033a5b91fce65f1cf7ed723a9f6895d74d28bdd1990d9988f)

PS D:\eth-test> geth --datadir ./db/ --rpc --rpcapi "eth,net,web3,personal,admin,txpool,debug,miner" --nodiscover console                                                                                                                       INFO [03-02|17:49:35.738] Bumping default cache on mainnet         provided=1024 updated=4096
WARN [03-02|17:49:35.757] Sanitizing cache to Go's GC limits       provided=4096 updated=2704
INFO [03-02|17:49:35.765] Maximum peer count                       ETH=50 LES=0 total=50
INFO [03-02|17:49:35.911] Starting peer-to-peer node               instance=Geth/v1.9.11-stable-6a62fe39/windows-amd64/go1.13.8
INFO [03-02|17:49:35.917] Allocated trie memory caches             clean=676.00MiB dirty=676.00MiB
INFO [03-02|17:49:35.923] Allocated cache and file handles         database=D:\\eth-test\\db\\geth\\chaindata cache=1.32GiB handles=8192
INFO [03-02|17:49:35.960] Opened ancient database                  database=D:\\eth-test\\db\\geth\\chaindata\\ancient
INFO [03-02|17:49:35.967] Initialised chain configuration          config="{ChainID: 666 Homestead: 0 DAO: <nil> DAOSupport: false EIP150: 0 EIP155: 0 EIP158: 0 Byzantium: 0 Constantinople: 0 Petersburg: 0 Istanbul: 0, Muir Glacier: <nil>, Engine: ethash}"
INFO [03-02|17:49:35.980] Disk storage enabled for ethash caches   dir=D:\\eth-test\\db\\geth\\ethash count=3
INFO [03-02|17:49:35.986] Disk storage enabled for ethash DAGs     dir=C:\\Users\\Administrator\\AppData\\Local\\Ethash count=2
INFO [03-02|17:49:35.994] Initialising Ethereum protocol           versions="[65 64 63]" network=1 dbversion=<nil>
WARN [03-02|17:49:36.001] Upgrade blockchain database version      from=<nil> to=7
INFO [03-02|17:49:36.007] Loaded most recent local header          number=0 hash=d3d6bb…c5304a td=2 age=3mo5d38m
INFO [03-02|17:49:36.014] Loaded most recent local full block      number=0 hash=d3d6bb…c5304a td=2 age=3mo5d38m
INFO [03-02|17:49:36.021] Loaded most recent local fast block      number=0 hash=d3d6bb…c5304a td=2 age=3mo5d38m
INFO [03-02|17:49:36.030] Regenerated local transaction journal    transactions=0 accounts=0
INFO [03-02|17:49:36.056] Allocated fast sync bloom                size=1.32GiB
INFO [03-02|17:49:36.060] Initialized fast sync bloom              items=0 errorrate=0.000 elapsed=0s
INFO [03-02|17:49:36.078] New local node record                    seq=1 id=6d017d8e59468ff8 ip=127.0.0.1 udp=0 tcp=30303
INFO [03-02|17:49:36.079] IPC endpoint opened                      url=\\\\.\\pipe\\geth.ipc
INFO [03-02|17:49:36.085] Started P2P networking                   self="enode://1f1c94a828eb5e9102845e4823489619ca67f347c4707712dc2c73e07e11fd6ea89d96d87ff8b04df6f99d9bd59d1f80b6b75b1db66814332a8a0612ca2e2fd0@127.0.0.1:30303?discport=0"
INFO [03-02|17:49:36.092] HTTP endpoint opened                     url=http://127.0.0.1:8545 cors= vhosts=localhost
INFO [03-02|17:49:36.144] Mapped network port                      proto=tcp extport=30303 intport=30303 interface=NAT-PMP(192.168.31.1)
INFO [03-02|17:49:36.187] Etherbase automatically configured       address=0xdb11B7d7d6D52d01D169e497f290c9392dB1C4E5
Welcome to the Geth JavaScript console!

instance: Geth/v1.9.11-stable-6a62fe39/windows-amd64/go1.13.8
coinbase: 0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5
at block: 0 (Thu Nov 28 2019 17:11:26 GMT+0800 (CST))
 datadir: D:\eth-test\db
 modules: admin:1.0 debug:1.0 eth:1.0 ethash:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0


 ## 创建新账户
 > eth.accounts
["0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5"]
> user1 = eth.accounts[0]
"0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5"
> eth.coinbase
"0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5"
> eth.getBalance(user1)
0
> personal.newAccount("xsmile")
INFO [03-02|17:52:02.621] Your new key was generated               address=0x5c51e3c26C0f67b3EEb2F4CabFc93AFB616e5849
WARN [03-02|17:52:02.626] Please backup your key file!             path=D:\\eth-test\\db\\keystore\\UTC--2020-03-02T09-52-00.518728700Z--5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849
WARN [03-02|17:52:02.635] Please remember your password!
"0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849"


## 设置挖矿奖励收益节点
> miner.setEtherbase("0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849")
true
> eth.coinbase
"0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849"
> eth.accounts
["0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5", "0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849"]

## 开始挖矿

> miner.start(1)
INFO [03-02|17:55:12.657] Updated mining threads                   threads=1
INFO [03-02|17:55:12.662] Transaction pool price threshold updated price=1000000000
nullINFO
[> 03-02|17:55:12.666] Commit new mining work                   number=1 sealhash=49a853…3269f6 uncles=0 txs=0 gas=0 fees=0 elapsed=0s
INFO [03-02|17:55:15.125] Generating DAG in progress               epoch=0 percentage=0 elapsed=1.663s
INFO [03-02|17:55:16.746] Generating DAG in progress               epoch=0 percentage=1 elapsed=3.284s
INFO [03-02|17:55:18.450] Generating DAG in progress               epoch=0 percentage=2 elapsed=4.988s
INFO [03-02|17:55:20.065] Generating DAG in progress               epoch=0 percentage=3 elapsed=6.603s
... ...
INFO [03-02|17:57:48.596] Generating DAG in progress               epoch=0 percentage=94 elapsed=2m35.134s
INFO [03-02|17:57:50.219] Generating DAG in progress               epoch=0 percentage=95 elapsed=2m36.757s
INFO [03-02|17:57:51.840] Generating DAG in progress               epoch=0 percentage=96 elapsed=2m38.378s
INFO [03-02|17:57:53.477] Generating DAG in progress               epoch=0 percentage=97 elapsed=2m40.015s
INFO [03-02|17:57:55.083] Generating DAG in progress               epoch=0 percentage=98 elapsed=2m41.621s
INFO [03-02|17:57:57.142] Generating DAG in progress               epoch=0 percentage=99 elapsed=2m43.679s
INFO [03-02|17:57:57.150] Generated ethash verification cache      epoch=0 elapsed=2m43.687s
INFO [03-02|17:58:04.001] Generating DAG in progress               epoch=1 percentage=0  elapsed=2.065s
INFO [03-02|17:58:06.062] Generating DAG in progress               epoch=1 percentage=1  elapsed=4.126s
INFO [03-02|17:58:08.067] Generating DAG in progress               epoch=1 percentage=2  elapsed=6.131s
INFO [03-02|17:58:09.358] Successfully sealed new block            number=1 sealhash=49a853…3269f6 hash=c31fdd…635b4d elapsed=2m56.692s
INFO [03-02|17:58:09.371] 🔨 mined potential block                  number=1 hash=c31fdd…635b4d
INFO [03-02|17:58:09.392] Commit new mining work                   number=2 sealhash=0863a0…77b45e uncles=0 txs=0 gas=0 fees=0 elapsed=16.000ms
INFO [03-02|17:58:10.123] Generating DAG in progress               epoch=1 percentage=3  elapsed=8.187s
INFO [03-02|17:58:12.219] Generating DAG in progress               epoch=1 percentage=4  elapsed=10.283s
INFO [03-02|17:58:14.281] Generating DAG in progress               epoch=1 percentage=5  elapsed=12.345s
INFO [03-02|17:58:16.372] Generating DAG in progress               epoch=1 percentage=6  elapsed=14.436s
INFO [03-02|17:58:17.536] Successfully sealed new block            number=2 sealhash=0863a0…77b45e hash=c3e0aa…8e21e5 elapsed=8.156s

> miner.stop()
null
> user2 = eth.accounts[1]
"0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849"
> eth.getBalance(user2)
170000000000000000000
> personal.newAccount("sophia")
INFO [03-02|18:06:47.829] Your new key was generated               address=0x9A55b9B0009B5b5E3e5B5e7B4d8db2134761dDF7
WARN [03-02|18:06:47.835] Please backup your key file!             path=D:\\eth-test\\db\\keystore\\UTC--2020-03-02T10-06-45.664686700Z--9a55b9b0009b5b5e3e5b5e7b4d8db2134761ddf7
WARN [03-02|18:06:47.844] Please remember your password!
"0x9a55b9b0009b5b5e3e5b5e7b4d8db2134761ddf7"

> web3.fromWei(eth.getBalance(user2), "ether")
170
> personal.unlockAccount(user2, "xsmile", 300)
WARN [03-02|18:16:08.507] Served personal_unlockAccount            reqid=26 t=2.0761ms err="account unlock with HTTP access is forbidden"
GoError: Error: account unlock with HTTP access is forbidden at web3.js:6347:37(47)
        at native
        at <eval>:1:41(5)


## 重启节点
PS D:\eth-test> geth --datadir ./db/ --rpc --rpcapi "eth,net,web3,personal,admin,txpool,debug,miner" --nodiscover console --allow-insecure-unlock                                                                                               INFO [03-02|21:22:00.645] Bumping default cache on mainnet         provided=1024 updated=4096
WARN [03-02|21:22:00.666] Sanitizing cache to Go's GC limits       provided=4096 updated=2704
INFO [03-02|21:22:00.675] Maximum peer count                       ETH=50 LES=0 total=50
INFO [03-02|21:22:00.819] Starting peer-to-peer node               instance=Geth/v1.9.11-stable-6a62fe39/windows-amd64/go1.13.8
INFO [03-02|21:22:00.830] Allocated trie memory caches             clean=676.00MiB dirty=676.00MiB
INFO [03-02|21:22:00.840] Allocated cache and file handles         database=D:\\eth-test\\db\\geth\\chaindata cache=1.32GiB handles=8192
INFO [03-02|21:22:01.167] Opened ancient database                  database=D:\\eth-test\\db\\geth\\chaindata\\ancient
INFO [03-02|21:22:01.173] Initialised chain configuration          config="{ChainID: 666 Homestead: 0 DAO: <nil> DAOSupport: false EIP150: 0 EIP155: 0 EIP158: 0 Byzantium: 0 Constantinople: 0 Petersburg: 0 Istanbul: 0, Muir Glacier: <nil>, Engine: ethash}"
INFO [03-02|21:22:01.187] Disk storage enabled for ethash caches   dir=D:\\eth-test\\db\\geth\\ethash count=3
INFO [03-02|21:22:01.193] Disk storage enabled for ethash DAGs     dir=C:\\Users\\Administrator\\AppData\\Local\\Ethash count=2
INFO [03-02|21:22:01.200] Initialising Ethereum protocol           versions="[65 64 63]" network=1 dbversion=7
INFO [03-02|21:22:01.211] Loaded most recent local header          number=153 hash=755289…7162e5 td=20315694 age=2m11s
INFO [03-02|21:22:01.217] Loaded most recent local full block      number=153 hash=755289…7162e5 td=20315694 age=2m11s
INFO [03-02|21:22:01.224] Loaded most recent local fast block      number=153 hash=755289…7162e5 td=20315694 age=2m11s
INFO [03-02|21:22:01.231] Loaded local transaction journal         transactions=0 dropped=0
INFO [03-02|21:22:01.238] Regenerated local transaction journal    transactions=0 accounts=0
WARN [03-02|21:22:01.243] Switch sync mode from fast sync to full sync
INFO [03-02|21:22:01.279] New local node record                    seq=2 id=6d017d8e59468ff8 ip=127.0.0.1 udp=0 tcp=30303
INFO [03-02|21:22:01.288] Started P2P networking                   self="enode://1f1c94a828eb5e9102845e4823489619ca67f347c4707712dc2c73e07e11fd6ea89d96d87ff8b04df6f99d9bd59d1f80b6b75b1db66814332a8a0612ca2e2fd0@127.0.0.1:30303?discport=0"
INFO [03-02|21:22:01.279] IPC endpoint opened                      url=\\\\.\\pipe\\geth.ipc
INFO [03-02|21:22:01.309] HTTP endpoint opened                     url=http://127.0.0.1:8545 cors= vhosts=localhost
INFO [03-02|21:22:01.363] Mapped network port                      proto=tcp extport=30303 intport=30303 interface=NAT-PMP(192.168.31.1)
INFO [03-02|21:22:01.397] Etherbase automatically configured       address=0xdb11B7d7d6D52d01D169e497f290c9392dB1C4E5
Welcome to the Geth JavaScript console!

instance: Geth/v1.9.11-stable-6a62fe39/windows-amd64/go1.13.8
coinbase: 0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5
at block: 153 (Mon Mar 02 2020 21:19:50 GMT+0800 (CST))
 datadir: D:\eth-test\db
 modules: admin:1.0 debug:1.0 eth:1.0 ethash:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

> eth.accounts
["0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5", "0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849", "0x9a55b9b0009b5b5e3e5b5e7b4d8db2134761ddf7"]
> user1 = eth.accounts[0]
"0xdb11b7d7d6d52d01d169e497f290c9392db1c4e5"
> user2 = eth.accounts[1]
"0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849"
> user3 = eth.accounts[2]
"0x9a55b9b0009b5b5e3e5b5e7b4d8db2134761ddf7"
> eth.getBalance(user1)
0
> eth.getBalance(user2)
306000000000000000000
> eth.getBalance(user3)
0

> web3.fromWei(eth.getBalance(user2), 'ether')
306
> miner.setEtherbase(user2)
true
> personal.unlockAccount(user2)
Unlock account 0x5c51e3c26c0f67b3eeb2f4cabfc93afb616e5849
Passphrase:
true


## 转账
> eth.sendTransaction({from:user2,to:user3,value:web3.toWei(10,'ether')})
INFO [03-02|21:30:03.303] Setting new local account                address=0x5c51e3c26C0f67b3EEb2F4CabFc93AFB616e5849
INFO [03-02|21:30:03.308] Submitted transaction                    fullhash=0xf2c55ee849d2d89535dff41d54e32cf51f0d8faddf2b5bc6d668ec7d6270c37e recipient=0x9A55b9B0009B5b5E3e5B5e7B4d8db2134761dDF7
"0xf2c55ee849d2d89535dff41d54e32cf51f0d8faddf2b5bc6d668ec7d6270c37e"

## 待打包信息
> txpool.status
{
  pending: 1,
  queued: 0
}


miner.start(1)
......

> miner.stop()
null
> txpool.status
{
  pending: 0,
  queued: 0
}

> eth.getBalance(user3)
10000000000000000000
> web3.fromWei(eth.getBalance(user3),'ether')
10


> eth.getBalance(user1)
0
> miner.setEtherbase(user1)
true
> eth.getBalance(user2)
384000000000000000000
> eth.getBalance(user3)
20000000000000000000
>   
