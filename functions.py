def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def terminal_1():
    print("please proceed to terminal 1")
def terminal_2():
    print("please proceed to terminal 2")
def terminal_3():
    print("please proceed to terminal 3")

def main_func(resul):
    if resul == "budget":
        terminal_1()
    if resul == "domestic":
        terminal_2()
    if resul == "business":
        terminal_3()