grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
studens = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

studens_list= sorted(studens)

exemple =[(sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])), (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])), (sum(grades[4]) / len(grades[4]))]

klass = {studens_list[0] : exemple[0], studens_list[1] : exemple[1], studens_list[2] : exemple[2], studens_list[3] : exemple[3], studens_list[4] : exemple[4]}
print(klass)
