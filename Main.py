from typing import List

def partition(array,low,high):
    pivot = array[high]
    i = (low-1)
    for j in range (low,high):
        if array[j]<pivot:
            i++
            swap array[i] and array[j]
            

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
