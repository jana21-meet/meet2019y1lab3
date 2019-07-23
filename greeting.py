name=input("what's your name??")
name=name.capitalize()
print("hello there " + name)
print("your name is " + str(len(name))+ " letters long")
f_letter=name[0].upper()
l_letter=name[-1].upper()
print("the first letter of your name is " + f_letter +"the last letter of your name is " + l_letter)
mis_letter= name[1:-1]
print ("the missing letters are " + mis_letter)

