

def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    
    # Boş liste veya yalnızca bir eleman içeren liste durumları
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    
    while low <= high:
        mid = (low + high) // 2
        
        # Listenin sınırları dışına çıkmadığımızdan emin olalım
        # ve sol ve sağ fark değerlerini elde edelim
        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)
        
        # Sol ve sağ elemanlar arasındaki mutlak değer farkının,
        # daha önce gördüğümüzden küçük olup olmadığını kontrol edelim
        if mid > 0 and min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid-1]
        if mid + 1 < len(A) and min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid+1]
        
        # İkili arama mantığına göre orta noktayı hareket ettirelim
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # Eğer eleman hedefin kendisiyse, en yakın sayı kendisidir
        else:
            return A[mid]
    
    return closest_num

# Örnek liste ve hedef
A = [2, 5, 6, 7, 8, 8, 9]
target = 4
result = find_closest_num(A, target)
print(result)  # Beklenen sonuç: 5
