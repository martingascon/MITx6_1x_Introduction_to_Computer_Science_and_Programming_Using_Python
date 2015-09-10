low = 0
mid = 50
high = 100
print"Please think of a number between 0 and 100!"
print "Is your secret number: " + str(mid) + "?"
guess = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while guess != 'c':
    if guess == 'h':
        high = mid
        mid = int((mid + low)/2)
    elif guess == 'l':
        low = mid
        mid = int((mid + high)/2)
    else:
        print "wrong input."
    print "Is your secret number: " + str(mid) + "?"
    guess = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if guess == 'c':
    print "Game over. Your secret number was:", mid