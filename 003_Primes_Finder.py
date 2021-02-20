################# PRIME NUMBER FINDER #################

n = 1000000 #Upper bound
number_range = set(range(2 , n + 1))  #Inside range we specify uper bound and lower bound
prime_list = [] #Used list to store prime numbers

while number_range:             #Loop will run till all the number_range elements are iterated
    prime= number_range.pop()   #Reomve first element from number_rangw which is 2 initially
    prime_list.append(prime)    #For adding the popped value in the list of primes
    multiples= set(range(prime * 2, n + 1, prime)) #For calculating multiples from the prime 
    number_range.difference_update(multiples)      #For removing the items that are available in both sets(number_range and muliples)

print(prime_list)                #For printing the list of prime numbers
prime_count= len(prime_list)     #For printing the total number of elements in the list of prime numbers
largest_prime= max(prime_list)   #For printing the maximum number from the list of prime numbers
print(f" There are {prime_count} prime numbers between 2 and {n}, the largest of which is {largest_prime}") #f is used for printing the text along with some data values which are specified in {}