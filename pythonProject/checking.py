import re


class Checking:

    def check(self, user):
        with open("scores.txt", mode="r") as file:
            score = file.read()
        x = re.match('^[A-Z]..', user)
        if x:
            with open("data.txt", mode="a") as file:
                file.write(str(user))
                file.write(str(score) + "\n")
            return True
        else:
            return False

