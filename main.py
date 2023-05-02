def hello_decore(hello):
    def say_hallo():
        print('Welcome to program')
        hello()
    return say_hallo()


def hello():
    print('Hello')


hello_decore(hello)
