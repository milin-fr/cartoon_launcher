from webbrowser import open as web_open
import random
import os


class App:
    def __init__(self):
        self.create_cartoons_txt()

        cartoons_list = self.get_cartoons_list()
        if cartoons_list:
            web_open(random.choice(cartoons_list))
        else:
            os.startfile("cartoons_list.txt")

    def get_cartoons_list(self):
        cartoons_list = []
        with open("cartoons_list.txt", "r") as file_cartoons_list:
            for line in file_cartoons_list:
                cartoons_list.append(line.strip("\n"))
        return cartoons_list

    def create_cartoons_txt(self):
        if not os.path.isfile('cartoons_list.txt'):
            with open("cartoons_list.txt", "w") as file_cartoons_list:
                file_cartoons_list.write("")


if __name__ == "__main__":
    App()
