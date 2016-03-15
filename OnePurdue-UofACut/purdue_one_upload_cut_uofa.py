#import matplotlib libary
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

def median(lst):
    return np.median(np.array(lst))

def thickcap(caps):
	for cap in caps:
		cap.set_markeredgewidth(2)
#define some data
#yi_err is 1.96*STDEVP

#setting color cycle for different curves
colors =['purple', 'white', 'orange', 'yellow', 'white', 'brown', 'blue', 'yellow', 'gray', 'magenta', 'green', 'blue', 'orange', 'gray', 'cyan']
markers = ['o', '^', '*', 's', 'v', '<']
linestyles = [':', '--', '-', '-.', '-.', '--' ]
hatches = ['/', ' ', '*',  '/', '+', 'o', '\\', '|', '-', 'O', '+']

x = [10, 20, 30, 40, 50, 60, 100]
labels = [#"Purdue to GoogleDrive (Direct)", "Purdue to Coldlake", "Coldlake to GoogleDrive", "Purdue to UofA", "UofA to GoogleDrive", 
	"Purdue to One Drive (Direct)", "Purdue to UofA", "UofA to One Drive", "Purdue to One Drive (UofA-cut-through)",
	#"Purdue to OneDrive (Direct)", "Purdue to Coldlake", "Coldlake to OneDrive", "Purdue to UofA", "UofA to OneDrive"
	]
stream = 'upload'
bar_width = 0.50

fig, ax = plt.subplots()
fig.set_size_inches(10.24, 8)

subplotNum = 111 #only one graph
subfig = fig.add_subplot(subplotNum)
ind = np.arange(2, 15, 2)

graphLines = []
rects = []

bar = -1;

j = -1;

'''
j+=1
bar+=1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("../GoogleDriveDirectPurdue.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))

	directavgs.append(st.median(values[2:7]))
	directsds.append(st.stdev(values[2:7]))

print(directavgs)
print(directsds)


rects.append(ax.bar(ind + bar_width * bar, directavgs, bar_width,
                 color=colors[j],
                 yerr=directsds, ecolor='black'))


j += 1
bar += 1
interavgs = []
intersds = []

for filesz in x:
	values = []
	with open("../GoogleDriveInterPurdueToColdlake.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	interavgs.append(st.median(values[2:7]))
	intersds.append(st.stdev(values[2:7]))

print(interavgs)
print(intersds)

rects.append(ax.bar(ind + bar_width * bar, interavgs, bar_width,
                 color=colors[j],
                 yerr=intersds, ecolor='black', hatch=hatches[j]))

j += 1
remoteavgs = []
remotesds = []

for filesz in x:
	values = []
	with open("../GoogleDriveInterNodePurdueCold.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	remoteavgs.append(st.median(values[2:7]))
	remotesds.append(st.stdev(values[2:7]))

print(remoteavgs)
print(remotesds)

rects.append(ax.bar(ind + bar_width * bar, remoteavgs, bar_width,
                 color=colors[j],
                 yerr=remotesds,
                 ecolor='black', bottom = interavgs, hatch=hatches[j]))

j += 1
bar += 1
interavgs = []
intersds = []

for filesz in x:
	values = []
	with open("../GoogleDriveInterPurdueToUofA.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	interavgs.append(st.median(values[2:7]))
	intersds.append(st.stdev(values[2:7]))

print(interavgs)
print(intersds)

rects.append(ax.bar(ind + bar_width * bar, interavgs, bar_width,
                 color=colors[j],
                 yerr=intersds, ecolor='black', hatch=hatches[j]))

j += 1
remoteavgs = []
remotesds = []

for filesz in x:
	values = []
	with open("../GoogleDriveInterNodePurdueUofA.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	remoteavgs.append(st.median(values[2:7]))
	remotesds.append(st.stdev(values[2:7]))

print(remoteavgs)
print(remotesds)

rects.append(ax.bar(ind + bar_width * bar, remoteavgs, bar_width,
                 color=colors[j],
                 yerr=remotesds,
                 ecolor='black', bottom = interavgs, hatch=hatches[j]))

'''
'''*******************************************************************One Drive************************************************************************'''


