secret_no = 5
limit = 3  # number of chances to try for guess
i = 1
while i <= limit:
    u_input = int(input("Guess : "))
    i += 1
    if secret_no == u_input:
        print("You Guessed It Right...!!!")
        break  # without break, the while loop continues to ask "guess = ", even after the correct answer
else:  # as its defined to go upto limits = 3, so to break the loop, we add break
    print("Sorry...its incorrect")
