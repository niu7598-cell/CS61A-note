# def print_sum(x):
#     print(x)
#     def next_sum(y):
#         return print_sum(x+y)
#     return next_sum

# print_sum(1)(3)(2)
# def split(n):
#     return n//10,n%10
# def sum_digits(n):
#     if n<10:
#         return n
#     else:
#         all_but_last,last= split(n)
#         return sum_digits(all_but_last) +last 
# print(sum_digits(114514))



# def inverse_cascade(n):
#     grow(n)
#     print(n)
#     shrink(n)


# def f_then_g(f,g,n):
#     if n:
#         f(n)
#         g(n)
# grow= lambda n : f_then_g(grow,print,n//10)
# shrink= lambda n : f_then_g(print,shrink,n//10)
    
# inverse_cascade(1234)

# def count_partitions(n, m):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0
#     elif m == 0:
#         return 0
#     else:
#         with_m = count_partitions(n - m, m)
#         without_m = count_partitions(n, m - 1)
#         return with_m + without_m

# result = count_partitions(5, 3)

# print(result)
# def index(key,values,match):
#     return {k: values for k in key if match }
k=['ikl','nba','3mz']
print('nba' in k)