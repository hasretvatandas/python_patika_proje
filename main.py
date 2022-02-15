"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""
input = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]

def flatten_array(array):
    flat_array = []
    for item in array:
        if isinstance(item, list):
            # kendi kendini cagiran fonksiyon (recursive function)
            # extend ile listeyi genisletiyoruz, iki listeyi birlistiriyoruz
            flat_array.extend(flatten_array(item))
        else:
            flat_array.append(item)
    return flat_array

print(flatten_array(input))


"""
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""
input2 = [[1, 2], [3, 4], [5, 6, 7]]
def reverse_func(array):
    answer = []
    for liste in array:
        liste.reverse()  # liste içinde bulunan arrayler sırası değişiyor.
        answer.append(liste)
    answer.reverse()  # liste sırası değişiyor.
    return answer

print(reverse_func(input2))
