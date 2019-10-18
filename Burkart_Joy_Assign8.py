#Assignment 8
#Joy Burkart
#this program will read in (prompt a user for) input until it comes across a !
#will also give a final count of letters a-z (capitalized or not)
#and a final count of other characters including spaces
#will also also tell you the letter(s) used most/least

#TODO
#move ! stuff around so it stops the program immediately when it sees this no matter where it's located
#generate lowest value

#COUNT
#count to stop while loop
stop = 0
#I did it this way because I needed my input within a while loop
#so that it would keep prompting for info and i couldn't tell until the user
#entered input if they would enter a "!" so I couldn't use ! as my stop variable
#and I also ended up needing an extra variable to stop the program
#from continuing to enter character values into the array after the "!" was entered
#if ! was entered in the middle of input

#PRIMING ARRAY
#variable so i'm not hard coding numbers in
#i guess this way if you wanted to add things you're counting (like numbers of symbols),
#having the variable set this way would make that transition smoother
v = 27

array = [0]*v #gives me an array with positions from 0-26
#extra one is for symbols including spaces, commas, numbers, anything that's not a letter
#or an exclamation point


#EXTRA VARIABLES
#which need to be here specifically outside my while loop
#becuase I am counting my vowels as the input is entered and
#the number of uses is logged into the araay

#for counting my vowels
vowelcount = 0

#for counting my consonants
consonantcount = 0

#PART 1-INPUT AND QUANTIFICATION
#am i using the word quantification right
#i feel like i should, as an english major, know this

#while loop, to keep prompting for input until "!" reached
while stop != 999:

    #input
    message = input("Input ur stuf: ") #not spelled correctly because I am trying to come off as casual and "hip," like I don't even care what you enter into my precious program

    #for loop to seperate and quantify/qualify letters in input, changed to upper because I like it like that
    for let in message.upper():

        #changes each letter into its ascii table value
        num = ord(let)

        #checks if the entry has an exclamation point for each character
        #becuase I only want it logging if the character isn't a !
        #AND a ! has not been found
        #33 is '!'s ascii table value
        #the 999 comes from the other half of this loop in which
        #stop will be set to that value when a ! is logged
        if num != 33 and stop != 999:
            
            #only counts if number is within range of A-Z
            if num >= 65 and num <= 90:
                
                #array position relative to letter being used (this is the minus 65 bit)
                #which was already qualified by the ord()
                #because setting it to the value from my for loop wouldn''t make any sense
                #or even necessarily reflect the number of spaces i've got in my array
                #which is set up to the number of letters in the alphabet
                #(i wrote this mostly to remind myself what I was doing please excuse it
                #for loops really... throw me for a loop)
                array[num-65] += 1

            #every other character pushed into a count in the extra space of my array
            #v-1 is that extra space, which is set to a constant
            #only problem with this is that if you want to count all the characters
            #individually and you're rewriting the program to do that, you'd have to
            #mess with this
            else:
                array[v-1] += 1

            #count for vowels and consonants, within the loop that checks if the character is a ! or not
            #becuase i don't want them counted unless there isn't a ! in front of them
            if num in [65, 69, 73, 79, 85]: #i'm not counting "y" as a vowel
                vowelcount+= 1
            #consonants
            elif num >= 65 and num <= 90:
                consonantcount += 1
        
        #this could probably just be an else but i'm uncomfortable with that
        elif num == 33:
           stop = 999
           #stops the while loop and the loop that's counting letter and character uses

#essentially this is a two layer loop
#one layer checks the stop variable and keeps prompting for input
#the other checks the stop variable and doesn't count the input (which has already been prompted for)
#they had to be seperate (as far as I'm concerned) so I could keep getting input
#I'm really bothered by the fact that I can't think of a way to consolidate that


#PART 2-PRINT OUT OF # OF USES

#range to tell you how often each individual letter, and any extra characters, were used
#set to v-1 becuase ranges and arrays are the way they are and if i don't do that the program gets mad at me
for let in range(v-2):

    #if only used once (this exists because I didn't want a plural on "time" if there was only one use)
    #sure I could have used "time(s)" but where's the fun in that if i can just program it in
    if array[let] == 1:
        print() #a space for nice formatting
        print("The letter ", chr(let+65), "was used 1 time.")

    #used in any instance where the character was used more than once
    elif array[let] >1:
        print()
        print("The letter ", chr(let+65), "was used ", array[let], "times.")

    #loop ignores characters that were never used

