
CMBChina_int_001 = [2.8,3,3.1,3.2,3.4,3.5,3.6,3.65,3.7]
CMBChina_day_001 = [7,14,21,31,61,91,181,365,9999]
CMBChina_int_001_180 = CMBChina_int_001[:8:]
CMBChina_day_001_180 = CMBChina_day_001[:8:]

BComm_int_002 = [2.1,2.4,2.7,3.0,3.3,3.6]
BComm_day_002 = [7,14,30,60,90,9999]
BComm_int_002_90 = BComm_int_002[:6:]
BComm_day_002_90 = BComm_day_002[:6:]

BComm_int_001 = [2.2,2.5,2.7,2.9,3.1,3.3]
BComm_day_001 = [7,30,92,184,730,9999]
BComm_int_001_180 = BComm_int_001[:5:]
BComm_day_001_180 = BComm_day_001[:5:]

CMBC_int_001 = [3.2,3.4,3.6,3.75,3.9,4,4,4]
CMBC_day_001 = [6,13,30,60,90,180,365,9999]
CMBC_int_001_180 = CMBC_int_001[:7:]
CMBC_day_001_180 = CMBC_day_001[:7:]

BoC_int_002 = [2.2,3.1,3.75,3.80,3.85,3.90,3.95,4.0,4.05,4.10]
BoC_day_002 = [29,89,179,269,364,547,729,913,1094,9999]
BoC_int_002_180 = BoC_int_002[:4:]
BoC_day_002_180 = BoC_day_002[:4:]

BoC_int_001 = [2.00,2.40,3.00,3.2,3.4,3.5,3.6,3.65,3.75]
BoC_day_001 = [6,13,20,30,60,90,120,180,9999]
BoC_int_001_180 = BoC_int_001[:9:]
BoC_day_001_180 = BoC_day_001[:9:]


intflow_int =  CMBChina_int_001_180
intflow_day =  CMBChina_day_001_180
len(intflow_day)



#a0 = 10
#a1 = a0 * (2  /100) / 365 * 6
#a2 = a1 * (2.4/100) / 365 * (13 - 6)
#a3 = a2 * (3  /100) / 365 * (20 - 13)
#a4 = a3 * (3.2/100) / 365 * (30 - 20)
#sum = a1 + a2 + a3 + a4

import numpy as np


npx = np.array(intflow_day[1::])
npy = np.array(intflow_day[0:len(intflow_day)-1:])
interval_intflow_day = npx - npy
interval_intflow_daylim = interval_intflow_day[:len(interval_intflow_day)-1:]

a0 = 10000

interval_interest = []
interval_sum = 0
interval_day = 0

a1 = a0 * (intflow_int[0]/100) / 365 * intflow_day[0]
interval_day += intflow_day[0]
print (a1)
interval_sum += a1

a_start = a0 + a1
intflow_int_start = intflow_int[1:len(intflow_int)-1:]
print(intflow_int_start)

i = 0
for ind in interval_intflow_daylim:
    interval_int = a_start * (intflow_int_start[i] / 100) / 365 * ind
    interval_day += ind
    interval_sum += interval_int
    interval_interest.append(interval_int)
    a_start = a_start + interval_int
    i+=1
    #pass
    #print(ind)

print("interval_interest", interval_interest)
print("summmary_interest: ", a_start)
print("total_day: ", interval_day)
print("interval_sum: ", interval_sum)

interestperday = interval_sum / interval_day
print("IPD: ", interestperday)



