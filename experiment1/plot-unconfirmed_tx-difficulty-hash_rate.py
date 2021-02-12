#!/usr/bin/env python3
# coding:utf-8
import matplotlib.pyplot as plt
import datetime
import sys

infilename = "bsv_stn-whatsonchain_data.csv"
infile = open(infilename, "r")

unixtime_list = []
hashrate_list = []
tx_count_list = []
difficulty_list = []

header_flag = True
for line in infile:
  if header_flag == True:
    header_flag = False
    continue
  data_list = line.replace("\n", "").split(",")
  #print(data_list[0])
  dt = datetime.datetime.strptime(data_list[0], '%Y-%m-%d %H:%M:%S.%f')
  unixtime_list.append( int(dt.timestamp()) )

  hashrate_list.append( float(data_list[1]) )
  tx_count_list.append( int(data_list[2]) )
  difficulty_list.append( float(data_list[3]) )
  

min_val = unixtime_list[0]
for i in range(1, len(unixtime_list)):
  if unixtime_list[i] < min_val:
    min_val = unixtime_list[i]

for i in range(len(unixtime_list)):
  unixtime_list[i] -= min_val

# plot
plt.plot(unixtime_list, tx_count_list, ",-", label="")
plt.xlabel("elapsed time [sec.]", fontsize=16)
plt.ylabel("# of unconfirmed transactions", fontsize=16)
#plt.show()
plt.savefig("time-vs-unconfirmed_tx-plot.png", bbox_inches="tight")
plt.savefig("time-vs-unconfirmed_tx-plot.eps", bbox_inches="tight")
plt.clf()

plt.plot(unixtime_list, difficulty_list, ",-", label="")
plt.xlabel("elapsed time [sec.]", fontsize=16)
plt.ylabel("difficulty [x 10^1]", fontsize=16)
#plt.show()
plt.savefig("time-vs-difficulty-plot.png", bbox_inches="tight")
plt.savefig("time-vs-difficulty-plot.eps", bbox_inches="tight")
plt.clf()

plt.plot(unixtime_list, hashrate_list, ",-", label="")
plt.xlabel("elapsed time [sec.]", fontsize=16)
plt.ylabel("hash rate [MH/s]", fontsize=16)
#plt.show()
plt.savefig("time-vs-hash_rate-plot.png", bbox_inches="tight")
plt.savefig("time-vs-hash_rate-plot.eps", bbox_inches="tight")
plt.clf()


plt.plot(hashrate_list, difficulty_list, marker=",", linestyle="-", label="")
plt.xlabel("hash rate [MH/s]", fontsize=16)
plt.ylabel("difficulty [x 10^1]", fontsize=16)
#plt.show()
plt.savefig("hash_rate-vs-difficulty-plot.png", bbox_inches="tight")
plt.savefig("hash_rate-vs-difficulty-plot.eps", bbox_inches="tight")
plt.clf()
