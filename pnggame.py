import pygame
import random, math, time


# constants
score_l = 0
score_r = 0
width = 640
height = 480
frames = 45



class Paddle(object):
    # Draws the player paddle object for pygame. __init__ contains most of the basics
    # dy is rate of change, no dx because it moves only on Y-axis; xy is starting position,
    # move is the actual direction of change and can be dy or -dy, shape is used for the draw method,
    # and state is used for if statements. Surface describes the pygame screen.
    # Has three methods: draw(), moveup(), and movedn() all of which take only self as parameter
    def __init__(self, surface, dy, start, color=(245, 245, 240)):
        self.color = color
        self.dy = dy
        self.move = 0
        self.xy = start
        self.win = surface
        self.shape = pygame.draw.rect
        self.state = 'still'

    def draw(self):
        if self.state == 'still':
            self.move = 0
            self.xy = (self.xy[0], self.xy[1] + self.move, self.xy[2], self.xy[3])
            return self.shape(self.win, self.color, self.xy)
        if 10 <= self.xy[1] <= 393:
            self.xy = (self.xy[0], self.xy[1] + self.move, self.xy[2], self.xy[3])
            return self.shape(self.win, self.color, self.xy)
        if self.xy[1] < 10:
            self.xy = (self.xy[0], 11, self.xy[2], self.xy[3])
        if self.xy[1] > 394:
            self.xy = (self.xy[0], 392, self.xy[2], self.xy[3])

    def moveup(self):
        self.state = 'moveup'
        self.move = -1 * padr.dy

    def movedn(self):
        self.state = 'movedn'
        self.move = padr.dy


class Ball(object):
    # Draws the ball object for pygame. __init__ contains most of the basics
    # xy are the combined X and Y coordinates, shape is used for the draw method,
    # color has default setting, and dy and dx are rates of change.
    def __init__(self, center, color=(245, 235, 210)):
        self.color = color
        self.xy = center
        self.shape = pygame.draw.circle
        self.dx = 10
        self.dy = 1
        self.hit = 0
        self.score_l = score_l
        self.score_r = score_r
    def draw(self, surface):
        return self.shape(surface, self.color, self.xy, 8)

    def move(self):
        self.xy = (self.xy[0] + self.dx, self.xy[1] + self.dy)

        # set limits - bounce off Y ceiling, reset to middle with -dx if outside X bound and increment score
        if self.xy[0] >= 639:
            self.score_l += 1
            self.xy = (390, 235)
            self.dx = -10
            self.dy = self.dy // 3
        elif self.xy[0] <= 1:
            self.score_r += 1
            self.xy = (220, 235)
            self.dx = 10
            self.dy = self.dy // 3
        elif self.xy[1] <= 5:
            self.xy = (self.xy[0], 6)
            self.dy *= -1
        elif self.xy[1] >= 475:
            self.xy = (self.xy[0], 474)
            self.dy *= -1
        # boundaries for right paddle, includes offset r = 8
        elif self.xy[0]+8 >= 440 and self.draw(win).colliderect((padr.xy[0], padr.xy[1] + 50, 1, 40)):
            self.xy = (self.xy[0] - 2, self.xy[1] + self.dy)
            angle = math.atan(self.dy/self.dx)
            if self.dy >= 0:
                anglenew = 180 - (90 + angle)
                self.dx = 12 * math.cos(anglenew * .6)
                self.dy = -6 * math.sin(anglenew * .6)
            else:
                anglenew = 180 - (90 + angle)
                self.dx = 12 * math.cos(anglenew * .6)
                self.dy = 6 * math.sin(anglenew * .6)
        elif self.xy[0] + 8 >= 440 and self.draw(win).colliderect((padr.xy[0], padr.xy[1] + 30, 1, 20)):
            self.xy = (self.xy[0] - 2, self.xy[1] + self.dy)
            self.dx *= -1
            self.dy = 0
        elif self.xy[0] + 8 >= 440 and self.draw(win).colliderect((padr.xy[0], padr.xy[1], 1, 30)):
            self.xy = (self.xy[0] - 2, self.xy[1] + self.dy)
            angle = math.atan(self.dy / self.dx)
            if self.dy <= 0:
                anglenew = 180 - (90 + angle)
                self.dx = 12 * math.cos(anglenew*.6)
                self.dy = 6 * math.sin(anglenew*.6)
            else:
                anglenew = 180 - (90 + angle)
                self.dx = 12 * math.cos(anglenew * .6)
                self.dy = -6 * math.sin(anglenew * .6)
        # boundaries for left paddle, includes offset r = 8
        elif self.xy[0]-8 <= 80 and self.draw(win).colliderect((padl.xy[0]+20, padl.xy[1] + 50, 1, 30)):
            self.xy = (self.xy[0] + 2, self.xy[1] + self.dy)
            angle = math.atan(self.dy/self.dx)
            if self.dy >= 0:
                anglenew = 180 - (90 + angle)
                self.dx = -12 * math.cos(anglenew * .6)
                self.dy = -6 * math.sin(anglenew * .6)
            else:
                anglenew = 180 - (90 + angle)
                self.dx = -12 * math.cos(anglenew * .6)
                self.dy = 6 * math.sin(anglenew * .6)

        elif self.xy[0] - 8 <= 80 and self.draw(win).colliderect((padl.xy[0]+20, padl.xy[1] + 30, 1, 20)):
            self.xy = (self.xy[0] + 2, self.xy[1] + self.dy)
            self.dx *= -1
            self.dy = 0

        elif self.xy[0] - 8 <= 80 and self.draw(win).colliderect((padl.xy[0]+20, padl.xy[1], 1, 30)):
            self.xy = (self.xy[0] + 2, self.xy[1] + self.dy)
            angle = math.atan(self.dy / self.dx)
            if self.dy <= 0:
                anglenew = 180 - (90 + angle)
                self.dx = -12 * math.cos(anglenew*.6)
                self.dy = 6 * math.sin(anglenew*.6)
            else:
                anglenew = 180 - (90 + angle)
                self.dx = -12 * math.cos(anglenew * .6)
                self.dy = -6 * math.sin(anglenew * .6)


