f = open("datetime_example.py")
# print(type(f))
# print(f.read())
f.close()

print("________________________________________")


# with open("os_module.py") as f:
#     print(f.read())

print("________________________________________")


# with open("random_module.py") as f:
#     # for _ in range(10):
#         # print(f.readline())
#         # ten_lines = f.read()
#     ten_lines = f.readline()
#     sec_lines = f.readline()
#     print(fr"{ten_lines}")
#     print(fr"{sec_lines}")
#     rest_of_the_lines = f.readline()
#     print(rest_of_the_lines)
#     for item in rest_of_the_lines:
#         if item[0] == "\\" and item[1] == "n":
#             rest_of_the_lines.remove(item)
#     print("=================================")
#     print(rest_of_the_lines)


# with open("example.txt",'w') as f:
#     f.write("the text or data whatever is passed here be it with \nor not")
#     f.write("D:\practise_code\pythonProject\important_modules\venv\Scripts\python.exe D:\practise_code\pythonProject\important_modules\file_handling_examples.py ")
#
# data = ["items1","some names","somedata","which needs to stored in file"]
# with open("filename.txt","w") as f:
#     f.writelines(data)

# with open("indian_team.txt") as rf:
#     with open("new_team.txt",'w') as wf:
#         all_content_of_rf = rf.read()
#         wf.write(all_content_of_rf)


with open("indian_team.txt",'a') as af:
    af.write("rahuldravid")
    af.write("sourav gangulay")

# rb-
# wb-
# ab-

# with open("3b.jpg","rb") as rf:
#     with open("new 3b.jpg", "wb") as wf:
#         wf.write(rf.read())
#         data = rf.read()
#         print(data)
#         wf.write(data)

# with open("3b.jpg","rb") as rf:
#     with open("new 3b.jpg", "ab") as wf:
#         wf.write(rf.read())
#         data = rf.read()
#         print(data)
#         wf.write(data)


# with open("indian_team.txt","r+") as f:
#     print(f.read())


# with open("indian_team.txt", "w+") as f:
#     f.write("\ntest")
#     f.write("\ntest1")
#     f.write("\test2")
#     f.seek(0)
#     print(f.read())

with open("indian_team.txt","r+") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    f.seek(0)
    print(f.readline())
    print(f.readline())
    print(f.readline())









