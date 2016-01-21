#import matplotlib libary
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

def median(lst):
    return np.median(np.array(lst))

#define some data
#yi_err is 1.96*STDEVP

#setting color cycle for different curves
colors =['purple', 'blue', 'orange', 'gray', 'red', 'brown', 'blue', 'yellow', 'gray', 'magenta', 'green', 'blue', 'orange', 'gray', 'cyan']
markers = ['o', '^', '*', 's', 'v', '<']
linestyles = [':', '--', '-', '-.', '-.', '--' ]
hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']

x = [10, 20, 30, 40, 50, 60, 100]
labels = ["UFL to GoogleDrive (Direct)", "UFL to Coldlake (V)", "Coldlake to GoogleDrive (V)", "UFL to UMich (V)", "UMich to GoogleDrive(V)", 
	"UFL to Dropbox (Direct)", "UFL to Coldlake (V)", "Coldlake to Dropbox (V)", "UFL to UMich (V)", "UMich to Dropbox (V)", "UFL to OneDrive (Direct)",
	"UFL to Coldlake (V)", "Coldlake to OneDrive (V)", "UFL to UMich (V)", "UMich to OneDrive (V)"
	]
stream = 'upload'
bar_width = 0.25

fig, ax = plt.subplots()
fig.set_size_inches(12, 9.5)

subplotNum = 111 #only one graph
subfig = fig.add_subplot(subplotNum)
ind = np.arange(3, 22, 3)

graphLines = []
rects = []

bar = 0;

j = 0;

directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("GoogDirectUFL.txt") as f:
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
	with open("GoogColdInterUFL.txt") as f:
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
	with open("GoogColdRemote.txt") as f:
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
	with open("GoogUMichInterUFL.txt") as f:
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
	with open("GoogUMichRemoteUFL.txt") as f:
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


'''*******************************************************************Dropbox************************************************************************'''

j += 1
bar += 1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("DropDirectUFL.txt") as f:
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
	with open("DropColdInterUFL.txt") as f:
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
	with open("DropColdRemote.txt") as f:
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
	with open("DropUMichInterUFL.txt") as f:
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
	with open("DropUMichRemote.txt") as f:
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


'''*************************************************************************One Drive******************************************************************************'''
'''
j += 1
bar += 1
directavgs = []
directsds = []

for filesz in x:
	values = []
	with open("OneDirectUCLAColdlake.txt") as f:
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
	with open("OneColdInter_UCLA.txt") as f:
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
	with open("OneColdRemoteUCLA.txt") as f:
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
	with open("OneUMichInter_UCLA.txt") as f:
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
	with open("OneUMichRemoteUCLA.txt") as f:
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

ax.set_xlabel("File-size (MB)", fontsize=18)
ax.set_ylabel("Time-taken (ms)", fontsize=18)
ax.set_title("Comparison of direct transfer and intermediate node-transfer - 6-Oct-15")
ax.set_xlim([3,24])
ax.set_xticklabels(x)
ax.set_xticks(ind + bar_width * (bar + 1) / 2)
ax.legend(rects, labels, prop={'size':'14'},loc='upper center', bbox_to_anchor=(0.45, 0.97), ncol=2, fancybox=True, shadow=True)

plt.show()
#plt.savefig("Direct_Client" + str(filesz) + "_MB_" + stream + ".png", bbox_inches='tight')
