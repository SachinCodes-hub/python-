class solution:
    def insert(self, key):
        self.arr.append(key)
        self.heapifyup(self.arr , self.count)
        self.count += 1
        
    def changekey(self , index , new_val):
        if self.arr[index] > new_val:
            self.arr[index] = new_val
            self.hepifyup(self.arr , index)
        
        else:
            self.arr[index] = new_val
            self.hepifydown(self.arr , index)
        
    
    def extractmin(self):
        if self.count == 0:
            return None
        ele = self.arr[0]
        self.arr[0] , self.arr[self.count - 1] - self.arr[self.count - 1] , self.arr[0]
        self.arr.pop()
        self.count -= 1
        if self.count > 0 :
            self.hepifydown(self.arr , 0 )
        return ele
    
    def isEmpty(self):
        return self.count == 0 
    
    