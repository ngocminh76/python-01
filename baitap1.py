#tạo ra 1 list chưa các số từ 1 đến 5
mylist = [1,2,4,5,6]
print("Phần tử thứ 3 của danh sánh là ", mylist[2])
print("Phần tử cuối cùng của danh sánh là ", mylist[-1])
# tính tổng các phần tử trong list
def calculate_sum(lst):
    return sum(lst)

# nhập vào danh sách list từ người dùng
user_list = [int(x) for x in input("Nhập vào các số nguyên ( cách nhau bở dấu cách )").split()]

print(calculate_sum(user_list))
# bài 3: tìm list chưa các số chẵn
def even_indices(lst):
    return lst[::2]
# list ban đầu
ori_list = [1,2,3,4,5,6,7,8]
# tạo 1 list mới chỉ chứa các phần tử số chẵn
result = even_indices(ori_list)
print(result)
#Bài tập 4: Sắp xếp list
#Viết một chương trình yêu cầu người dùng nhập vào một list các số nguyên, 
# sau đó sắp xếp list này theo thứ tự tăng dần và in ra kết quả.
def sort_list(lst):
    lst.sort()
    return lst
# nhập danh sách người dùng
user_list =[int(x) for x in input("Nhap vao danh sach :").split()]
print(sort_list(user_list))

# giải theo cách khác, ko sử dụng hàm có sẵn
def buble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            # so sánh 2 phần tử liền kề và hoán đổi khi cần thiết
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]= lst[j+1]
                lst[j+1]=temp
                # lst[j],lst[j+1]= lst[j+1],lst[j]
                # swapped=True
        # nếu không thực hiện được sự hoán đổi nào đó, thì dừng swapped
        if not swapped:
            break
    return lst
#Bài tập 5: Đảo ngược list
def reverse_list(ls):
    return ls[::-1]
ori = [1,5,6,8,9,102]
print(reverse_list(ori))
#Bài tập 6: List comprehension
#Ví dụ:
#Input: [1, 2, 3, 4, 5]
#Output: [1, 4, 9, 16, 25]
def squrepow2(lst):
    return [x**2 for x in lst]
myl = [1, 2, 3, 4, 5]
outp = squrepow2(myl)
print(outp)

#Bài tập 7: List lồng nhau
#Tạo một list lồng nhau có tên nested_list chứa các list con [1, 2, 3], [4, 5, 6], [7, 8, 9].
#Truy cập và in ra phần tử 5 từ nested_list.
nest_list =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ele = nest_list[1][1]
print(ele)
# Bài tập 8: List comprehension lồng nhau
# Tạo một list lồng nhau mới chứa các bộ số (a, b)
# trong đó a là số chẵn trong khoảng từ 1 đến 3 và b là số lẻ trong khoảng từ 1 đến 3.
# Ví dụ:
# Output: [(2, 1), (2, 3)]
netl = [(a,b) for a in range(1,4) for b in range(1,4) if a%2==0 and b%2!=0]

print(netl)
# viết theo cách khác nè:
list_empt =[]
# vòng lặp
for a in range(1,4):
    if a%2==0:
        for b in range(1,4):
            if b%2!=0:
                list_empt.append((a,b))
print(list_empt)
#Bài tập 9: Sắp xếp list con trong list
#Cho một list các tuple chứa tên và điểm của một số học sinh:
#Hãy sắp xếp danh sách học sinh theo điểm từ cao đến thấp.
students = [("Alice", 85), ("Bob", 72), ("Cathy", 90), ("David", 78)]
result =(sorted(students,key=lambda x: x[1],reverse=True))
for std in result:
    print(f"{std[0]} : {std[1]} điểm")

#Bài tập 10: Chèn phần tử vào list
def insert_sorted(lst,n):
    for i in range(len(lst)):
        if lst[i]>n:
            lst.insert(i,n)
            return lst
    lst.append(n)
    return lst
sort_list01 = [2,4,5,6,71,4,41]
n =21
newlist = insert_sorted(sort_list01,n)
print(newlist)