# found the volume of a cuboid
# given the volume and the width and height need to found the length

# have user enter the following inputs
volume = float(input('Enter the volume: '))
width = float(input('Enter a width: '))
height = float(input('Enter a height: '))

# multiply height and width

multiplyHW = width * height

# divide multiplyHW with volume

lenghtTotal = volume / multiplyHW

print(f'the length of the cuboid is {lenghtTotal}')
