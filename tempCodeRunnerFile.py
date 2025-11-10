def add(a,b):
    try:
        result=a+b
    except Exception as e:
        print(e)
    else:
        print(f"The result is:{result}")
add(int(input("Enter a value:")),int(input("Enter b value:")))