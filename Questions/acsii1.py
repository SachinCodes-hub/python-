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


string3 = "ttththrj"
hashmap = [0] *26
for ch in string3:
    print(ord(ch))
    index = ord(ch) - 97 # ascii values are from 97 - 123 - so to make them start from 0 index . 
    hashmap[index] = hashmap[index] + 1


    print(hashmap[3])

