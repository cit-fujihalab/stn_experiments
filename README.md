# stn_experiments

## Specifications of the machine used in the experiments

```
CPU: Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz x 24

Memory: 64GB

HDD: 7.3TB

Internet: 
$ speedtest-cli 
Hosted by fdcservers.net (Tokyo) [11.02 km]: 13.876 ms
Download: 187.32 Mbit/s
Upload: 96.06 Mbit/s

OS: Ubuntu 20.04 LTS

Software version: bitcoin-sv-1.0.5
```


## experiment1

```
$ sudo pip3 install numpy matplotlib

$ python3 plot-unconfirmed_tx-difficulty-hash_rate.py 

$ python3 plot-queue_occupancy_rate.py 
average occupancy rate: 1.0118902422783222
1-1/rho = 0.011750525681076596
```

## experiment2

```
$ tar -zxvf 20201104-20210113getinfo_errors.tar.gz 
20201104-20210113getinfo_errors.csv

$ python3 estimate_fork_probability.py 
This is a pre-release or beta test build - use at your own risk - do not use for mining or merchant applications : 0.9141934285996256
Warning: The network does not appear to fully agree! We received headers of a large fork. Still waiting for block data for more details. : 0.05599724337733113
Warning: The network does not appear to fully agree! Some miners appear to be experiencing issues. A large valid fork has been detected. : 0.029809328023043223
Fork probability: 0.0858065714003744
```


## experiment3

```
$ sudo pip3 install powerlaw

$ python3 tx_confirmation_latency_analysis.py 
alpha: 2.2408700769198675
sigma: 0.023731602028076185
power law vs. exponential: (282.5344467132366, 1.9772250598634115e-12)
```

