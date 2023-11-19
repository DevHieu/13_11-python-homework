def read_file(file):
  with open(file, "r") as read:
    data = read.readlines()
  value = data[0].split(" ")
  data.pop(0)

  thisinh = {}
  quest = []
  score = []

  for c in range(int(value[0])):    #list thí sinh
    thisinh[data[c].strip()] = 0

  for p in range(int(value[0]), int(value[0])+ int(value[1])):  #list câu hỏi
    quest.append(data[p].strip().split(" ")[0]) #Lấy tên bài
    score.append(data[p].strip().split(" ")[1]) #Lấy điểm
  
  for i in range(int(value[0])+ int(value[1])): #phần còn lại
    data.pop(0)

  return data, thisinh, quest, score

def write_file(file, ans):
  with open(file,"w") as write:
    write.write(ans)

def contest():
  ans = ""
  data, thisinh, quest, score = read_file("CONTEST.INP")
  
  for i in data:
    arr = i.strip().split(" ")
    if arr[0] in thisinh and arr[2] == "AC":
      thisinh[arr[0]] += int(score[quest.index(arr[1])])
  
  for k in thisinh:   #Đổi từ dict sang str để ghi vào file
    ans += (k +" "+ str(thisinh[k]) + "\n")

  write_file("CONTEST.OUT", ans)


if __name__ == "__main__":
  contest()