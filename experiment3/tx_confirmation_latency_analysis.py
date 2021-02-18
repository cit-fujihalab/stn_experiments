#!/usr/bin/env python3
# coding: utf-8
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import powerlaw
import sys

latency_list = []
tx_sent_time_list = []
block_number_list = []
tx_size_list = []
fee_rate_list = []

infilename = "txidlog-todo_now.txt-analyzed_results.csv"
infile = open(infilename, "r")

for line in infile:
  data_list = line.replace("\n", "").split(",")
  #print(data_list[8], data_list[4])
  latency_list.append( int(data_list[8]) )
  block_number_list.append( int(data_list[4]) )
  tx_sent_time_list.append( int(data_list[1])/60.0 )
  tx_size_list.append(int(data_list[11][:-2]))
  fee_rate_list.append(float(data_list[9][:-6]))
  

min_tx_sent_time = min(tx_sent_time_list)
#print("min tx sent time", min_tx_sent_time)
for i in range(len(tx_sent_time_list)):
  tx_sent_time_list[i] -= min_tx_sent_time


# plot histogram curve 
n, bins, patches = plt.hist(latency_list, bins=100, density=True)
plt.clf()
bins_mod = []
for i in range(len(bins)-1):
  bins_mod.append( (bins[i] + bins[i+1])/2.0 )

## normal plot
#plt.plot(bins_mod, n, marker="o", linestyle="-")
#plt.xlabel("latency [sec.]", fontsize=16)
#plt.ylabel("frequency", fontsize=16)
#plt.savefig("latency_histogram-normal.png")
#plt.savefig("latency_histogram-normal.eps")
#plt.clf()

## plot with semilogy 
#plt.semilogy(bins_mod, n, marker="o", linestyle="-")
#plt.xlabel("latency [sec.]", fontsize=16)
#plt.ylabel("frequency", fontsize=16)
#plt.savefig("latency_histogram-semilogy.png")
#plt.savefig("latency_histogram-semilogy.eps")
#plt.clf()


# fit with powerlaw
fit = powerlaw.Fit(latency_list)
print("alpha:", fit.power_law.alpha)
print("sigma:", fit.power_law.sigma)
print("power law vs. exponential:", fit.distribution_compare('power_law', 'exponential'))
print("power law vs. truncated power law:", fit.distribution_compare('power_law', 'truncated_power_law'))
fit.power_law.plot_pdf(color="red", linestyle="--")
#sys.exit(0)


# plot with loglog 
plt.loglog(bins_mod, n, marker=".", linestyle="-")
plt.xlabel("latency [sec.]", fontsize=16)
plt.ylabel("frequency", fontsize=16)
plt.savefig("latency_histogram-loglog.png")
plt.savefig("latency_histogram-loglog.eps")
plt.clf()


# plot time vs. block number
plt.plot(tx_sent_time_list, block_number_list, marker=".", linestyle="-", markersize=4)
plt.xlabel("elapsed time [min.]", fontsize=16)
plt.ylabel("block number", fontsize=16)
plt.savefig("time-block_number.png")
plt.savefig("time-block_number.eps")
#plt.show()
plt.clf()


## plot tx size vs. latency
#plt.plot(tx_size_list, latency_list, marker=".", linestyle="")
#plt.xlabel("tx size [Byte]", fontsize=16)
#plt.ylabel("latency [sec.]", fontsize=16)
#plt.savefig("tx_size-latency.png")
#plt.savefig("tx_size-latency.eps")
#plt.clf()

# plot fee rate vs. latency
plt.plot(fee_rate_list, latency_list, marker=".", linestyle="")
plt.xlabel("fee rate [satoshi/Byte]", fontsize=16)
plt.ylabel("latency [sec.]", fontsize=16)
plt.savefig("fee_rate-latency.png")
plt.savefig("fee_rate-latency.eps")
plt.clf()


