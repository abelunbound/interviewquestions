# Write a program that collects two input values
# from a user and stores them in two different containers "a" and "b"
# then swithces the values stored in the variables "a" and "b" and prints
# the content. Upon printing, "a" would hold the content of what was inputed in "b"
# and variable "b" would hold the content of what was inputed in "a"

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print ("a:" + a)
print ("b:" + b)