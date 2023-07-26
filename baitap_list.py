#Bài tập 1: Tổng các số trong list
#Viết một chương trình yêu cầu người dùng nhập vào một list các số nguyên,
#sau đó tính và in ra tổng của các số trong list.
# def calcu_sum(lst):
#    return sum(lst)
# mylist = [int(x) for x in input('Nhập vào các số nguyên ').split()]
# kq1 = calcu_sum(mylist)
# print(kq1)
#Bài tập 2: Đảo ngược list
#Viết một chương trình để đảo ngược một list. Hãy in ra list sau khi đã đảo ngược.
# bt2 = [1,4,5,2,10,3]
# def sortlist(lst):
#     res = lst.sort()
#     return res
# kq2 = sorted(bt2)
# print(kq2)
#Bài tập 3: Chèn phần tử vào list
#Viết một chương trình yêu cầu người dùng nhập vào một list và một số nguyên n.
# Sau đó, hãy chèn n vào đầu list và in ra list sau khi đã chèn.
# bt3 = [1,5,13,42]
# kq3 = bt2.append(3)
# bài tập 4: Bài tập 5: List chứa số nguyên tố
#Viết một chương trình yêu cầu người dùng nhập vào một list các số nguyên,
#  sau đó tạo một list mới chỉ chứa các số nguyên tố từ list ban đầu và in ra list mới này.
#Lưu ý: Để kiểm tra xem một số có phải là số nguyên tố hay không,
#  hãy kiểm tra xem nó chia hết cho 1 và chính nó. Số nguyên tố là các số lớn hơn 1 và không chia hết cho số nào ngoài 1 và chính nó.
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True


# def prime_numbers(lst):
#     return [num for num in lst if is_prime(num)]
# firstlist = [int(i) for i in input("Nhập vào danh sách các số nguyên :").split()]
# list_prime = [num for num in firstlist if is_prime(num)]
# check1 = prime_numbers(firstlist)
# print(list_prime)
# print(check1)
# print(5**0,5+1)
for i in range(10):
    if i != 4:
        print(i)

for i in range(10):
    if i == 4:
        continue
    print(i)

for i in range(10):
    print(i)
    if i == 4:
        break