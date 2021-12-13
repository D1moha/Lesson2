#0 - создаём список
list0 = [1, 3, 3, 4] #ключ 3
list1 = [2, 1, 3, 5] #ключ 1
list2 = [4, 0, 1, 7] #ключ 0
list3 = [5, 2, 1, 0] #ключ 2
list4 = [0, 4, 8, 3] #ключ 4
listOriginal = [list0, list1, list2, list3, list4]
print ("Исходный список:", listOriginal)
print ("- - -")

#1 - сортируем список по возрастанию
listSortByAscending = sorted(listOriginal, key = lambda x: x[1]) #сортируем список по второму элементу (по возрастанию)
print ("1. Список по возрастанию:", listSortByAscending) #выводим список
print ("- - -")

#2 - создаём словарь
dicNew = dict(zip([x.pop(1) for x in listSortByAscending], [x for x in listSortByAscending])) #создаём словарь, где ключ - это второй элемент списка, а значения - остальыне элементы 
print ("2. Словарь:", dicNew) #выводим словарь
print ("- - -")
    
#3 - сортируем значения в словаре по убыванию
dicValues = list(dicNew.values()) #выбираем значения из словаря в виде списка
for x in dicValues:
    x.sort(reverse = True) #сортируем значения по убыванию
dicSortValuesByDescending = dict(zip(dicNew.keys(),dicValues)) #формируем словарь с отсортированными значения
print ("3. Словарь со значениями по убыванию:", dicSortValuesByDescending) #выводим словарь
print ("- - -")

#4 - получаем множество из всех значений словаря
setDicValues = dicSortValuesByDescending.values() #выбираем значения из словаря
setNew = set([item for sublist in setDicValues for item in sublist]) #формируем множество
print("4. Множество из значений словаря:", setNew) #выводим множество
print ("- - -")

#5 - преобразуем множество в строку
strNew = ''.join(map(str,setNew)) #формируем строку из элементов множества, меняя тип каждого элемента, без разделителя
print ("5. Строка:", strNew)
