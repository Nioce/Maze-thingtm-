# Imports
import pygame
import intersects
import random
# Initialize game engine
pygame.init()
MY_FONT = pygame.font.Font(None, 50)
MY_FON = pygame.font.Font(None, 25)
MY_FONSMOLL = pygame.font.Font(None, 15)

# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

#spleshscreen
img = pygame.image.load('aaa.jpg')
# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
MEH = (25, 186, 142)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)
BLUE = (120,200,10)
RAINBOW=(random.randrange (0,255), random.randrange (0,255), random.randrange (0,255))

#stages
START = 0
PLAYING = 1
END = 2

def setup():
    global coins, player, player_vx, player_vy, door1, red_door, green_door, switch_meh, wall_meh, stage
    player =  [350, 375, 25, 25]
    player_vx = 0
    player_vy = 0
    player_speed = 5
    stage = START
# Make a player
player =  [350, 375, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make wallswa
door1=[100,200,100,25]
red_door=[25,360,300,10]
green_door=[1,1,1,1]
wall1 =  [1, 1, 1, 1]



#red walls
red_door1=[300,325,25,100]
red_door2=[300,425,125,25]
red_door4=[400,325,25,100]
red_door5=[400,200,25,125]
red_door6=[300,200,25,125]
rd1=[300,150,125,25]
rd2=[400,150,25,50]
rd3=[300,150,25,50]
rd4=[300,175,75,25]
rd5=[0,400,100,25]
rd6=[0,500,100,25]
red_doors=[red_door1, red_door2, red_door4, red_door5, red_door6,rd1,rd2,rd3,rd4,
           rd5,rd6]
#Meh walls
meh_door2=[325,350,100,25]
meh_door3=[425,350,100,25]
meh_door4=[325,350,25,100]
md5=[25,50,25,100]
md6=[25,150,100,25]
md7=[125,25,25,150]
md8=[0,200,100,25]
m8=[75,0,25,100]
m9=[125,175,25,50]
m10=[50,250,25,25]
m11=[125,250,25,25]
m12=[150,175,75,25]
m13=[200,75,25,100]
m14=[150,25,100,25]
m14=[150,250,25,25]
m15=[175,225,25,25]
m16=[175,225,100,25]
m17=[250,25,25,200]
m18=[125,25,125,25]
m19=[100,275,25,25]
m20=[50,275,25,75]
m21=[50,325,100,25]
m22=[150,300,25,50]
m23=[175,300,25,25]
m24=[225,275,25,25]
m25=[250,275,75,25]
m26=[275,25,50,25]
m27=[300,25,25,250]
m28=[400,175,25,25]
m29=[400,0,25,300]
m30=[325,225,125,25]
m31=[175,325,200,25]
m32=[350,275,25,50]
m33=[450,325,25,25]
m34=[425,275,25,25]
m35=[475,200,25,25]



switchblueandmeh = [200,200,25,25]

wallmeh=[450,400,25,100]
wall_meh=[wallmeh, meh_door2, meh_door3, meh_door4, md5, md6, md7, md8, m8, m9
          ,m10,m11, m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23
          ,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,m34,m35]

#greem walls
green_door1=[300,325,25,100]
green_door2=[300,425,125,25]
green_door3=[300,325,125,25]
green_door4=[400,325,25,100]

#blue walls
rw1=[200,275,25,25]
blue_walls=[rw1]




gd1=[75,75,150,25]
gd2=[75,75,25,125]
gd3=[75,200,175,25]
gd4=[225,75,25,125]


switchmeh=[375, 175,25,25]
green_doors=[green_door, green_door1, green_door2, green_door3, green_door4,gd1,
             gd2,gd3,gd4]

swon=[50,450,25,25]
switchon= [350,400,25,25]
switchoff=[125, 125,75, 75]
walls = [wall1]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [125, 125, 75, 75]


coins = [coin1, coin2, coin3]

#Collide stuff
collidables = walls + green_doors


# Game loop
case = 1
win = False
red_doors_open = False
green_doors_open = True
switch_on = False
switch_off = True
switch_meh = False
wallmeh_open = False
blue_walls_open = False

playimage = pygame.image.load('Untitled.png')

setup()
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                    stage = PLAYING
                  
            elif stage == END:
                    setup()
                    done = False

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

        
        # Game logic (Check for collisions, update points, etc.)
        ''' move the player in horizontal direction '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for c in collidables:
            if intersects.rect_rect(player, c):        
                if player_vx > 0:
                    player[0] = c[0] - player[2]
                elif player_vx < 0:
                    player[0] = c[0] + c[2]

        ''' move the player in vertical direction '''
        player[1] += player_vy
        
        ''' resolve collisions vertically '''
        for c in collidables:
            if intersects.rect_rect(player, c):                    
                if player_vy > 0:
                    player[1] = c[1] - player[3]
                if player_vy < 0:
                    player[1] = c[1] + c[3]


        ''' get block edges (makes collision resolution easier to read) '''

        top = player[1]
        bottom = player[1] + player[3]
        left = player[0]
        right = player[0] + player[2]
        if case == 1:
            ''' if the block is moved out of the window, nudge it back on. '''
            if top < 0:
                player[1] = 0
            elif bottom > HEIGHT:
                player[1] = HEIGHT - player[3]
            if left <0:
                player[0] = 0
            elif right > WIDTH:
                player[0] = WIDTH - player[2]




        ''' get the coins '''
        hit_list = [c for c in coins if intersects.rect_rect(player, c)]

        for hit in hit_list:
            coins.remove(hit)
            #score += 1
            #play sound, etc.
        #screem player omages
            
        
        ''' open door on switch contact '''
        if intersects.rect_rect(player, switchon):

            red_doors_open = True
            green_doors_open = False
            wallmeh_open = False
            blue_walls_open = False
            collidables = [c for c in collidables if c not in green_doors]
            collidables = [c for c in collidables if c not in wall_meh]
            collidables = [c for c in collidables if c not in blue_walls]


            collidables += red_doors
            
            switch_on = True
            switch_off = False
            switch_meh = False

        if intersects.rect_rect(player, swon):

            red_doors_open = True
            green_doors_open = False
            wallmeh_open = False
            blue_walls_open = False
            collidables = [c for c in collidables if c not in green_doors]
            collidables = [c for c in collidables if c not in wall_meh]
            collidables = [c for c in collidables if c not in blue_walls]


            collidables += red_doors
            
            switch_on = True
            switch_off = False
            switch_meh = False

        if intersects.rect_rect(player, switchblueandmeh):
            switch_on = False
            switch_off = False
            switch_meh = True

            blue_walls_open = True
            red_doors_open = False
            green_doors_open = False
            wallmeh_open= True
            collidables = [c for c in collidables if c not in red_doors]
            collidables = [c for c in collidables if c not in green_doors]

            collidables += blue_walls
            collidables += wall_meh
        if intersects.rect_rect(player, switchoff):
            switch_on = False
            switch_off = True
            switch_meh = False
            blue_walls_open = False            
            red_doors_open = False
            green_doors_open = True
            wallmeh_open = False
            
            collidables = [c for c in collidables if c not in red_doors]
            collidables = [c for c in collidables if c not in wall_meh]
            collidables = [c for c in collidables if c not in blue_walls]  
            collidables += green_doors
        if intersects.rect_rect(player, switchmeh):
            switch_on = False
            switch_off = False
            switch_meh = True
            blue_walls_open = False
            red_doors_open = False
            green_doors_open = False
            wallmeh_open = True
            collidables = [c for c in collidables if c not in blue_walls]  
            collidables = [c for c in collidables if c not in red_doors]
            collidables = [c for c in collidables if c not in green_doors]
            collidables += wall_meh
        if len(coins) == 0:
            win = True


        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)



    #Blit sccrren
    screen.blit(playimage, (player[0], player[1]))
    
    for w in walls:
        pygame.draw.rect(screen, MEH, w)
        

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
    
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    pygame.draw.rect(screen, MEH, switchmeh)
    pygame.draw.rect(screen, GREEN, switchon)
    pygame.draw.rect(screen, GREEN, swon)
    pygame.draw.rect(screen, YELLOW, switchoff)

    if red_doors_open:
        for d in red_doors:
            pygame.draw.rect(screen, RED, d)
            
    if green_doors_open:
        for d in green_doors:
            pygame.draw.rect(screen, GREEN, d)

    if blue_walls_open:
        for d in blue_walls:
            pygame.draw.rect(screen, BLUE, d)

    if wallmeh_open:
        for d in wall_meh:
            pygame.draw.rect(screen, MEH, d)

    pygame.draw.rect(screen, BLUE, switchblueandmeh)
    if stage == START:
        screen.blit(img,(0,0))
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
    for x in range(0, WIDTH, 25):
        pygame.draw.line(screen, WHITE, [x,0],[x,HEIGHT])

    for y in range(0, HEIGHT, 25):
        pygame.draw.line(screen, WHITE, [0,y],[WIDTH, y])

    for y in range(0, HEIGHT, 25):
        text1 = MY_FON.render(str(y), True, GREEN)
        screen.blit(text1, [0,y-7.5])
    for x in range(0, WIDTH, 25):
        text1 = MY_FONSMOLL.render(str(x), True, GREEN)
        screen.blit(text1, [x-7.5,0])
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
