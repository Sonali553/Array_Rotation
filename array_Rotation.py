lst = list(map(int, input().split()))
K = int(input())
def Array_Rotation(lst, K):
  n = len(lst)
  K = K % n
  def reverse(l, r):
    while(l < r):
        temp = lst[l]
        lst[l] = lst[r]
        lst[r] = temp
        l += 1
        r -= 1
    return lst
  reverse(0, n-1)
  reverse(0, K-1)
  reverse(K, n-1)
  return lst


print(Array_Rotation([1, 2, 3, 4],2))
print(Array_Rotation([2, 5, 6], 1))
print(Array_Rotation(lst, K))
