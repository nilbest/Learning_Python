# Use the file name mbox-short.txt as the file name
fname = 'mbox-short.txt'
fh = open(fname)
sum=0
line_count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line_count=line_count+1
    line.rsplit()
    print(line)
print("Done")
average=sum/line_count