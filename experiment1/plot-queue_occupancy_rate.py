#!/usr/bin/env python3
# coding: utf-8
import numpy as np
import datetime
import sys
import matplotlib.pyplot as plt

### main ###
infilename = "bsv_stn-whatsonchain_data.csv"
infile = open(infilename, "r")

lambda_list = []
mu_list = []
tx_count_list = []
time_list = []

header_flag = True
for line in infile:
  if header_flag == True:
    header_flag = False
    continue

  data_list = line.replace("\n", "").split(",")
  tx_count_list.append( int(data_list[2]) )
  dt = datetime.datetime.strptime(data_list[0], "%Y-%m-%d %H:%M:%S.%f")
  time_list.append(dt.timestamp())

unixtime_list = []
lambda_list = []
mu_list = []
rho_list = []
for i in range(1, len(tx_count_list)):
  if tx_count_list[i] - tx_count_list[i-1] > 0:
    lambda_list.append( tx_count_list[i] - tx_count_list[i-1] )
  elif tx_count_list[i] - tx_count_list[i-1] < 0:
    mu_list.append( tx_count_list[i-1] - tx_count_list[i] )

    # save rho data
    unixtime_list.append( time_list[i] )
    len_ratio = len(lambda_list)/len(mu_list)
    lambda_val = np.average(lambda_list)
    mu_val = np.average(mu_list)
    rho_val = lambda_val / mu_val
    rho_list.append( rho_val*len_ratio )


# plot
plt.plot(unixtime_list[100:], rho_list[100:], ",-")
plt.xlabel("Unix time [sec.]", fontsize=16)
plt.ylabel("Queue occupancy rate", fontsize=16)
plt.savefig("time-vs-queue_occupancy_rate.png", bbox_inches="tight")
plt.savefig("time-vs-queue_occupancy_rate.eps", bbox_inches="tight")
plt.clf()

print("average occupancy rate:", np.average(rho_list[100:]))
print("1-1/rho =", 1.0-1.0/np.average(rho_list[100:]))
