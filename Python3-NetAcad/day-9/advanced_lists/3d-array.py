# Imagine a hotel. It's a huge hotel consisting of three buildings,
# 15 floors each. There are 20 rooms on each floor.
# For this, you need an array which can collect and process information on the occupied/free rooms.
# First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.

### Create a 3D array with building number, floors and rooms as the three dimensions.

#hotel=[[["["+str(b)+"]"+"["+str(f)+"]"+str(False) for r in range(20)] for f in range(15)] for b in range(3)]
hotel=[[[False for r in range(20)] for f in range(15)] for b in range(3)]
print(hotel)
hotel[2][14][2]=True
hotel[2][14][3]=True
hotel[2][14][6]=True
hotel[2][14][8]=True
hotel[2][14][9]=True
hotel[2][14][12]=True
### checking vacancy
vacancy=0
for i in range(20):
    if hotel[2][14][i]==False:
        vacancy += 1
print("Vacant rooms in 15th floors are:",vacancy)
