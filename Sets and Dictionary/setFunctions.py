friends={'saif','ali','hassan','asad','ahmed'}
my_friends={'wajid','arslan','sherry','amir','ali','saif','asad'}

cars=['vigo','farrari','v8','civic','gli']

print('ali' in friends and 'ahmed' in friends)
print(my_friends.union(friends))#combine all elements in one set
print(friends.intersection(my_friends))# same elements in set
print(friends.difference(my_friends)) #diffrence between two sets

print(my_friends.symmetric_difference(friends)) #symmetric difference
print(my_friends ^ friends)#symmetric difference 

car_no_copy=set(cars)
print(car_no_copy)