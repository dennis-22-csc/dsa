def half_list(mylist, index, sublist1, sublist2):
    if index < len(mylist):
        if index < 5:
            sublist1.append(mylist[index])
        else:
            sublist2.append(mylist[index])
        half_list(mylist, index + 1, sublist1, sublist2)

employees = ["Dennis Koko", "Lincoln Burrow", "Michael Scofield", "Nathan Petrelli", "Peter Petrelli", "Sarah Connor", "John Connor", "Raymond Gray", "Ryan Whitewater", "Jessica Roberts"]
print("Employees List: ", employees) 
start_index = 0
sublist1 = [] 
sublist2 = [] 
half_list(employees, start_index, sublist1, sublist2)
print("Sub List 1: ", sublist1)
print("Sub List 2: ", sublist2)
