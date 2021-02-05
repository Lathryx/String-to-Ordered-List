from time import sleep as wait
import re 

usr = input("Please insert the string to be parsed... \n\n")
wait(0.5)
print(f"Your string is: {usr}\n\n") 

wait(1)
delimiter = input("Please type the delimiter to parse your string with... \n(To split by character, type '!bycharacter'. To split by word, type '!byword'. To split by sentence, type '!bysentence'. \n\n") 

wait(0.5)
print("Thank you, your list will be printed soon!") 

listOrd = []
item_no = 1

wait(1)
if (delimiter == '!bycharacter'): 
	list_unOrd = list(usr)
elif (delimiter == '!byword'): 
	list_unOrd = usr.split() 
elif (delimiter == '!bysentence'): 
	list_unOrd = re.split('.\s|!\s|?\s', usr) 
else: 
	list_unOrd = usr.split(delimiter) 

for item in list_unOrd:
	listOrd.append(str(item_no) + '. ' + item)
	item_no += 1

print('\n'.join(listOrd))
