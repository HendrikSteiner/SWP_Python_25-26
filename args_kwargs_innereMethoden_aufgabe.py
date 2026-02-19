def func(para1, para2, *args ,**kwargs):
    print(para1)
    print(para2)
    print(*args)
    print("-------")

func('A',**{'para2':1000})
func('A',*(67,100,200))
func(para2 = 1000, *('A',))
#func('A',**{'parameter_1':1000,'parameter_2':1000})

def greet(name):
    def make_message():
        return f"Hallo, {name}!"  # nutzt Variable aus äußeren Funktionn

    return make_message()

print(greet("Sepp"))