import pandas as pd
import matplotlib.pyplot as plt
import random
import math

#read data
set1 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')
set2 = pd.read_csv("path to dataset", sep = " |\t", header = None, engine='python')

final = [set1, set2]
total = pd.concat(final)

#split input into list to plot histogram
def final_list(list1):
    list2 = []

    for x in list1:
        if type(x).__name__ == "list":
            list2 += final_list(x)
        else:
            list2.append(x)

    return list2


#hist for total dataset
total_dist = final_list(total.iloc[:, :].values.tolist())
plt.hist(total_dist, bins='auto')
total_sum = sum(total_dist)
mean = total_sum / len(total_dist)
variance  = sum(pow(x-mean,2) for x in total_dist) / len(total_dist)
std_deviation  = math.sqrt(variance)
print mean
print std_deviation
print variance
plt.xlabel('Mean :{} \nStandard Deviation :{} \nVariance :{}'.format(mean,std_deviation,variance), ha='left')
plt.title('Total distribution')
plt.show()

#hist for 10 random vectors
mylist=[]
mylist = random.sample(range(1, 1000), 10)
print(mylist)
for i in mylist:
    lst = final_list(total.iloc[i-1:i, :].values.tolist())
    list_sum = sum(lst)
    mean_lst = list_sum / len(lst)
    variance_lst = sum(pow(x - mean_lst, 2) for x in lst) / len(lst)
    std_deviation_lst = math.sqrt(variance_lst)
    print mean_lst
    print std_deviation_lst
    print variance_lst
    plt.hist(lst,bins=25)
    plt.xlabel('Mean :{} \nStandard Deviation :{} \nVariance :{}'.format(mean_lst, std_deviation_lst, variance_lst), ha='left')
    plt.title('Vector:'+format(i))
    plt.show()
    print i
    print lst

