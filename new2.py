my_age =37
#candles=""
#if my_age ==1:
#   candles="i"
#elif my_age== 2:
#   candles="ii"

#this makes 37 candles
candles ="i"*my_age
# This makes space + space = 37 candles
candles= "  "+candles
#Now I have the top of my cake.
#This make the outline of the cake
bottom = "-" *my_age
#Now I add the sides of the cake. 
bottom = "| " + bottom + "|"
#wonderfull I have baked a cake
print (candles)
print (bottom)


