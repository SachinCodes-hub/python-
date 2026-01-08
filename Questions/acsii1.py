str = "abccdgfr" # string are iterable in python and in general language
str1 = "abcd"# now here we have characters 
hashmap = [0] * 26
for ch in str:
    ascii = ord(ch)
    index = ascii - 97
    hashmap[index] +=1
for ch in str1:
    ascii = ord(ch)
    index = ascii - 97
    
    print(hashmap[index])
    
