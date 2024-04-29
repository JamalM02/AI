#Q2

#Given Lists
List1 = [x ** 2 for x in range(5, 12)]
List2 = [x + y for x in [10, 20, 30, 40] for y in [1, 2, 3, 4]]
print("Given List1", List1)
print("Given List2", List2)


#Genarating the same lists in new ways
def list1(f, i, n):
    new_list1 = list()
    for x in range(i, n + 2):
        new_list1.append(f(x))
    return new_list1


def list2(f, x, y):
    new_list1 = list()
    for i in range(len(x)):
        for j in range(len(y)):
            new_list1.append(f(x[i], y[j]))
    return new_list1


#f1(x)=x**2
def f1(x):
    return x ** 2


#f2(x,y)=x+y
def f2(x, y):
    return x + y


#results
print("New Generated List1", list1(f1, 5, 10))
print("New Generated List2", list2(f2, [10, 20, 30, 40], [1, 2, 3, 4]))
