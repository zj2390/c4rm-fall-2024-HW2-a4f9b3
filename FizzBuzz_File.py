import numpy as np

def FizzBuzz(start, finish):
   
   
    numvec = np.arange(start, finish + 1)


    objvec = numvec.astype(object)

 
    objvec[(numvec % 3 == 0) & (numvec % 5 == 0)] = "fizzbuzz"
    objvec[(numvec % 3 == 0) & (numvec % 5 != 0)] = "fizz"
    objvec[(numvec % 5 == 0) & (numvec % 3 != 0)] = "buzz"

    return objvec


start = 40
finish = 45
result = FizzBuzz(start, finish)


print(result)
