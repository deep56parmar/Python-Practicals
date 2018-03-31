import math
#Linear Search
list = [1,2,3,4,23,45,67,1,7,9,43,65,78,76,45,3,54,234,35,23,6,76,97,98,45,12,213,16,17,18,15,16,14,9,0,86,75,64,534,43,23,53,64,42,34,10]
def search(lists,num):
    found = False
    count = 0
    for i in list:
        count += 1
        if i == num:
            found = True
            break
        else :
            pass
    if found:
        return count
    if not found:
        print("not found")
        return -1
print(search(list,234))
print(search(list,12233))

#Bucket sort

def sort(array, bucketSize=10):
  if len(array) == 0:
    return array
  minValue = array[0]
  maxValue = array[0]
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
    elif array[i] > maxValue:
      maxValue = array[i]
  bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
  buckets = []
  for i in range(0, bucketCount):
    buckets.append([])
  for i in range(0, len(array)):
    buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])
  array = []
  for i in range(0, len(buckets)):
    buckets[i].sort()
    for j in range(0, len(buckets[i])):
      array.append(buckets[i][j])
  return array

print(sort(list))
