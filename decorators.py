def dec(function_arg):
    
    def mfx(*args,**kwags):
        print("\nNice! You are using the decorators...\n")
        function_arg(*args,**kwags)
        print("\n You have succesfully used the decorators")
    return mfx

@dec
def add(a,b):
    print(a+b)
add(3,7)

def hello():
    print("Hello Guys")
dec(hello)()

# import logging
# def log_function_call(func):
#     def decorated (*args,**kwargs):
#         logging.info(f"calling {func.__name__} with args={args},kwargs={kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"calling {func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a,b):
#     # return a+b