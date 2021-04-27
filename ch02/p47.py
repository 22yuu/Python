
name = "홍길동"
age = 35
price = 125.456

print("이름 : {}, 나이 : {}, data={}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age, name, price))

# format 축약형
uid = input("id input :")
query = f"select * from member where uid = {uid}"
print(query)
