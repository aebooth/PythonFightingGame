#import necessary modules
import math
import pygame
import GameUtils

#Intialize colors
WHITE = (255,255,255)
RED = (255,0,0)

#Intialize PyGame
pygame.init()

#Initialize window
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Cool Game")

#Get game screen image
main_background = pygame.image.load("FightBackground.png").convert()

#Intialize Left Side Fighter
action_images = {"block":pygame.image.load("LBlock.png"), "punch":pygame.image.load("LPunch.png"), "kick":pygame.image.load("LKick.png"), "hit":pygame.image.load("LHit.png")}
movement_images = [pygame.image.load("LWalk1.png"),pygame.image.load("LWalk2.png"),pygame.image.load("LWalk3.png")]
default_image = pygame.image.load("LStill.png")
position = (200,200)
left_fighter = GameUtils.Fighter(action_images,movement_images,default_image,position)


# Loop until the user clicks the close button.
quit_now = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
walk_left = False
walk_right = False
walk_count = 0
while True:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            quit_now = True# Flag that we are done so we exit this loop
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                left_fighter.kick()
            elif event.key == pygame.K_d:
                left_fighter.punch()
            elif event.key == pygame.K_s:
                left_fighter.block()
            elif event.key == pygame.K_a:
                left_fighter.hit()
            elif event.key == pygame.K_LEFT:
                walk_left = True
            elif event.key == pygame.K_RIGHT:
                walk_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f or event.key == pygame.K_d or event.key == pygame.K_s or event.key == pygame.K_a:
                left_fighter.stop()
            elif event.key == pygame.K_LEFT:
                left_fighter.stop()
                walk_left = False
                walk_count = 0
            elif event.key == pygame.K_RIGHT:
                left_fighter.stop()
                walk_right = False
                walk_count = 0
    if quit_now:
        pygame.quit()
        break
 
    # --- Game logic should go here

    left_fighter.x = left_fighter.vx + left_fighter.x
    #left_fighter.y = left_fighter.vy + left_fighter.y
    if walk_left or walk_right:
        walk_count = walk_count + 1
        if walk_left and walk_count%10==0:
            left_fighter.walk(-5)
        elif walk_right and walk_count%10==0:
            left_fighter.walk(5)
    # --- Drawing code should go here
    
    #Blank out screen
    if walk_left:
        left_fighter_surface = pygame.transform.flip(left_fighter.get_drawable_surface(),True, False)
    else:
        left_fighter_surface = left_fighter.get_drawable_surface()
    screen.fill(WHITE)
    #Draw game background (simple game that has no menu screen and only one level)
    screen.blit(main_background,(0,0))
    
    ##Draw Game Objects##
    screen.blit(left_fighter_surface, (left_fighter.x,left_fighter.y))
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    #screen.fill(WHITE)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
