#Let's help an online store with their new refund policy. In this store, you can return an item and get a refund in 2 cases:
#1. Within 10 days from the day of purchase, given that you have not used the item, or
#2. No matter when you bought it, when the item broke down through no fault of your own.


days_of_purchase = int(input( 'How many days ago have you purchased the item? '))
used_the_item = input('Have you used the item at all [y/n]? ')
broken_on_its_own = input('Has the item broken down on its own [y/n]?  ')

if(broken_on_its_own == 'y'or (days_of_purchase <= 10 and used_the_item == 'n')):
    print('You can get a refund.')
else:
    print('You cannot get a refund.')