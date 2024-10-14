# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]} 

#answer- TypeError: unhashable type: 'list'
#        we can't access elements using indexing in sets
#        sets are immutable
