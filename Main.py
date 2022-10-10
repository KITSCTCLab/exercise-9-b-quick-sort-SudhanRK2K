from typing import List

def partition(arr,low,high):
    pivot = arr[high]
    i = (low-1)
    for j in range (low,high):
        if arr[j]<pivot:
            i = i+1
            (arr[i],arr[j] = arr[j],arr[i])
    (arr[i+1],arr[high] = arr[high],arr[i+1])
    return i+1
            

def quick_sort(data, low, high) -> List[int]:
    # Write code here


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
