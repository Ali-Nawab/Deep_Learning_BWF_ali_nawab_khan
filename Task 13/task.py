import pandas as pd

ser1 = pd.Series([1,2,3,4,5], ['a', 'b','c','d','e']) # you also try to add new index f and don't increase data value. 

ser2 = pd.Series([4,6,7,9,2], ['a','b','c','d','e'])



ser1['f'] = ""


ser2 = pd.Series([4,6,7,9,2, 10], ['a','b','c','d','e', 'g'])


print(ser1 + ser2)


ser1 = pd.Series([1,2,3,4,5, 6], ['a', 'b', 'c', 'd','e', 'f'])
ser2 = pd.Series([5,4,3,2,1, 7], ['a', 'b', 'c', 'd', 'e', 'z'])


print()
print()
print(ser1 + ser2)