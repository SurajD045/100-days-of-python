#finally clause
"""a finally codr block is a also a part of  exception handling  when 
when we handle exception using the try and except block, we can include a finally block at the end.
the finally block is always executed. so its generally used for doing the concluding task
like closing file resources or closing database connection or may be ending the program execution 
with delighfull msg.
"""

def func1():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("i am always executed.")
    # print("i am always executed.")

x = func1()
print(x)

"""The finally block is executed irrespective of outcome of try ... except ..else blocks .
one of the imp use cases of finally block is in function which returns a value.
"""
