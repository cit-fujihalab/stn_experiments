#!/usr/bin/env python3


errors_dict = {}
header_flag = True

infile = open("20201104-20210113getinfo_errors.csv")

for line in infile:

  # skip header
  if header_flag == True:
    header_flag = False
    continue

  # get errors
  data_list = line.replace("\n", "").split(",")
  if data_list[2] not in errors_dict:
    errors_dict[ data_list[2] ] = 1
  else:
    errors_dict[ data_list[2] ] += 1
infile.close()

# print results
total_count = 0
for k, v in errors_dict.items():
  total_count += v

for k, v in errors_dict.items():
  print(k, ":",  float(v)/total_count)

for k, v in errors_dict.items():
  print("Fork probability:", 1-float(v)/total_count)
  break
