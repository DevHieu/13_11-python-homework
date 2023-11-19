def read_file(file):
  with open(file, "r") as read:
    data = read.readlines()
  n = int(data[0].split()[0])
  t = int(data[0].split()[1])
  data.pop(0)
  data = data[0].split(" ")
  return data,int(n),int(t)

def write_file(file, ans):
  with open(file,"w") as write:
    write.write(ans)

def ddc():
  data, n, t = read_file("DDC.INP")
  ans = 0

  prefix = []     #Tạo mảng prefix
  sum = 0
  for i in range(len(data)):
    sum += int(data[i])
    prefix.append(sum)

  key1 = 0
  key2 = 0
  while key1 <= n-1 and key2 <= n-1:
    if key2 != n-1:
      if prefix[key2] - prefix[key1] + int(data[key1]) <= t:
        print(key1, key2)
        ans +=1
        key2 +=1
      else:
        key1 +=1
        key2 = key1
    else:
      if prefix[key2] - prefix[key1] + int(data[key1]) <= t:
        print(key1, key2)
        ans +=1
        key1 +=1
      else:
        key1 +=1
        key2 = key1
  write_file("DDC.OUT", str(ans))


if __name__ == "__main__":
  ddc()