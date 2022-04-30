from math import ceil

def deta_put_many(list_items,database_instance):
    # accepts list of items and a deta database_instance where the items will be put
    number_items_per_put =25 # deta allows only 25 items to be inserted inside a database at once
    no_iterations=ceil(len(list_items)/number_items_per_put)
    for count in range(1,no_iterations+1):
        from_index=count*number_items_per_put - number_items_per_put
        to_index=from_index + number_items_per_put
        sub_selected=list_items[from_index:to_index]
        database_instance.put_many(sub_selected)