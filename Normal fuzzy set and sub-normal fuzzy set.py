# 6.Normal fuzzy set and sub-normal fuzzy set
 
A = dict()
A = {"a": 1, "b": 0.3, "c": 0.5, "d": 0.2 ,"e":0.5}

for i in A :
     height = A[i]
     if height == 1 :
         print(A, ' is a normal fuzzy set')
         break
     elif (0 < height < 1) :
         print(A, ' is sub - normal fuzzy set') 
         break