j += 1
bar += 1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("OneDirectUofA.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))

	directavgs.append(st.median(values[2:7])/1000)
	directsds.append(st.stdev(values[2:7])/1000)

#print(directavgs)
#print(directsds)


rects.append(ax.bar(ind + bar_width * bar, directavgs, bar_width,
                 color=colors[j]))

(_, caps, _) = ax.errorbar(ind + bar_width/2 * (bar + 1), directavgs, yerr=directsds, ecolor='black', elinewidth=4.0, fmt=None, capsize=7)

thickcap(caps)


j += 1
bar += 1
interavgs = []
intersds = []

for filesz in x:
	values = []
	with open("OneUofAInter.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	interavgs.append(st.median(values[2:7])/1000)
	intersds.append(st.stdev(values[2:7])/1000)

#print(interavgs)
#print(intersds)

rects.append(ax.bar(ind + bar_width * bar, interavgs, bar_width,
                 color=colors[j], hatch=hatches[j]))

(_, caps, _) = ax.errorbar(ind + bar_width/2 * (bar + 2), interavgs, yerr=intersds, ecolor='black', elinewidth=4.0, fmt=None, capsize=7)

thickcap(caps)

j += 1
remoteavgs = []
remotesds = []

for filesz in x:
	values = []
	with open("OneUofARemote.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	remoteavgs.append(st.median(values[2:7])/1000)
	remotesds.append(st.stdev(values[2:7])/1000)

print(remoteavgs)
print(remotesds)

rects.append(ax.bar(ind + bar_width * bar, remoteavgs, bar_width,
                 color=colors[j], bottom = interavgs, hatch=hatches[j]))

(_, caps, _) = ax.errorbar(ind + bar_width/2 * (bar + 2), np.array(interavgs)+np.array(remoteavgs), yerr=remotesds, ecolor='black', elinewidth=4.0, fmt=None, capsize=7)

thickcap(caps)

j += 1
bar += 1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("OneUofAInterWorm.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	directavgs.append(st.median(values[2:7])/1000)
	directsds.append(st.stdev(values[2:7])/1000)

#print(directavgs)
#print(directsds)


rects.append(ax.bar(ind + bar_width * bar, directavgs, bar_width,
                 color=colors[j], hatch=hatches[j]))

(_, caps, _) = ax.errorbar(ind + bar_width/2 * (bar + 3), directavgs, yerr=directsds, ecolor='black', elinewidth=4.0, fmt=None, capsize=7)

thickcap(caps)

rmct = []
rmctsds = []

for filesz in x:
	values = []
	with open("OneUofARemoteCutThrough.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	rmct.append(st.median(values[2:7])/1000)
	rmctsds.append(st.stdev(values[2:7])/1000)

print(rmct)
print(rmctsds)

'''*************************************************************************One Drive******************************************************************************'''

'''
j += 1
bar += 1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("OneDirectPurdueColdlake.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))

	directavgs.append(st.median(values[2:7]))
	directsds.append(st.stdev(values[2:7]))

print(directavgs)
print(directsds)


rects.append(ax.bar(ind + bar_width * bar, directavgs, bar_width,
                 color=colors[j],
                 yerr=directsds, ecolor='black'))


j += 1
bar += 1
interavgs = []
intersds = []

for filesz in x:
	values = []
	with open("OneColdInter_Purdue.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	interavgs.append(st.median(values[2:7]))
	intersds.append(st.stdev(values[2:7]))

print(interavgs)
print(intersds)

rects.append(ax.bar(ind + bar_width * bar, interavgs, bar_width,
                 color=colors[j],
                 yerr=intersds, ecolor='black'))

j += 1
remoteavgs = []
remotesds = []

for filesz in x:
	values = []
	with open("OneColdRemotePurdue.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	remoteavgs.append(st.median(values[2:7]))
	remotesds.append(st.stdev(values[2:7]))

print(remoteavgs)
print(remotesds)

rects.append(ax.bar(ind + bar_width * bar, remoteavgs, bar_width,
                 color=colors[j],
                 yerr=remotesds,
                 ecolor='black', bottom = interavgs))

j += 1
bar += 1
interavgs = []
intersds = []

for filesz in x:
	values = []
	with open("OneUofAInter_Purdue.txt") as f:
		for line in f:
			lineValues = line.strip().split(' ')
			if (int)(lineValues[0]) != filesz:
				continue
			values.append(float(lineValues[1]) * 1000)
	interavgs.append(st.median(values[2:7]))
	intersds.append(st.stdev(values[2:7]))

print(interavgs)
print(intersds)

rects.append(ax.bar(ind + bar_width * bar, interavgs, bar_width,
                 color=colors[j],
                 yerr=intersds, ecolor='black'))

j += 1
remoteavgs = []
remotesds = []

for filesz in x:
	values = []
	with open("OneUofARemotePurdue.txt") as f:
		for line in f:
			lineValues = line.split('\t')
			if lineValues[2] != stream or (int)(lineValues[1]) != filesz:
				continue
			values.append(float(lineValues[3]))
	remoteavgs.append(st.median(values[2:7]))
	remotesds.append(st.stdev(values[2:7]))

print(remoteavgs)
print(remotesds)

rects.append(ax.bar(ind + bar_width * bar, remoteavgs, bar_width,
                 color=colors[j],
                 yerr=remotesds,
                 ecolor='black', bottom = interavgs))
'''

print(bar)

ax.set_xlabel("File size (MB)", fontsize=26)
ax.set_ylabel("Transfer Time (s)", fontsize=26)
#ax.set_title("Comparison of direct transfer and intermediate node-transfer - 5-Oct-15")
ax.set_xlim([1.5,16])
#ax.set_ylim([0,1300000/1000])
ax.set_xticklabels(x)
ax.tick_params(labelsize=26)
ax.set_xticks(ind + bar_width * (bar + 1) / 2)
fig.subplots_adjust(right=0.99)
fig.subplots_adjust(left=0.108)
ax.legend(rects, labels, prop={'size':'22'},loc='upper center', bbox_to_anchor=(0.44, 0.99), ncol=1, fancybox=True, shadow=True)

#plt.show()
plt.savefig("./purdue_one_cut_uofa.pdf", bbox_inches='tight', dpi=60000)
