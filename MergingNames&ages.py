#Q3

names = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen',
         'Irene', 'Jack', 'Kelly', 'Larry']
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]


#Crating class for storing name and age for each person
class dictionary:
    def __init__(self, d_name, d_age):
        self.d_age = d_age
        self.d_name = d_name


#Creating combined list by the two lists
def combine_lists(c_name, c_age):
    people_list1 = list()
    for i in range(len(c_name)):
        person = dictionary(c_name[i], c_age[i])
        people_list1.append(person)
    return people_list1


#Finding people with the same age in the list and printing their names
def people(p_age):
    p_list = combine_lists(names, ages)
    age_list = list()
    for i in range(len(p_list)):
        if p_list[i].d_age == p_age:
            age_list.append(p_list[i].d_name)
    return age_list


#testing
print('is Dan and Cathy are 18 years old?')
print('Dan' in people(18) and 'Cathy' in people(18))
print('is Ed, Helen, Irene, Jack and Larry are 19 years old?')
print('Ed' in people(19) and 'Helen' in people(19) and 'Irene' in people(19) and 'Jack' in people(
    19) and 'Larry' in people(19))
print('is Alice, Frank and Gary are 20 years old?')
print('Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20))
print('is Bob 21 years old?')
print(people(21) == ['Bob'])
print('is Bob, Dan and Kelly are 21 years old?')
print(people(21) == ['Bob', 'Dan', 'Kelly'])
print('no one is 23 years old?')
print(people(23) == [])
