# found the volume of a cuboid
# l * w * h = volume units

length = float(input('Enter a length: '))
width = float(input('Enter a width: '))
height = float(input('Enter a height: '))

volume = length * width * height

print(f'You enter the length of {length} and the width of {width} and the'
      f'  height of {height} which will give you the cuboid volume of {volume} units')