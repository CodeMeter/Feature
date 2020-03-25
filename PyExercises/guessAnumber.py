answer = 21

# this is just a sample answer and guess
guess = int(input("Guess your number: "))

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"
print(result)
