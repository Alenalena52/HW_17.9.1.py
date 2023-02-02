# На входе получаем последовательность чисел и сразу преобразовываем ее в список
arr = [int(x) for x in input("Введите целые числа от 0 до 10000 через пробел: ").split()]

# Для сортировки списка по возрастанию применим метод сортировки слиянием
def merge_sort(arr):  
    if len(arr) < 2:  # если в массиве меньше 2 элементов,
        return arr[:]  # возвращаемся
    else:
        middle = len(arr) // 2  # иначе делим список пополам
        left = merge_sort(arr[:middle])  # рекурсивно делим левую часть списка, реализуем срез
        right = merge_sort(arr[middle:])  # рекурсивно делим правую часть списка
        return merge(left, right)  

# применим функцию для объединения двух списков
def merge(left, right):
    c = []  # задаем список
    i, j = 0, 0 # определяем два указателя, которые будут указывать на первые элементы списков left и right соответственно

    while i < len(left) and j < len(right): # пока i не превысит длину списка left и j не превысит длину списка right
        if left[i] < right[j]: # проверяем, кто из элементов меньше
            c.append(left[i]) # то в список с мещаем i элемент из списка left
            i += 1 # и двигаем указатель i на единицу
        else:
            c.append(right[j]) # иначе в список с помещаем j элемент из списка left
            j += 1 # и двигаем указатель j на единицу

    while i < len(left):
        c.append(left[i])
        i += 1

    while j < len(right):
        c.append(right[j])
        j += 1

    return c

print(merge_sort(arr))


def binary_search(arr, num, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if arr[middle] == num:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif num < arr[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(arr, num, left, middle - 1)
    else:  # иначе в правой
        return binary_search(arr, num, middle + 1, right)


while True:
    try:
        num = int(input("Введите целое число от 1 до 9999: "))
        if num < 0 or num >= 9999:
            raise Exception
        break
    except ValueError:
        print("Ошибка ввода. Введите целое число")
    except Exception:
        print("Ошибка ввода. Введите число от 1 до 9999")


print(binary_search(arr, num, 0,  len(arr)))
