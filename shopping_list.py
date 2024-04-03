#Task 1

shopping_list = []
done_add = False

def add_item_to_list(item):
    shopping_list.append(item)

while done_add == False:
    shop_item = input("Enter an item to add to your list: ")
    add_item_to_list(shop_item)
    if input("Would you like to add more to the list (y or n)?") == "n":
        done_add = True


#Task 2

done_remove = False
while done_remove == False:
    if input("Would you like to remove an item from the list? (y or n) ") == "y":
        print(shopping_list)
        remove_item = input("Please type which item you would like to remove: ")
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
        else:
            print("That item is not in your list.")
    else:
        done_remove = True


#Task 3

def format_shop_list(shop_liat):
    print("Your shopping list is: ")
    for x in shop_liat:
        print(f"~{x}~")

format_shop_list(shopping_list)
