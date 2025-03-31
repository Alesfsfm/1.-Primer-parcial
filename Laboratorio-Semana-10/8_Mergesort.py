def merge(arr1, arr2):
    result= []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+= 1
        else:
            result.append(arr2[j])
            j+=1
    if i == len(arr1):
        for k in range(j, len(arr2)):
            result.append(arr2[k])
    elif j == len(arr2):
        for k in range(i,len(arr1)):
            result.append(arr1[k])
    return result

def merge_sort(arr):
    if len(arr)<2:
        return arr
    else:
        mid = (len(arr))//2
        arr1 = merge_sort(arr[:mid])
        arr2 = merge_sort(arr[mid:])
    return merge(arr1, arr2)

lista = list(map(float, input("Ingrese una lista de números separados por espacio: ").split()))

lista_ordenada = merge_sort(lista)
print("Su lista original es:", lista, "\n")
print("\nSu lista ordenada es:", lista_ordenada)