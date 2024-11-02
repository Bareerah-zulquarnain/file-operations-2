with open("Codingal_txt.txt",'w') as file:
    file.write("hi iam a cat")
file.close()

with open("Codingal_txt.txt",'r') as file:
    data= file.readlines()
    print("word in this file are ...")
    for lines in data:
        word = lines.split() 
        print(word)
file.close()