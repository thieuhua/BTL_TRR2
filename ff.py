def outer():
    x = 10
    
    def inner():
        x = x + 1  # Lỗi: UnboundLocalError
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
