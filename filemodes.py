# -*- coding: utf-8 -*-
"""filemodes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VXnKHGSCGlDB6gQpCFeOwwqIGngZuCK2
"""

with open("File.txt","r+") as fl2:
   print(fl2.read())
   fl2.write("Hey")

with open("File.txt","w+") as fl2:
  fl2.write("gresey")
  print(fl2.read())

with open("File.txt","+a") as fl2:
  fl2.write(" patidar")
  print(fl2.read())