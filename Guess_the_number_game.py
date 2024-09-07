import random
number=random.randint(1,100)
attempt=1
while True:
    try:
        guess=int(input('guess a number'))
    except ValueError:
        print('Invalid value')
        continue

    if guess==number:
        print(f"You guessed the {number} right")
        print(f"You took {attempt} no. of attempt")
            
        break
    if guess>number:
        print("guess lower....")
        attempt+=1
    if guess<number:
        print("guess higher.....")
        attempt+=1      
