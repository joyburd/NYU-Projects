#Joy Burkart, Assignment 9
#generates 100 random donation numbers, each donated to a random charity

#sprinkling the chicken blood
import random

#i'm just gonna go ahead and prime all the arrays i know i'll need
donations = [0]*100 #logs each donation individually
charities = [0] *100 #logs which charity the donation was given to in the corresponding space

totals = [0]*15 #totals for each charity
num_don = [0]*15 #number of donations to each charity



#PART 1- A TALE OF TWO ARRAYS

#for loop to get 100 donations
for donation in range(100):

    #print statment: numbering donations for... i dunno, posterity
    print("#", donation+1, ": ", end="")
    #adding one to the donation number bc it's a prettier list that way
    #but also keeping in mind the list is really 0-99, corresponding to the positions in the arrays
    
    #print statement: opening
    print("A donation of ", end="")

    #generating random float
    d = random.uniform(1.00,100.00)
    #putting that number in the donations array
    donations[donation] = d

    #print statment: donation
    print("$%3.2f" % d, " was made to ", end="")

    #generating random charity
    c = random.randint(0, 14)  #range set this way to correspond to an upcoming array
    #logging charity number in charities array
    charities[donation] = c

    #print statement: charity
    print("charity number", c+1)
    #adding to the generated number because that will realistically correspond to the array position to be designated in ~la futura~



#PART 2- CHARITIES GET THEIR $$$

#another for loop to sort the data into the totals and number of donations arrays
for total in range(100):

    #IF STATEMENTS
    #starting a series of if statements to count charity totals/fill preprimed arrays
    
    #if statement checks number of charity in position corresponding to the donation
    if charities[total] == 0:
    #so if the number there is 0, correesponding to charity in position zero of the fifteen position arrays (aka, charity 1)

        #this could probably just as easily be "charities[total]"
        totals[0] += donations[total] #adds to total in array position corresponding to charity
        num_don[0] += 1 #adds to count, in the num-don array

    #etc etc so on whathaveyou
    elif charities[total] == 1:
    
        totals[1] += donations[total]
        num_don[1] += 1

    elif charities[total] == 2:
        totals[2] += donations[total]
        num_don[2] += 1

    elif charities[total] == 3:
        totals[3] += donations[total]
        num_don[3] += 1

    elif charities[total] == 4:
        totals[4] += donations[total]
        num_don[4] += 1

    elif charities[total] == 5:
        totals[5] += donations[total]
        num_don[5] += 1

    elif charities[total] == 6:
        totals[6] += donations[total]
        num_don[6] += 1

    elif charities[total] == 7:
        totals[7] += donations[total]
        num_don[7] += 1

    elif charities[total]== 8:
        totals[8] += donations[total]
        num_don[8] += 1

    elif charities[total] == 9:
        totals[9] += donations[total]
        num_don[9] += 1

    elif charities[total] == 10:
        totals[10] += donations[total]
        num_don[10] += 1

    elif charities[total] == 11:
        totals[11] += donations[total]
        num_don[11] += 1

    elif charities[total] == 12:
        totals[12] += donations[total]
        num_don[12] += 1

    elif charities[total] == 13:
        totals[13] += donations[total]
        num_don[13] += 1

    elif charities[total] == 14:
        totals[14] += donations[total]
        num_don[14] += 1

print()

#PART 3- AVERAGES/TOTALS
#i'm going to go on an use an array for the next part too
#which I'm priming here
averages = [0]*15

#for loop to go though all the charities
for x in range(15): #i chose x because it's less annoying 2 write

    #Finding Total For Charity
    #again, charity number is variable+1, because this corresponds to the position in the array (x does. x+1 keeps there from being a charity 0)
    print("Total for charity number ", x+1, " is ", end="")
    print("%3.2f" % totals[x], ".")

    #Finding Average
    print("The average amount donated to this charity was ", end="")
    #converts number of donations in the corresponding num_don spot to a float
    y = float(num_don[x])
    #checks just in case there were no donations to this one (ergo, the number was not randomly generated)
    if y != 0:
        #so long as the number was randomly generated at least once, finds the average
        z = totals[x]/y
    else:
        #else the average is just zero, and no one has to divide by zero, and we all have a good time
        z = 0
    #putting this info in an array for easy access
    averages[x] = z
    #Print Statement: Average
    print("%3.2f" % z, ".")
    
    #a space after this info printed per charity
    print()

#a space (really, a double space, given the last one) to seperate next bit
print()

#PART 4- YOUR AVERAGE NONSENSE

