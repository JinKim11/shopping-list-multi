def menu():
	print """Please select an option:
   Main Menu 
1- Show all lists
2- Show a specific list
3- Add a new shopping list
4- Add an item to a shopping list
5- Remove an item from a shopping list
6- Remove a list by nickname
7- Exit"""


dictionary = {}

def show_specific_list():
	keys = dictionary.keys()
	keys.sort()
	print keys
	store = raw_input("Which list would you like to view?")
	values = dictionary[store]
	values.sort()
	print values

def show_all_lists():
	keys = dictionary.keys()
 	keys.sort()
 	print keys

def new_list():
	store = raw_input("What list would you like to add?").lower()
	items = []
	if store in dictionary:
		print "List already exists."
	dictionary[store] = items


def new_item():
	print dictionary.keys()
	select_list = raw_input("Which list would you like to add to?").lower()
	if select_list in dictionary:
		add_item = raw_input("What item would you like to add?").lower()
		if add_item in dictionary[select_list]:
			print "Your item is already on the list"
		else:
			dictionary[select_list].append(add_item) 
			values = dictionary[select_list] 
			values.sort()
			print dictionary[select_list]
	else:
		print "That list does not exist."

def rem_item():
	print dictionary.keys()
	select_list = raw_input("Which list would you like to remove an item from?")
	if select_list in dictionary:
		values = dictionary[select_list]
		values.sort()
		print values
		del_item = raw_input("What item would you like to delete?")
		if del_item in dictionary[select_list]:
			dictionary[select_list].remove(del_item)
			print "Your item has been removed."
		else:
			print "Your item is not on the list."
	else:
		print "That list does not exist."

def rem_list():
	keys = dictionary.keys()
	keys.sort()
	print keys
	key_list = raw_input("What list would you like to remove?").lower()
	if key_list in dictionary.keys():
		del dictionary[key_list]
		print "Your list has been removed."
	else:
		print "List does not exist."

def main():
	menu()
	while(True):
		choice = int(raw_input("Please choose any of the above menu items or enter 0 to see the main menu:"))
		if choice == 7:
			break
		elif choice == 0:
			menu()
		elif choice == 1:
			show_all_lists()
		elif choice == 2:
			show_specific_list()
		elif choice == 3:
			new_list()
		elif choice == 4:
			new_item()
		elif choice == 5:
			rem_item()
		elif choice == 6:
			rem_list()
		else:
			print "Please enter a valid input."

if __name__ == "__main__":
	main() 