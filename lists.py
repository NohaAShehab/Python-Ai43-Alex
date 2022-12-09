"""
    list
"""

"1- to define a list "
l = []
myl = list()
myll = list([])
print(l)

"2- list can hold different data from different types "
l = ["Ahmed", True, 2022, "iti", 3.14, ["machine learning01", "machine learning02"], "iti", "iti"]
print(l)
"3- you access list elements using index"
print(l[2])
print(l[5][1])

"3- list is mutable datatype"
l[1] = "Python"
# l[10] = "iti"  # list assignment index out of range
"4- get len of the list"
print(len(l))
"5- count no of occurance for element in the list "
print(l.count("iti"))
"6- get index of item in the list"
print(l.index("iti"))
"7- iterate over the list items ---> iti"
for item in l:
    print(f"item = {item}")
#
# for i in "noha":
#     print(i)

"8- append element to the list ---> add element to the end the of the list "
print(l)
l.append("appended item")
print(l)
"9- insert element at certain position"
l.insert(3, "inserted item")

"10- pop element from the list ---> "
popped_item = l.pop()  # remove the last element from the list
print(l, popped_item)

other_popped = l.pop(2)
print(l, other_popped)

"11- remove element ---> "
l.remove("iti")  # remove first occurrence from the list
print(l)

"12- check existance of the element"
print("itit" in l)

print("a" in "noha")

"13- sort the list --> the data must from the same type "
"""
    "A" >10  This operation is not allowed 
"""
l = ["Habiba", 'Mona', "Omar", "Basel", "Mohamed", "Rashed", "Ahmed", "andrew"]
# print(l)
# l.sort() ### sort the same list # ascending
# print(l)
# l.sort(reverse=True)
# print(l)

"14- reverse a list"
l = ["Ahmed", "iti", True, 3.14, 2022, [3, 4, 5]]
l.reverse()
print(l)

"15- list concatenation"
l1 = ["ml1", "CV", "introduction to AI", "Spark", 3.14]
l2 = ["Python", "DB", "NoSql", 2022, 3.14]
courses = l1 + l2  # return with new list
print(courses)

"16- extend ? "
l1.extend(l2)  # modify l1 object
print(l1)

"17- min , max ---> comparison ---> elements from the same type"
print(max([3,4,5]))

"18- empty is considered to be a falsy value"
ll = []
if ll:
    print('hi')
else:
    print("bye")

"19- split string to a list ---> according to delemiter "
info = "My name is Noha"
info_data = info.split(" ")
print(info_data)

content = ["test", "abc", "lala", "python"]
# newcontent = ""
# for item in content:
#     newcontent +=f" {item}"
# print(newcontent)
newcontent = "_".join(content)
print(newcontent)


"""
    input :  3
    
    [[1],[2,4], [3,6,9]]
"""