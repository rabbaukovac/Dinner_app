##Lab 2 part 2 added a few new functions


import random #import random

#First function which utilizes the Random Mod, random number rolled each time its called.  If random number
# is 2,3,6,8 then it prints the list to the user.
def destroyHumans():
    random_number = random.randint(1, 10)
    if random_number in {2, 3, 6, 8}:
        ai_list = '****destroy**** ***all*** ***humans*** '
        print(ai_list)


# the main function in our code, takes user inputs and utilizes if statements to produce a response.
def dinner():
    print('Hello what is your name?')
    destroyHumans()
    userName = input()
    print('Hello ' + userName + ' How old are you? Int only')
    destroyHumans()
    userAge = input()
    print('Do you want pizza or pasta for dinner tongiht?')
    destroyHumans()
    userDin = input()

    if int(userAge) >= 18:
        if userDin == 'pasta':
            print('Awesome! ' + userName + ' We are going to Olive Garden and ordering ' + userDin + ' tonight!')
            destroyHumans()
        elif userDin == 'pizza':
            print('I know a fancy ' + userDin + ' place with a special that includes drinks and a side!')
            destroyHumans()
        else:
            print('I have never made ' + userDin + ' before but we can go get grocries and make it!')
            destroyHumans()

    else:
        print('Sorry ' + userName + ', we need to ask my parents before we can get ' + userDin + ' tonight!')
        destroyHumans()

    print('Thanks for dinner!')
    destroyHumans()



# This was the final piece of the puzzle, using a while true statement to ask if anyone else wants to go to dinner.

# this was the hardest part by far for me, I still am a little confused on the try and finally part

def askAgain():
     while True:
         try:
             age = str(input('Does anyone else want to come to dinner? Yes or No'))
             if age == 'no':
                 print('That is too bad, good bye humans : )')
                 break

             elif age == 'yes':
                 dinner()
         finally:
             print(' ')



# I decided to use the random gen function rather than the for loop in this case but wanted to show this is how I was use it.
## rather than calling the random function in each case (destroyHumans) I would call "theLoop" function.


##def theLoop():
  ##  for i in range(random.randint(1, 5)):
    ##    print('yum ' + str(i))






# calling each function to run when the program starts.

dinner()
askAgain()
destroyHumans()