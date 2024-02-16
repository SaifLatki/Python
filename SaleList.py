#to show the profit in weeks to sell the items
#best day,worst day and combine sell in weeks
sale_w1=[4,55,66,23,7,12,9]
sale_w2=[13,3,28,94,17,6]
sales=[]
new_day=input('Enter the number of item for new day: ')#enter the new day number
sale_w2.append(int(new_day))#add new day number in sale_w2
sales.extend(sale_w1)#store list of sale_w1 in sales list
sales.extend(sale_w2)#store list of sale_w2 in sales list

sales.sort()#both lists combined and sorted in order
worst_day_prof= sales[0] * 1.5 #calculating worst day profit
best_day_prof= sales[-1] * 1.5#calculating best day profit
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')
