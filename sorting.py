import numpy as np
import random 

class SortList:

    def __init__(self, l):
        self.l = l
    
    def bubble(self):
        for passnum in range(len(self.l)-1,0,-1):
            for i in range(passnum):
                if self.l[i]>self.l[i+1]:
                    temp = self.l[i]
                    self.l[i] = self.l[i+1]
                    self.l[i+1] = temp
        return

    def randomize(self):
        random.shuffle(self.l)

    def __str__(self):
        return str(self.l)


sort_list = SortList([5,4,3,5,4])

print(sort_list)
sort_list.bubble()
print(sort_list)
sort_list.randomize()
print(sort_list)
