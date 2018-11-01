mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple']) # dict style

import ex40_mystuff
ex40_mystuff.apple() # module style

# import ex40_mystuff
print(ex40_mystuff.tangerine) # same thing, it's just variable


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)




class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()