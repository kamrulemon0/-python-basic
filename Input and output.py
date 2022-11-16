# Built in  function
text1 ='hello'
text2 ='How are you'
text3 = 'Hope are you well'

print("-".join((text1,text2,text3)))



# HOW TO check length

let = 'I love in python'
print(len(let))


# Some input think  Know  upper and big letter

const = input()
const = const.capitalize()
print(const)

# All text big letter

text = 'every think will be ok'
text = text.upper()
print(text)

#  when first  word  big litter
name = input()
name = name.title()
print(name)

# this type big letter can be small letter

text = "I love python"
text = text.lower()
print(text)



# That which is big becomes small that which  was  small become big

const =" i loVe python"
const = const.swapcase()
print(const)


# To find how many times a word occurs
Text5 = " hello bi heo eoe fe"
print(Text5.count('e'))

# find fuction how find

Text9 = "nkodeNalennf"
print(Text9.find("e"))

#Reverse search

Text3 = "I Love python"
print(Text3.rfind("o"))

#resplase function

Text8 = "Life is think"
print(Text8.replace("is" ,"was"))

# remove space

Text1 = "    kamrul emon  "
print(Text1.strip(" "))



# split function
Text = " I love bangladesh"
print(Text.split())
print(Text.split()[0])
print(Text.split()[1])
print(Text.split()[2])



# Center function

Text1 = "Python"
print(Text1.center(8 ,"*"))     # Static
print(Text1.center(len(Text1) +10 ,  "*"))  # dynamic