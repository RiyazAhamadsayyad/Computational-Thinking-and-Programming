#Exp1
def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid]
        R = a[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        a[k:] = L[i:] + R[j:]


a = [38, 12, 27, 43, 9, 31]
print("Before:", a)

merge_sort(a)

print("After:", a)
