import json
import csv
import os
import numpy as np
import matplotlib.pyplot as plt


handle9 = open("./Metricstest/inlabhovertime.csv", 'rb')
handle10 = open("./Metricstest/outlabhovertime.csv", 'rb')

inlabhover = []
outlabhover = []


with handle9 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		inlabhover = np.array(list(row)).astype(np.float)

with handle10 as infile:
	parsed=csv.reader(infile)
	for row in parsed:
		outlabhover = np.array(list(row)).astype(np.float)

bins = np.arange(0, 1500, 10)

#print len(inlabhover)
#print len(outlabhover)
#print len(inlabtimes)
#print len(outlabtimes)

#inlabhover = np.log(inlabhover)
#outlabhover = np.log(outlabhover)

inlabhover = np.ma.masked_equal(inlabhover,0)
outlabhover = np.ma.masked_equal(outlabhover,0)

sdvinlab = np.std(inlabhover)
meaninlab = np.mean(inlabhover)
varinlab = np.var(inlabhover)
sdvoutlab = np.std(outlabhover)
meanoutlab = np.mean(outlabhover)
varoutlab = np.var(outlabhover)

'''
label1 = ["$\overline{x}$ = " + str(meaninlab) + "\n" + "$s$ = " + str(sdvinlab) + "\n" + "$s^2$ = " + str(varinlab)]
plt.hist(inlabhover, bins, label = label1)
plt.title("Histogram of mouse hover time duration before mouse click \n in lab environment")
plt.xlabel("Hover time duration (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 1500, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.tight_layout()
#plt.show()
plt.savefig('./finalgraphs/In_Lab_Hover_Time_Histogram_Unweighted.png')
plt.clf()


label2 = ["$\overline{x}$ = " + str(meanoutlab) + "\n" + "$s$ = " + str(sdvoutlab) + "\n" + "$s^2$ = " + str(varoutlab)]
plt.hist(outlabhover, bins, label = label2)
plt.title("Histogram of mouse hover time duration before mouse click \n out of lab environment")
plt.xlabel("Hover time duration (ms)")
plt.ylabel("Frequency (# of mouse path sequences)")
plt.xticks(np.arange(0, 1500, 100), rotation = 'vertical')
plt.legend(loc="best")
plt.tight_layout()
#plt.show()
plt.savefig('./finalgraphs/Out_Lab_Hover_Time_Histogram_Unweighted.png')
plt.clf()
'''

print meaninlab
print sdvinlab
print varinlab
print meanoutlab
print sdvoutlab
print varoutlab
print min(inlabhover)
print max(inlabhover)
print min(outlabhover)
print max(outlabhover)

'''
data = [inlabhover, outlabhover]
plt.boxplot(data, 0, '', labels=["In lab", "Out of lab"])
plt.title("Mouse hover time before click event")
plt.ylabel('Hover time (ms)')
#plt.savefig('./finalgraphs/Total_Hover_Times_Box_Plot_No_Notches_Exclude_Outliers.png')
plt.show()
plt.clf()
'''