#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Print:
# A line of hyphens the same length as the Belgium string, followed by

# The string with the comma separators replaced by colons ':' followed by
# The population of Belgium (the second field) plus the population of the capital city (the fourth field)
#   Hint: the answer should be 11 183 818

lengthBelg = len(Belgium)

# print(lengthBelg)
print('-'*lengthBelg)

print(Belgium.replace(',', ':'))

NewBelg = Belgium.split(',')
pop1 = int(NewBelg[1])
pop2 = int(NewBelg[3])
print("\nThe population of Belgium and of Brussels combined is", pop1 + pop2)
