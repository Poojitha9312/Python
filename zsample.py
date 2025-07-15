def outer_fun():
    print("hai")
    def inner_fun():
        print("how are you")
    return inner_fun
x=outer_fun()
x()