#checks for extra characters used
if array[v-1] == 1: #which i put in the last space (#26, or v-1)

    print()

    #only prints this if a single extra character is used (like one space or one comma in the entire input)
    print("Another character was used ", array[v-1], "time.")

#checks for any instance in which multiple extra chars were used, so it can use the plural of time
elif array[v-1] > 1:

    print() #formatting for cool kids

    #print out with time plural
    print("Other characters were used ", array[v-1], "times.")

#again, this is problematic if you're reprogramming for counting characters
    #but I guess you could always adapt these parts of the program for use in that instance
    #i'm gonna stop worrying about that, tbh
    #like i GUESS it's true that even if you do reprogram for counting all extra characters
    #this bit would be relatively harmless
    #or at least easier to deal with because of the use of a "v" variable instead of a hard coded number
    #this bit will, instead, just constantly refer to the last space in your array


#PART 3- EXTRA VARIABLE COUNTS
#i made this way more complicated than it has to be
#just a fair warning

#VOWELS
#starts by checking to see how many consonants (counterintuitively)
#bc it needs to know what form of print out to use
if consonantcount == 0:

    #if there are no consonants and only one vowel (ex input: a!)
    if vowelcount== 1:
        print("There was 1 vowel.")

    #if there are no consonants and multiple vowels (ex input: a!)
    elif vowelcount >1:
        print("There were ", vowelcount, "vowels.")

#still in vowel printouts, now entering print outs that also consider consonants
elif consonantcount >0: #if there are ANY consonants at all

    #if there are consonants and only one vowel (ex input: ab!)
    if vowelcount == 1:
        print("There was 1 vowel and ", end="")

    #if there are consonants and multiple vowels (ex input: aab!)
    elif vowelcount > 1:
        print("There were ", vowelcount, "vowels and ", end="")

#CONSONANTS
#checking vowel count
#i could have collapsed these if/else loops a lot but i felt like
#they were easier to read this way
#also i'm tired
#checking vowel count
if vowelcount == 0:

    #if no vowels and only one consonant (ex input: b!)
    if consonantcount== 1:
        print("There was 1 consonant.")

    #if no vowels and multiple consonants (ex input: bb!)
    elif vowelcount >1:
        print("There were ", consonantcount, "consonants.")

#if there are any vowels at all
elif vowelcount >0:

    #having this here makes sure that there was a vowel printout before the consonant bit
    #otherwise this won't print and there won't just be  a floating statement of "# constonants" in the output

    #if any vowels and only one consonant (ex input: ab! or aab!, etc)
    if consonantcount == 1:
        print("1 consonant.")

    #if any vowels and multiple consonants (ex input: abb! or aabb!, etc)
    elif consonantcount >1:
        print(consonantcount, "consonants.")

#PART 4- HIGHEST CHARACTER USAGE

#VARIABLES
highest = -999 #force some value to take it's place (even a zero, which won't print out becuase of other stuff i've done(i hope))
#i have two counts in here:
#this one is to count the number of letters with highest values so it can start or stop generating print outs with that info
counttimes = 0
#this one is to precount them so the program knows which letter is the last one in the list and it can put an ampersand (&) before it)
#this literally only exists because I was trying to format nicely
#it's so superfluous
#please end me
ampersand = 0

#for loop for replace highest variable with highest value from array
for let in range(v-1):
    #checks to make sure those values aren't all just zero
    if array[let] != 0:
        #bit that actually replaces variable
        if array[let] > highest:
            highest = array[let]

#this bit counts how many letters were used most frequently
#checks to make sure that the highest value was replaced with something, otherwise it won't give a print out
if highest != -999:
    #going through array
    for let in range(v-1):
        #making sure not to count anything with a value of 0
        if array[let] != 0:
            #count itself
            if array[let] == highest:
                ampersand += 1
                #so when i get out of this if statement i know how many different places in the array have the same value, which is a number i'll need later
                #i really just needed a count like this so i could mess with it outside of my other if statements
                #or bring it in if i needed it, which i did

