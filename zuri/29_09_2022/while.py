sum_of_number = 0
counter = 0

while True:
    counter+=1
    if counter == 100:
        print("100 is your answer")
        continue
    elif counter == 150:
        break
    else:
        print("i dont think it is correct")
    print(f"the increasing the values: {counter}")