import pygame

# Initialize game
pygame.init()

# Set display
# Variables
WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy")

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE = 10

class Barrier(pygame.sprite.Sprite):

    COLOR = WHITE

    def __init__(self, x, y, width, height, vel):
        pygame.sprite.Sprite.__init__(self)
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height     
        self.vel = vel   

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, vel):
        self.x -= vel

class Ball:
    
    VELOCITY = 10
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.VELOCITY
        self.y_vel = 0
        self.height = radius * 2

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self, up=True):
        if up:
            self.y -= self.VELOCITY
        else:
            self.y += self.VELOCITY


# Draw window function, takes in window and list of paddles, called in main function
def draw(win, ball):
    # Background
    win.fill(BLACK)
    # Ball
    ball.draw(win)
    pygame.display.update()


def draw_barrier(win, barrier):
    barrier.draw(win)
    pygame.display.update()


def handle_ball_movement(keys, ball):
    if keys[pygame.K_UP] and ball.y - ball.VELOCITY >= 0:
        ball.move(up=True)
    if keys[pygame.K_DOWN] and ball.y + ball.VELOCITY + ball.height <= HEIGHT:
        ball.move(up=False)


def handle_barrier_velocity(barrier):
    barrier.vel = 1


# Main function
def main():
    run = True
    clock = pygame.time.Clock()

    # Initialize Variables
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    start = pygame.time.get_ticks()

    barrier_group = pygame.sprite.Group()

    # Game loop
    while run:

        # Run 60 frames per a second
        clock.tick(FPS)

        # Draw window
        draw(WINDOW, ball)

        for event in pygame.event.get():

            # Check for quit
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()

        handle_ball_movement(keys, ball)

        now = pygame.time.get_ticks()

        if now - start > 2000:
            print("should print rectangle")
            start = now
            new_barrier = Barrier(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT, 1)
            barrier_group.add(new_barrier)
            barrier_group.draw(WINDOW)


        handle_barrier_velocity(barrier_group)



    pygame.quit()


if __name__ == '__main__':
    main()


