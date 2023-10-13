import os
def create():
    os.mkdir("./img")
    for i in range(100):
        name = f"{i}.png"
        with open(f"./img/{name}", "w"):
            pass
create()