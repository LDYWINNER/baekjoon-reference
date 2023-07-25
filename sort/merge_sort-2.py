# 병합 결과를 담을 새로운 배열을 매번 생성해서 리턴하지 않고, 
# 인덱스 접근을 이용해 입력 배열을 계속해서 업데이트하면 메모리 사용량을 
# 대폭 줄일 수 있습니다. (In - place sort)

def merge_sort(arr):
  def sort(low, high):
    if high - low < 2:
      return
    mid = (low + high) // 2
    sort(low, mid)
    sort(mid, high)
    merge(low, mid, high)

  def merge(low, mid, high):
    temp = []
    l, h = low, mid

    while l < mid and h < high:
      if arr[l] < arr[h]:
        temp.append(arr[l])
        l += 1
      else:
        temp.append(arr[h])
        h += 1
    
    while l < mid:
      temp.append(arr[l])
      l += 1
    
    while h < high:
      temp.append(arr[h])
      h += 1
    
    for i in range(low, high):
      arr[i] = temp[i - low]
    
  return sort(0, len(arr))