#set so that it only enters this junk if the highest value was changed (ergo, no input no highest value, otherwise it should give you something)
if highest != -999:

    #this part exists solely so that if only one character is used most frequently, the print out will use the singular form of "letter"
    if ampersand == 1: #if there is only one letter used most frequently

        #initial print statement for single letter used most frequently
        print("The letter used most frequenty was ", end="")

        #if the most frequently the most frequent letter is used is only once (ex input: a!")
        #so that the print out says "use" as in "one use" and not "one uses"
        if highest == 1:
            
            for let in range(v-1):
                if array[let] != 0: #i'm not completely sure that i need as many of these checks that it isn't 0, but safety first, i guess? I mean at this point I already know the value in that array space is going to be at least 1... oh well. once i ran this and it told me that the whole alphabet was used most frequently at zero uses and that was awful and I just don't want it to happen again
                    if array[let] == highest:
                        print(chr(65+let), end="") #prints the character(65+let=character ascii table value) without skipping lines so the next printout hangs on the end nicely

            #end of print out about single characters used once as most frequent
            print(" at ", highest, " use.")

        #i'm realizing you may not even want to KNOW that a single character was used
        #once and that one time was the most frequently that one character was used
        #i feel like giving that info is pretty smarmy
        #but hey, it's here
        #i just don't want it to do nothing for you, i feel like that would weird for you

        #if there is only one letter used the most times (ex input: aaa!)
        if highest > 1: #so, if uses were more than one (this is also a zero check, technically)
            for let in range(v-1):
                if array[let] != 0: #zero checks for dayz
                    if array[let] == highest:
                        print(chr(65+let), end="")

            #final print out, for multiple uses            
            print(" at ", highest, " uses.")

    #if the highest use is only once among several letters (ex input: abc!)
    elif highest == 1 and ampersand > 1:

        #print out for multiple letters used most frequently
        print("The letters used most frequenty were ", end="")

        #going through array
        for let in range(v-1):
            if array[let] != 0: #zero check (i have no idea how a zero would have made it to this point, that would be one strong zero)
                if array[let] == highest: #checks if each value matches the highest, which was already logged as a variable
                    counttimes += 1
                    #this seperate count functions with in the if statement here
                    #so that the program knows when it has reached the end of the letters that were used most
                    #and it can put an ampersand in front of it

                    #if count is one (which it will inevitably be) prints the character with no punctuation and no new line, so it can continue the statement
                    if counttimes == 1:
                        print(chr(65+let), end="")

                    #if count gets over one use and is still under the total number of characters used most
                    elif counttimes > 1 and counttimes < ampersand:
                        print(" , ", chr(65+let), end="")

                    #for final character (count within this if statement reaches the value of the pre-made count of characters(ampersand) used most)
                    elif counttimes == ampersand:
                        print(", & ", chr(65+let), end="")

        #final print out on these
        print(" at ", highest, " use each.")

    #any other instance in which the value of the highest number of uses has been found (ergo, if there is any input whatsoever that doesn't include only one letter used once, multiple letters used once, or if there is only one most frequently used letter, god that's a lot) 
    else:

        #print statement now assuming there are multiple letters used most frequently
        print("The letters used most frequently were ", end="")

        #usual range
        for let in range(v-1):
            if array[let] != 0:
                if array[let] == highest:
                    counttimes +=1 #counting again (also, for posterity, i feel like i should mention at this part that i don't have to reset this to zero because the program wouldn't have entered the if statement that beigns this count, so for all intents and purposes, this is still 0 at this point)
                    #i hope

                    #for fist letter
                    if counttimes == 1:
                        print(chr(65+let), end="")
                        
                    #any letters in between
                    elif counttimes > 1 and counttimes < ampersand:
                        print(" , ", chr(65+let), end="")

                    #last letter
                    elif counttimes == ampersand: #oh my god it worked
                        print(", & ", chr(65+let), end="")

        #print out for these possibilities                       
        print(" at ", highest, " uses each.")
        
    
#PART 5- LOWEST CHARACTER USAGE
#my comments on this part are going to be pretty barren/the same considering this is literally
#the last part copied and pasted with the variables changed

#VARIABLES (i'm just going to essentially reuse the same ones, which works because once it exits the loop above, this part will reset the variables 
lowest = 999 #force some value to take it's place (even a zero, which won't print out becuase of other stuff i've done(i hope))

