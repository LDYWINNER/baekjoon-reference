# Time complexity: O(NlogN)
# 파이썬의 list slice notation을 사용하면 다음과 같이 간결한 코드를 작성할 수 있습니다. 
# 하지만 list slice를 할 때 list의 복제가 일어나므로 메모리 사용 효율은 좋지 않습니다. 


def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr) // 2
  low_arr = merge_sort(arr[:mid])
  high_arr = merge_sort(arr[mid:])

  merged_arr = []
  l = h = 0
  while l < len(low_arr) and h < len(high_arr):
    if low_arr[l] < high_arr[h]:
      merged_arr.append(low_arr[l])
      l += 1
    else:
      merged_arr.append(high_arr[h])
      h += 1
  
  merged_arr += low_arr[l:]
  merged_arr += high_arr[h:]
  return merged_arr

