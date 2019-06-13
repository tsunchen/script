


CMBChina_int_001 = [2.8,3,3.1,3.2,3.4,3.5,3.6,3.65,3.7]
CMBChina_day_001 = [7,14,21,31,61,91,181,365,9999]
#CMBChina_int_001_180 = CMBChina_int_001[:8:]
#CMBChina_day_001_180 = CMBChina_day_001[:8:]

BComm_int_002 = [2.1,2.4,2.7,3.0,3.3,3.6]
BComm_day_002 = [7,14,30,60,90,9999]
#BComm_int_002_90 = BComm_int_002[:6:]
#BComm_day_002_90 = BComm_day_002[:6:]

BComm_int_001 = [2.2,2.5,2.7,2.9,3.1,3.3]
BComm_day_001 = [7,30,92,184,730,9999]
#BComm_int_001_180 = BComm_int_001[:5:]
#BComm_day_001_180 = BComm_day_001[:5:]

CMBC_int_001 = [3.2,3.4,3.6,3.75,3.9,4,4,4]
CMBC_day_001 = [6,13,30,60,90,180,365,9999]
#CMBC_int_001_180 = CMBC_int_001[:7:]
#CMBC_day_001_180 = CMBC_day_001[:7:]

BoC_int_002 = [2.2,3.1,3.75,3.80,3.85,3.90,3.95,4.0,4.05,4.10]
BoC_day_002 = [29,89,179,269,364,547,729,913,1094,9999]
#BoC_int_002_180 = BoC_int_002[:4:]
#BoC_day_002_180 = BoC_day_002[:4:]

BoC_int_001 = [2.00,2.40,3.00,3.2,3.4,3.5,3.6,3.65,3.75]
BoC_day_001 = [6,13,20,30,60,90,120,180,9999]
#BoC_int_001_180 = BoC_int_001[:9:]
#BoC_day_001_180 = BoC_day_001[:9:]










#a0 = 10
#a1 = a0 * (2  /100) / 365 * 6
#a2 = a1 * (2.4/100) / 365 * (13 - 6)
#a3 = a2 * (3  /100) / 365 * (20 - 13)
#a4 = a3 * (3.2/100) / 365 * (30 - 20)
#sum = a1 + a2 + a3 + a4

import numpy as np


a0 = 10000


def calc_interval_array(interval_sum, interval_day, intflow_day, intflow_int, dlim):
    # interval of interest_day
    npx = np.array(intflow_day[1::])
    npy = np.array(intflow_day[0:len(intflow_day)-1:])
    interval_intflow_day = npx - npy
    interval_intflow_daylim = interval_intflow_day[:len(interval_intflow_day)-1:]
    #print(interval_intflow_daylim)
    interval_intflow_daylim2 = []
    interval_intflow_daylim2.append(intflow_day[0])
    interval_intflow_daylim2 += list(interval_intflow_daylim)
    #print(interval_intflow_daylim2)
    dlim, i, a_start = dlim, 0, a0
    intflow_int_start = intflow_int[:len(intflow_int)-1:]
    #print(intflow_int_start)
    for ind in interval_intflow_daylim2:
        interval_day += ind
        if interval_day > dlim:
            interval_int = a_start * (intflow_int_start[i] / 100) / 365 * (ind - (interval_day - dlim))
            interval_sum += interval_int
            interval_interest.append(interval_int)
            interval_rate.append(intflow_int_start[i])
            a_start = a_start + interval_int
            break
        else:
            interval_int = a_start * (intflow_int_start[i] / 100) / 365 * ind
            interval_sum += interval_int
            interval_interest.append(interval_int)
            interval_rate.append(intflow_int_start[i])
            a_start = a_start + interval_int
        i += 1
    print("interval_rate: ", interval_rate)
    print("interval_day: ", npy[:len(interval_rate)+1:])
    print("interval_interest", interval_interest)
    print("summmary_interest: ", a_start)
    print("lessthan_day: ", interval_day)
    print("interval_lessincome: ", interval_sum)
    interestperday = interval_sum / dlim
    print("    IPD: ", interestperday)
    print("")  
            




if __name__ == '__main__':
    array_list = [
     [CMBChina_int_001, CMBChina_day_001, "CMBChina_001"],
     [BComm_int_002, BComm_day_002, "BComm_002"],
     [BComm_int_001, BComm_day_001, "BComm_001"],
     [CMBC_int_001, CMBC_day_001, "CMBC_001"],
     [BoC_int_002, BoC_day_002, "BoC_002"],
     [BoC_int_001, BoC_day_001, "BoC_001"]
    ]

    for i in array_list:
        #print([i][0][0])
        #print([i][0][1])
        #intflow_int =  CMBChina_int_001
        intflow_int = [i][0][0]
        #intflow_day =  CMBChina_day_001
        intflow_day = [i][0][1]
        print(":----: " , [i][0][2])
        len(intflow_day)
        interval_interest = []
        interval_rate = []
        interval_sum = 0
        interval_day = 0
        dlim = 32
        calc_interval_array(interval_sum, interval_day, intflow_day, intflow_int, dlim)
    



