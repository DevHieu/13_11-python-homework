def read_file(file):
  with open(file, "r") as read:
    data = read.readlines()
  t = data[0]
  data.pop(0)
  data = list(int(a.strip()) for a in data)
  return data,int(t)

def write_file(file, ans):
  arr = "\n".join(ans)
  with open(file,"w") as write:
    write.write(arr)

def TimUoc(n):
  times = 0
  for j in range(1,n+1):
    if n%j == 0:
      times +=1
  return times

def chanle():
  data, t = read_file("UOCCHANLE.INP")

  arr = []
  for i in range(t):
    times = TimUoc(data[i])
    if times %2 == 0:
      arr.append("CHAN")
    else:
      arr.append("LE")
  write_file("UOCCHANLE.OUT", arr)

if __name__ == "__main__":
  chanle()