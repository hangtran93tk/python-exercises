friends = ["Tran","Nguyen", "Dang"]

#Truy cập phần tử (lấy giá trị)
print(friends)
print(friends[0])

#Thêm một phần tử
friends.append("Hoang")
friends.insert(0,"Pham")
print(friends)

#Xóa một phần thử, lamda
del friends[1:2] #slicing
friends.pop(1)
friends.remove("Tra")
print(friends)
