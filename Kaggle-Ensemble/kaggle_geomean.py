from __future__ import division
from collections import defaultdict
from glob import glob
import sys
import math
'''
glob_files = sys.argv[1]
loc_outfile = sys.argv[2]

def kaggle_bag(glob_files, loc_outfile, method="average", weights="uniform"):
  if method == "average":
    scores = defaultdict(float)
  with open(loc_outfile,"wb") as outfile:
    for i, glob_file in enumerate( glob(glob_files) ):
      print("parsing:", glob_file)
      # sort glob_file by first column, ignoring the first line
      lines = open(glob_file).readlines()
      lines = [lines[0]] + sorted(lines[1:])
      #print(lines)
      
      for e, line in enumerate( lines ):
        if i == 0 and e == 0:
          line=line.encode()
          outfile.write(line)
        if e > 0:
          row = line.strip().split(",")
          if scores[(e,row[0])] == 0:
            scores[(e,row[0])] = 1
          scores[(e,row[0])] *= float(row[1])
    for j,k in sorted(scores):
      print(k)
      print(math.pow(scores[(j,k)],1/(i+1)))
      print(type(k))
      k=k.encode()
      print(type(k))
      outfile.write("%s,%f\n"%(k,math.pow(scores[(j,k)],1/(i+1))))
      #outfile.write(k)
      #outfile.write("%s,%f\n"%(k,math.pow(scores[(j,k)],1/(i+1))))
    print("wrote to %s"%loc_outfile)

kaggle_bag(glob_files, loc_outfile)
'''

glob_files = sys.argv[1]
loc_outfile = sys.argv[2]

def kaggle_bag(glob_files, loc_outfile, method="average", weights="uniform"):
  if method == "average":
    scores = defaultdict(float)
  with open(loc_outfile,"w") as outfile:
    for i, glob_file in enumerate( glob(glob_files) ):
      print("parsing:", glob_file)
      # sort glob_file by first column, ignoring the first line
      lines = open(glob_file).readlines()
      lines = [lines[0]] + sorted(lines[1:])
      #print(lines)
      
      for e, line in enumerate( lines ):
        if i == 0 and e == 0:
          #line=line.encode()
          outfile.write(line)
        if e > 0:
          row = line.strip().split(",")
          if scores[(e,row[0])] == 0:
            scores[(e,row[0])] = 1
          scores[(e,row[0])] *= float(row[1])
    for j,k in sorted(scores):
      print(k)
      print(math.pow(scores[(j,k)],1/(i+1)))
      print(type(k))
      #k=k.encode()
      print(type(k))
      outfile.write("%s,%f\n"%(k,math.pow(scores[(j,k)],1/(i+1))))
      #outfile.write(k)
      #outfile.write("%s,%f\n"%(k,math.pow(scores[(j,k)],1/(i+1))))
    print("wrote to %s"%loc_outfile)

kaggle_bag(glob_files, loc_outfile)






















