filename = 'python.txt'

with open (filename) as file_object:
    lines = file_object.readlines()
    

for line in lines:
    new_line = line.replace('python', 'C')
    print(new_line.rstrip())