# intialize variables
l = int(0) # number of aliens that land originally
w = int(0) # number of weeks the aliens have been on earth 
p = int(0) # the population of aliens based on the users imput
wkDisp = str("week")                      
checkL = False # this is the condition for while loop
checkW = False # this is the condition for while loop

# introduction
print(" Welcome to your Alien counter where we determine the population of aliens ")
print("based on the inputs for the number of aliens landed ")
print("and how long they've been on earth that you type.")

#Q1
print()
print ("How many aliens have landed on earth") # users first question to answer

while checkL == False:     # while this condition is occuring
    try:                   # try nto do the following:                 
        l = int(input ("[ Please Give a Positive Integer] "))
                           # Get user's INTEGER answer to the question.
        if l > 0:          # if l is greater than 0 than print...
            print("Good ANSWER")   # Giving user feedback.
            checkL = True          # Trigger the escape condition for the while Loop.
        else:                      # If the user does not input an integer...
            print("That wasn't a good answer")  # giving user feedback
            # NO escape condition-->stay in while loop
    except ValueError:
        print("Maybe try somthing like a... Whole Number.") 
             # No escape conition --> stay in the while loop
#Q2
print("How long have the aliens been on earth (This Will Be Determined In Weeks)")
             # you only get to this line if you escape while Loop

while checkW == False: # while this condition is occuring..
    try:               # try to do the following
        w = int(input ("[Please Give a Positive Integer] "))
                       # Get users Integer to the question
        if w > 0:      # if w is greater than 0 than print...
            print("Great Answer") # giving user feedback
            checkW = True         # Trigger the escape condition for the while Loop.
        else:                     # If the user does not input an integer...
            print ( "try agin using a positive integer!")
                 # No escape conition --> stay in the while loop
    except ValueError:
        print("That wasnt a smart answer")
              # No escape conition --> stay in the while loop

#for loop 
for i in range (w): # for loop to decide the alien population
    print( "After", i , wkDisp, "the alien population will be" , round(l * (2)**i), ".")
    if i == 1: # if = 1 than it will represent week out of weeks
        wkDisp = "weeks" # week will become weeks after 1 week
