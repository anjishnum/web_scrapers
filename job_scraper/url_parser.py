with open('jobs.log','r') as file:
    contents = file.read()

word_list = contents.split(' ')

url_list = []

for word in word_list:
    if word[:4]=='Link':
        url_list.append(word[6:-1])

url_string = " ".join(url_list)

file =  open('url_file.txt'.'a+')
    
file.write(url_string)

file.close()
