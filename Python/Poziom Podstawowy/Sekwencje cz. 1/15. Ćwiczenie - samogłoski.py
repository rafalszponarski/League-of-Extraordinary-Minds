text = """I'm glad to say we've got the go-ahead to lend you the money you required. We will, of course,
need for security the deed to your house, the deed to your aunt's house, of your wife's parents' house, 
and of your granny's bungalow. And we will, in addition, need a controlling interest in the stock of 
your new company, unrestricted access to your private bank accounts, the deposit of your three children 
in our vaults as hostages, and a full legal indemnity in case of any embezzlement carried out against 
you by members of our staff during the normal course of their duties."""

A=0
E=0
I=0
O=0
U=0
Y=0


for x in text:

   if x == 'a' or x == 'A':

       A +=1

   if  x == 'e' or x == 'E':

       E += 1

   if x == 'i' or x == 'I':

       I += 1

   if  x == 'o' or x == 'O':

       O += 1

   if x == 'u' or x == 'U':

       U += 1

   if x == 'y' or x == 'Y':

       Y += 1

print('A '+str(A)+'\nE '+ str(E)+ '\nI '+str(I)+ '\nO '+  str(O) +'\nU ' + str(U) +'\nY ' + str(Y))