filename = 'programming_responses.txt'

while True:
    response = input("Why do you like programming? (enter 'q' to quit): ")
    
    if response == 'q':
        break
    
    with open(filename, 'a') as file:
        file.write(response + '\n')
    
    print("Thanks for your response! Your answer has been recorded.")
