#ham nac danh
# lamda argument
testlamda = lambda x:x+48
# testlamda (60)
print(testlamda(80))
list_lamda = [1,-1,0,-3,4,-5,9]
print(sorted(list_lamda,key=lambda x: abs(x)))
list_coor = [(0,5),(1,-6),(-1,5),(-4,5)]
print(sorted(list_coor,key=lambda x: x[1]))
