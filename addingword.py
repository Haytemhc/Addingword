import fileinput
word2num = {}
num2word = {}

for line in fileinput.input():
    cmd = line.rstrip().split(" ")
    answer = ""
    undefined = False
    if cmd[0]=="def" :
        if (cmd[1] != "unkown"):
            if cmd[1] in word2num: num2word.pop(word2num[cmd[1]])
            if cmd[2] in num2word: word2num.pop(num2word[cmd[2]])
            word2num[cmd[1]] = cmd[2]
            num2word[cmd[2]] = cmd[1]

    elif cmd[0] == "calc":
        counter = 1
        for i in cmd[1:-1]:
            try:
                answer += i if (counter%2) == 0 else word2num[i]
            except:
                undefined = True
            counter += 1
        print(" ".join(cmd[1:]), end=" ")
        try:
            if (undefined):
                print("unknown")
            else:
                print(num2word[str(eval(answer))])
        except:
            print("unknown")
    elif cmd[0] == "clear":
        word2num = {}
        num2word = {}
