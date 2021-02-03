usr = input("Please insert the string to be parsed... \n\n")
list_unOrd = list(usr)
listOrd = []
item_no = 1

for c in list_unOrd:
	listOrd.append(str(item_no) + '. ' + c)
	item_no += 1

print('\n'.join(listOrd))
