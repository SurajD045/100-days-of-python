#  match case statements:
"""To implement a switch-case lilke characteristics very similar to is-else functionallity,we use a match-cse in a python."""
"""The match statement will compare a given variables value to different shapes , also refferd to as the pattern. the main idea is to keep on comparing
the variable with all the present patterns untill it fits into one

The match case consist three entities:
1. The maatch keyword
2.One or more case clauses
3.Expression for each case

The case clause consist of patterns to be matched to a variable,condition to a evaluated,if the patterns matches ,and a set of statementsto be executed 
if the pattern matches."""

x = input("Enter the value of x:")
#x is the variable to match
match int(x):
    #if x is 0
    case 0:
        print("You entered 0")
    case 5:
        print("you eneterd 5")
    case 4 if int(x) % 2 == 0:
        print("x%2==0 means you enetered 4.")
    case _:
        print(x)

