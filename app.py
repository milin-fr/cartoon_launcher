from webbrowser import open
import random


class App:
  def __init__(self):
    self.cartoon_list = [
                        'https://www.youtube.com/watch?v=ijUf5vadUho',
                        'https://www.youtube.com/watch?v=Gv5Y0eyUjmM',
                        'https://www.youtube.com/watch?v=v7jKx_SUb4E',
                        'https://www.youtube.com/watch?v=lvc5HZzfICA',
                        'https://www.youtube.com/watch?v=nlV1gD-Q4kc',
                        'https://www.youtube.com/watch?v=guMPIMthGqA',
                        'https://www.youtube.com/watch?v=XgTikrvX-bs',
                        'https://www.youtube.com/watch?v=4u3VJKJ7pa0',
                        'https://www.youtube.com/watch?v=JV6fajokJe8',
                        'https://www.youtube.com/watch?v=RaSxvc5fXFc',
                        'https://www.youtube.com/watch?v=R28bYp3IP80'
                        ]

    open(random.choice(self.cartoon_list))


if __name__ == "__main__":
  App()
