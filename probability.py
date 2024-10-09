import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls > len(self.contents):
            drawn_balls = self.contents[:]
        else:
            for _ in range(num_balls):
                choice = random.choice(self.contents)
                self.contents.remove(choice)
                drawn_balls.append(choice)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1

        success = True
        for color, count in expected_balls.items():
            if drawn_balls_count.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments


if __name__ == "__main__":
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                    expected_balls={'red':2,'green':1},
                    num_balls_drawn=5,
                    num_experiments=2000)
    
    # Since this is based on random draws, the probability
    # will be slightly different each time the code is run.
    print(probability)