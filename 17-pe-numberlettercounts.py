# COMPLETE

def stringcount():
    """
    Takes a number as input. Count starts at 0 and ends at desired number. Numbers get converted to word equivalents and each letter of each word gets counted. 
    
    Example: (This example represents what the function does instead of the exact steps it takes to do it)
        Input: 3
        Convert: 1, 2, 3 -> one, two, three -> one = 3(letters), two = 3, three = 5. 
        Output: 11

    Note: only works 1000. Also excludes space, dash, and 0(zero) but includes the word 'and' where appropriate.
    """



    data = { 0:" zero", 1:" one", 2:" two", 3:" three", 4:" four", 5:" five", 6:" six", 7:" seven", 8:" eight", 9:" nine", 10:" ten", 11:" eleven", 12:" twelve", 13:" thirteen", 14:" fourteen", 15:" fifteen", 16:" sixteen", 17:" seventeen", 18:" eighteen", 19:" nineteen", 20:" twenty", 21:" twentyone", 22:" twentytwo", 23:" twentythree", 24:" twentyfour", 25:" twentyfive", 26:" twentysix", 27:" twentyseven", 28:" twentyeight", 29:" twentynine", 30:" thirty", 31:" thirtyone", 32:" thirtytwo", 33:" thirtythree", 34:" thirtyfour", 35:" thirtyfive", 36:" thirtysix", 37:" thirtyseven", 38:" thirtyeight", 39:" thirtynine", 40:" forty", 41:" fortyone", 42:" fortytwo", 43:" fortythree", 44:" fortyfour", 45:" fortyfive", 46:" fortysix", 47:" fortyseven", 48:" fortyeight", 49:" fortynine", 50:" fifty", 51:" fiftyone", 52:" fiftytwo", 53:" fiftythree", 54:" fiftyfour", 55:" fiftyfive", 56:" fiftysix", 57:" fiftyseven", 58:" fiftyeight", 59:" fiftynine", 60:" sixty", 61:" sixtyone", 62:" sixtytwo", 63:" sixtythree", 64:" sixtyfour", 65:" sixtyfive", 66:" sixtysix", 67:" sixtyseven", 68:" sixtyeight", 69:" sixtynine", 70:" seventy", 71:" seventyone", 72:" seventytwo", 73:" seventythree", 74:" seventyfour", 75:" seventyfive", 76:" seventysix", 77:" seventyseven", 78:" seventyeight", 79:" seventynine", 80:" eighty", 81:" eightyone", 82:" eightytwo", 83:" eightythree", 84:" eightyfour", 85:" eightyfive", 86:" eightysix", 87:" eightyseven", 88:" eightyeight", 89:" eightynine", 90:" ninety", 91:" ninetyone", 92:" ninetytwo", 93:" ninetythree", 94:" ninetyfour", 95:" ninetyfive", 96:" ninetysix", 97:" ninetyseven", 98:" ninetyeight", 99:" ninetynine", 100:" onehundred", 200:" twohundred", 300:" threehundred", 400:" fourhundred", 500:" fivehundred", 600:" sixhundred", 700:" sevenhundred", 800:" eighthundred", 900:" ninehundred", 1000:" onethousand",
    }

    n = int(input("Enter any number lower than 1000: "))

    longword = ''

    for number in range(n+1): # The number given on input to loop through
        if number > 1000: 
            # Number greater than the scope of this program
            return print("This is only set up to run to 1000")

        if number == 1000:
            # Adds Key:value for 1000
            longword+=data[number] # Add number name to string
            
        if number > 100 and number < 1000:
            # Adds Key:Value for any number 101-999
            ten = (number % 100) # Correct number at the tenth position and lower for Key match
            hundred = number - ten # Correct number at the hundredth position and lower for Key match

            if number % 100 == 0:
                # If no remainder just return correct hundredth place Key
                longword += data[hundred] # Add number name to string
            else:
                # If number has a remainder get the hundredth place, concatonate 'and', and the tenth/first place
                longword += data[hundred] + ' and' + data[ten] # Add number name to string

        if number <= 100:
            # If less than 100, use correct Key:Value
            longword += data[number] # Add number name to string

    check = (longword.replace(' ','')) # Remove whitespace. White space was added for easier visual testing. 
    final = (len(check) -4) # Gets the length of the large string created and subtracts 4 for the word 'zero'. TODO Change this into a function argument Boolean 
    print(final)

print(stringcount())