#two counts:
counttimes = 0
ampersand = 0

#for loop for replace lowest variable with lowest value from array
for let in range(v-1):
    #checks to make sure those values aren't all just zero
    if array[let] != 0:
        #bit that actually replaces variable
        if array[let] < lowest:
            lowest = array[let]

#this bit counts how many letters were used least frequently, as long as they weren't zero
#checks to make sure that the lowest value was replaced with something, otherwise it won't give a print out
if lowest != 999:
    #going through array
    for let in range(v-1):
        #making sure not to count anything with a value of 0
        if array[let] != 0:
            #count itself
            if array[let] == lowest:
                ampersand += 1
                #outside count set

#only enters this if lowest variable was changed
if lowest != 999:

    if ampersand == 1: #if there is only one letter used least frequently (ex input: abb!)
    #yes, some of these will overlap with the highest series of if statements
    #but they should still tecnically be true

        #initial print statement for single letter used least frequently
        print("The letter used least frequenty was ", end="")

        #if the least frequently the least frequent letter is used is only once (ex input: a!")
        #so that the print out says "use" as in "one use" and not "one uses"
        if lowest == 1:
            
            for let in range(v-1):
                if array[let] != 0: #i'm not completely sure that i need as many of these checks that it isn't 0, but safety first, i guess? I mean at this point I already know the value in that array space is going to be at least 1... oh well. once i ran this and it told me that the whole alphabet was used most frequently at zero uses and that was awful and I just don't want it to happen again
                    if array[let] == lowest:
                        print(chr(65+let), end="") #prints the character(65+let=character ascii table value) without skipping lines so the next printout hangs on the end nicely

            #end of print out about single characters used once as most frequent
            print(" at ", lowest, " use.")

        #enjoy these useless printouts

        #if there is only one letter used the least times, but still more than once (ex input: aabbb!)
        if lowest > 1: #so, if uses were more than one (this is also a zero check, technically)
            for let in range(v-1):
                if array[let] != 0: #zero checks for dayz
                    if array[let] == lowest:
                        print(chr(65+let), end="")

            #final print out, for multiple uses            
            print(" at ", lowest, " uses.")

    #if the lowest use is only once among several letters (ex input: abc!)
    elif lowest == 1 and ampersand > 1:

        #print out for multiple letters used least frequently
        print("The letters used least frequenty were ", end="")

        #going through array
        for let in range(v-1):
            if array[let] != 0:
                if array[let] == lowest: #checks if each value matches the highest, which was already logged as a variable
                    counttimes += 1

                    #if count is one (which it will inevitably be) prints the character with no punctuation and no new line, so it can continue the statement
                    if counttimes == 1:
                        print(chr(65+let), end="")

                    #if count gets over one use and is still under the total number of characters used most
                    elif counttimes > 1 and counttimes < ampersand:
                        print(" , ", chr(65+let), end="")

                    #for final character (count within this if statement reaches the value of the pre-made count of characters(ampersand) used most)
                    elif counttimes == ampersand:
                        print(", & ", chr(65+let), end="")

        #final print out on these
        print(" at ", lowest, " use each.")

    #any other instance in which the value of the lowest number of uses has been found (ergo, if there is any input whatsoever that doesn't include only one letter used once, multiple letters used once, or if there is only one most frequently used letter)
    else:

        #print statement now assuming there are multiple letters used most frequently
        print("The letters used least frequently were ", end="")

        #usual range
        for let in range(v-1):
            if array[let] != 0:
                if array[let] == lowest:
                    counttimes +=1 #counting again (also, for posterity, i feel like i should mention at this part that i don't have to reset this to zero because the program wouldn't have entered the if statement that beigns this count, so for all intents and purposes, this is still 0 at this point)
                    #i hope

                    #for fist letter 
                    if counttimes == 1:
                        print(chr(65+let), end="")
                        
                    #any letters in between
                    elif counttimes > 1 and counttimes < ampersand:
                        print(" , ", chr(65+let), end="")

                    #last letter
                    elif counttimes == ampersand: #oh my god it worked
                        print(", & ", chr(65+let), end="")

        #print out for these possibilities                       
        print(" at ", lowest, " uses each.")