#for loop going through alllllll the data again
for x in range(100):
    
    #Print Statement: Opening Statement for each donation
    print("Donation number ", x+1, " of $%3.2f" % donations[x]," for charity number ", end='')

    #checks charity spot coresponding to each donation (way back in the first, 100 spot arrays)
    if charities[x] == 0:

        #Print Statement: Prints Realistic Charity Number
        print(charities[x]+1, end="")

        #grabs donation and compares it to average
        #if it's greater, will subtract average from donation
        if donations[x] > averages[0]:

            #Print Statement: Priming for Difference From Average
            print("was greater than the average by ", end="")

            #finds difference
            y = donations[x] - averages[0]

            #Print Statement: Difference from Average
            print("%3.2f" % y, ".")

        #if donation is equal to average (for example: if there was only one donation)
        elif donations[x] == averages[0]:

            #just prints the average, which is also the value of the donation
            print(" was equal to the average of ", averages[0])

        #if donation is less than the average
        elif donations[x] < averages[0]:

            #Print Statement: Priming for Difference
            print(" was less than the average by ", end="")

            #Subtracts donation from Average
            y = averages[0] - donations[x]

            #Print Statement: Difference from Average
            print("%3.2f" % y, ".")

    #etc etc so on
    elif charities[x] == 1:

        print(charities[x]+1, end="")
    
        if donations[x] > averages[1]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[1]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[1]:

            print(" was equal to the average of ", averages[1])

        elif donations[x] < averages[1]:

            print(" was less than the average by ", end="")
            y = averages[1] - donations[x]
            print("%3.2f" % y, ".")
            
    elif charities[x] == 2:

        print(charities[x]+1, end="")

        if donations[x] > averages[2]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[2]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[2]:

            print(" was equal to the average of ", averages[2])

        elif donations[x] < averages[2]:

            print(" was less than the average by ", end="")
            y = averages[2] - donations[x]
            print("%3.2f" % y, ".")


    elif charities[x] == 3:

        print(charities[x]+1, end="")
        
        if donations[x] > averages[3]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[3]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[3]:

            print(" was equal to the average of ", averages[3])

        elif donations[x] < averages[3]:

            print(" was less than the average by ", end="")
            y = averages[3] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 4:

        print(charities[x]+1, end="")

        if donations[x] > averages[4]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[4]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[4]:

            print(" was equal to the average of ", averages[4])

        elif donations[x] < averages[4]:

            print(" was less than the average by ", end="")
            y = averages[4] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 5:

        print(charities[x]+1, end="")

        if donations[x] > averages[5]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[5]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[5]:

            print(" was equal to the average of ", averages[5])

        elif donations[x] < averages[5]:

            print(" was less than the average by ", end="")
            y = averages[5] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 6:

        print(charities[x]+1, end="")

        if donations[x] > averages[6]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[6]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[6]:

            print(" was equal to the average of ", averages[6])

        elif donations[x] < averages[6]:

            print(" was less than the average by ", end="")
            y = averages[6] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 7:

        print(charities[x]+1, end="")

        if donations[x] > averages[7]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[7]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[7]:

            print(" was equal to the average of ", averages[7])

        elif donations[x] < averages[7]:

            print(" was less than the average by ", end="")
            y = averages[7] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x]== 8:

        print(charities[x]+1, end="")

        if donations[x] > averages[8]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[8]
            print("%3.2f" % y, ".")
        
        elif donations[x] == averages[8]:

            print(" was equal to the average of ", averages[8])

        elif donations[x] < averages[8]:

            print(" was less than the average by ", end="")
            y = averages[8] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 9:

        print(charities[x]+1, end="")

        if donations[x] > averages[9]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[9]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[9]:

            print(" was equal to the average of ", averages[9])

        elif donations[x] < averages[9]:

            print(" was less than the average by ", end="")
            y = averages[9] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 10:

        print(charities[x]+1, end="")

        if donations[x] > averages[10]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[10]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[10]:

            print(" was equal to the average of ", averages[10])

        elif donations[x] < averages[10]:

            print(" was less than the average by ", end="")
            y = averages[10] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 11:

        print(charities[x]+1, end="")

        if donations[x] > averages[11]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[11]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[11]:

            print(" was equal to the average of ", averages[11])

        elif donations[x] < averages[11]:

            print(" was less than the average by ", end="")
            y = averages[11] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 12:

        print(charities[x]+1, end="")

        if donations[x] > averages[12]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[12]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[12]:

            print(" was equal to the average of ", averages[12])

        elif donations[x] < averages[12]:

            print(" was less than the average by ", end="")
            y = averages[12] - donations[x]
            print("%3.2f" % y, ".")
            
    elif charities[x] == 13:

        print(charities[x]+1, end="")

        if donations[x] > averages[13]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[13]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[13]:

            print(" was equal to the average of ", averages[13])

        elif donations[x] < averages[13]:

            print(" was less than the average by ", end="")
            y = averages[13] - donations[x]
            print("%3.2f" % y, ".")

    elif charities[x] == 14:

        print(charities[x]+1, end="")

        if donations[x] > averages[14]:
            
            print(" was greater than the average by ", end="")
            y = donations[x] - averages[14]
            print("%3.2f" % y, ".")
            
        elif donations[x] == averages[14]:

            print(" was equal to the average of ", averages[14])

        elif donations[x] < averages[14]:

            print(" was less than the average by ", end="")
            y = averages[14] - donations[x]
            print("%3.2f" % y, ".")
