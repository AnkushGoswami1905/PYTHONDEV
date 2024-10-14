# Check that a tuple type cannot be changed in python.

a=(24,45,"harry")
a[2]="larry"      # TypeError: 'tuple' object does not support item assignment