def score():
    # function for score keeping, keeps track of left and right scores,
    # uses boolean value to avoid double counting
    global score_rend, score_l, score_r
    score_b = 42 < ball.xy[0] < 598
    text_str = "CPU: %s" % score_l + "    " + "Player: %s" % score_r
    pygame.font.init()
    font = pygame.font.SysFont("monospace", 18)
    score_rend = font.render(text_str, False, (220, 200, 170))
    win.blit(score_rend, (220, 24))
    if score_b:
        pass
    else:
        if ball.score_l:
            score_l = ball.score_l
        if ball.score_r:
            score_r = ball.score_r


def ai_loop():
    # handicapped computer player loop, tracks Y movement of ball
    diff = random.randrange(1, 10, 1)
    if padl.xy[1] >= ball.xy[1] > padl.xy[1] + 80:
        if diff > 3:
            padl.state = 'still'
            padl.move = 0
            padl.draw()
        if diff <= 3:
            padl.movedn()
            padl.draw()
    if not padl.xy[1] > ball.xy[1] > padl.xy[1] + 80:
        padl.state = 'still'
        if ball.xy[1] > padl.xy[1] + 80 and ball.xy[0] < 300:
            if diff > 4:
                padl.movedn()
                padl.draw()
            if diff == 2 or diff == 4:
                padl.movedn() if ball.xy[1] == padl.xy[1] + random.randrange(70, 140, 15) else padl.state == 'still'
                padl.draw()
            if diff == 1 or diff == 3:
                padl.moveup() if ball.xy[1] == padl.xy[1] - random.randrange(70, 140, 15) else padl.state == 'still'
                padl.draw()
        elif ball.xy[1] < padl.xy[1] and ball.xy[0] < 300:
            if diff > 2:
                padl.moveup()
                padl.draw()
            if diff == 2 or diff == 4:
                padl.movedn() if ball.xy[1] == padl.xy[1] + random.randrange(70, 140, 15) else padl.state == 'still'
                padl.draw()
            if diff == 1 or diff == 3:
                padl.moveup() if ball.xy[1] == padl.xy[1] - random.randrange(70, 140, 15) else padl.state == 'still'
                padl.draw()

def update(win):
    win.fill((15,15,19))
    ball.draw(win)
    padr.draw()
    padl.draw()
    ball.move()
    score()
    pygame.display.update()


def main():
    global ball, padr, padl, win, clock
    win = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    ball = Ball((315,235))
    padr = Paddle(win, 6, (600, 180, 20, 80))
    padl = Paddle(win, 1, (20, 200, 20, 80))

    while True:
        clock.tick(frames)

        ai_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        padr.moveup()
                        padr.draw()
                    elif event.key == pygame.K_s:
                        padr.movedn()
                        padr.draw()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        padr.state = 'still'
                        padr.draw()
        update(win)

main()
