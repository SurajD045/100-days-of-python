#exception handling in python.
"""Exception handling is the process of responding to unwanted or unexpected 
evrnts when a computer program runs.exption handling deals with these events to avoid the program or system
crashing ,and whitout this process ,exptions would disrupt the normal operation
of a python."""

"""Python haas many built in exceptions that are raised when your progeam
encounters an error (something in the program goes wrong)

when these exceptions occurs , the pythin interpreter stops the current procees 
and passes it to the calling process untill it is handled. if not handled the pprogram will crash.
"""
"""python try..except
try...except blocks are used in python to handle errors and exception . 
the code in the block runs when ther is no error.
If they try block catches error, then the except block is executed.
"""
# a = input("enter the number:")
# print(f"Multiplication table of {a} is :")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{i}={int(a)*i}")
# # except:
# #     print("invalid input!")


# # except Exception as e:
# #     print(e)

    

# print("some imp lines of code ")
# print("End of program")
try:
    num = int(input("Enter an intger: "))
    a = [6,8,5]
    print(a[num])
except ValueError:
    print("Number enterd is not aan integer.")
except IndexError:
    print("Index error.")