def prize(day, month):

   win = 0

   if month in (1,3,5,7,8,10,12):

       for i in range(day, 32):

           win = win+i

   elif month in (4,6,9,11):

       for i in range(day, 31):

           win = win+i

   elif month == 2:

       for i in range(day, 29):

           win = win+i

   return win

