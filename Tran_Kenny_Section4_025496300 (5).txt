#Kenny Tran 025496300
#CECS 229 Lab 3
#3/3/21
class hash_table:
        def __init__(self, size = 8):
                self.table = (None,) * size
                self.size = size

        def insert(self, value, index):
                temp = list(self.table)
                temp[index] = value
                self.table = tuple(temp)

        def linear_probe(self, value, start_index):
                if self.table[start_index]== None:
                        self.insert(value,start_index)
                else:
                        while self.table[start_index]!=None:
                                if start_index >= len(self.table)-1:
                                        start_index = 0
                                else:
                                        start_index +=1
                        self.insert(value,start_index)
                                
        def hash(self, value):
                start_index = value % self.size
                self.linear_probe(value,start_index)
                
        def get_table(self):
                return self.table

        def __str__(self):
                return str(self.table)
