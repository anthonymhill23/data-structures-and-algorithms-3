def insertion_sort(list):
  for i in range(len(list)):
    j = i -1
    temp = list[i]

    while j >= 0 and temp < list[j]:
      list[j+1] = list[j]
      j -= 1

    list[j+1] = temp

  return list
