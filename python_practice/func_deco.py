def test(function):
    def wrapper():
        print("start hello")
        function()
        print("Bye")
    return wrapper()

@test 
def hello():
    print("hello")
    
hello()