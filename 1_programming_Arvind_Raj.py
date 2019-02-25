def englishify(number):
    
    #Define some common numbers to be spelt out from 0-20 & the tens in a dict:
    digits = {0: 'Zero', 1: 'One', 2:'Two', 3: 'Three', 4 : 'Four', 5 : 'Five', 
           6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
          19 : 'Nineteen', 20 : 'Twenty',
          30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' 
          }
    
    #Define thousand & million
    K = 1000
    M = K * 1000
    
    
    assert(number >= 0), "Please enter positive integer" #check if is positive integer
    
    #Parse the integer to its constituent digits and spell accordingly:
    if (number < 20):
        return digits[number]
    
    if (number < 100):    #20-99 numbers
        if number % 10 == 0 :
            return digits[number]
        else:
            return digits[number//10 * 10] + ' ' + digits[number%10]
    
    if (number < K):      #hundreds numbers
        if number % 100 == 0:
            return digits[number//100] + ' Hundred'
        else:
            return digits[number//100] + ' Hundred And ' + englishify(number%100)
    
    if (number < M):      #thousands numbers
        if number % K ==0:
            return englishify(number//K) + ' Thousand'
        else:
            return englishify(number//K) + ' Thousand, ' + englishify(number%K) 
    else:
        raise AssertionError("Integer is above specified range") #if integer is above 999999
"""		
		"# PLEASE WRITE TEST CASES HERE. YOU MAY USE MULTIPLE FIELDS."
    print(englishify(-200))
    print(englishify(3))
    print(englishify(4))
    print(englishify(7))
    print(englishify(89))
    print(englishify(57))
    print(englishify(212))
    print(englishify(478))
    print(englishify(908))
    print(englishify(5903))
    print(englishify(8923))
    print(englishify(59287))
    print(englishify(390762))
    print(englishify(982409))
    print(englishify(900006))
    print(englishify(100000002))
   ]
  },
  {
@ -92,6 +153,11 @@
   "metadata": {},
   "source": [
    "_You may write your explanation here._"
    Complexity of this algorithm is O(log(n)). The main motivation was a recursive algorithm to minimize the amount of times the function
    had to call itself. As the range of the integers was given in the problem, it was sufficient to stop at the thousands range. There are
    some cases where the expected output is not as natural especially when dealing with numbers in the high thousands and low singles
    e.g: 900006 where the output is given as 'Nine Hundred Thousand, Six'. These are the cases that need further tweaking as it should be
    'And' instead of the comma. 
   ]
  }
  """