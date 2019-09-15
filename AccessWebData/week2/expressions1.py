#!/usr/bin/python3
# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_274050.txt"
lst=[]
list(lst)
fh = open(fname)
count = 0
int(count)
suma=int()
suma=0
for line in fh:
    line = line.rstrip()
    aux = re.findall("[0-9]+",line)
    print(lst, "\n")
    if aux != []:
        lst.extend(aux)
        print(aux,"\n\n\n")
    print("****************")
for i in lst:
    suma=suma+int(i)
    count=count+1
    print(suma)
print(count, suma)

    #if line.startswith('From:'):
     #   aux=line.split()
      #  # if aux[1] not in lst:
       # lst.append(aux[1])
       # count=count+1
       # print(aux[1])
#print("There were", count, "lines in the file with From as the first word")

