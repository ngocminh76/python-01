# map
list_temp =[7,8,9,12]
def sum(x):
    return x+2
# áp dụng lamda
print(list(map(lambda x:x*2,list_temp)))
print(list(map(sum,list_temp)))