# intialize variables
l = int(0) # number of aliens that land originally
w = int(0) # number of weeks the sliens have been on earth 
p = int(0) # the population of aliens based on the users imput
wkDisp = str("week")

# introduction
print(" Welcome to your Alien counter where we determine the population of aliens ")
print("based on the inputs for the number of aliens landed ")
print("and how long they've been on earth that you type.")

week = False
while week == false:
    try:
        w = int(input ("[Please Give a Positive Integer] "))
#Q1
print()
print ("How many aliens have landed on earth")
l = int(input ("[ Please Give a Positive Integer] "))
if l > 0:
    print()
    
   #Q2
    print("How long have the aliens been on earth (This Will Be Determined In Weeks)")
    w = int(input ("[Please Give a Positive Integer] "))
    if w > 0:
        print()
        for i in range (w):
            print( "After", i , wkDisp, "the alien population will be" , round(l * (2)**i), ".")
            if i == 1:
                wkDisp = "weeks"
    else:
        print ( "try agin using a positive integer!")
           
else:
    print ( "try agin using a positive integer!")
