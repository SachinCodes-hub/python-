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
        
    # TC - O(log(N))
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
    
    
    # TC -  o(1)
    def isEmpty(self):
        return self.count == 0 
    
    def getmin(self):
        return self.arr[0] if self.count > 0 else None
    
    def heapsize(self):
        return self.count


    def main():
        heap = solution()
        
        heap.initializeHeap()
        
        heap.insert(4)
        print("inserted 4")
    
        heap.insert(5)
        print("inserted 5") 
        
        heap.insert(10)
        print("inserted 10")       
    