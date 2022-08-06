"""Task 1. 5 points"""

print('TASK1:')
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
spisok = [first, second, third, fourth, fifth]
new_dict = {}
for i in spisok:
    new_dict.update(i)
print(new_dict)

"""Task 2. 10 points"""
#square_key = {12: 144, 11: 121,  14: 196, 13: 169, 19: 361, 15: 225,  17: 289, 16: 256, 18: 324,  20: 400}
#print(sum(square_key.values()))

"""Task 3. 5 points"""
#print(sorted(square_key.keys()))

"""Task 4. 15 points"""

print('TASK4:')
new_dict1 = {'id1':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
},

'id2':
{
'name': 'Mark',
'class': 2,
'subjects' : {'Geometry', 'Java', 'Cooking'}
},

'id3':
{
'name': 'Ruslan',
'class': 1,
'subjects' : {'Math', 'Algorithms', 'English'}
}
}
new_dict2 = {}
for key, value in new_dict1.items():
    if value not in new_dict2.values():
        new_dict2.update({key: value})
print(new_dict2)


"""Task 5. 10 points"""

print('TASK5:')
new_set = set()
new_dict3 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
for v in new_dict3:
    for i in v.values():
        new_set.add(i)
print(new_set)

new_set1 = set()
new_dict4 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
new_dict4.reverse()
new_dict5 = {}
for v2 in new_dict4:
    new_dict5.update(v2)
print(new_dict5)

"""Task 6. 15 points"""

print('TASK6:')
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
shedule2 = {}
shedule3 = []
shedule2 = shedule.values()
print(shedule2)
for n in shedule2:
    if isinstance(n, list):
        for j in n:
            shedule3.append(j)
    else:
        shedule3.append(n)
print(shedule3)
shedule3.remove(None)
counter = 0
for values in shedule3:
    counter = counter +1
print(counter)

#Найти официальную документацию по Словарям и прикрепить ссылку к домашней работе 5 points
#https://docs.python.org/3/c-api/dict.html

"""Task 7. 10 Points"""
#https://www.sporcle.com/games/ruslanskira/built-in-dictionary-methods/results

"""Task 8. 25 Points"""
#Done
