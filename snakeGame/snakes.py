import pygame
from pygame import mixer
import random

pygame.init()


white = (255, 255, 255)

black = (0, 0, 0)

red = (255, 0, 0)

clock = pygame.time.Clock()

display_width = 800

display_height = 600

background = pygame.image.load('images/new.png')

img=pygame.image.load('images/snake.png')

gameDisplay = pygame.display.set_mode((display_width, display_height))

icon=pygame.image.load('images/icon.png')

pygame.display.set_icon(icon)

pygame.display.set_caption('snake')

block_size =10

fps =30

medfont = pygame.font.SysFont('Georgia', 40, bold=True)

largefont=pygame.font.SysFont('Georgia',60,bold=True)

direction="right"

apple=pygame.image.load('images/apple.png')

def text_objects(text,color,size):
    global textSurface
    if size=='high':
        textSurface=largefont.render(text,True,color)
    elif size=='small':
        textSurface=medfont.render(text,True,color)
    return textSurface,textSurface.get_rect()


def message_to_screen(msg, color,size,text_displacement=0):
   textSurf,textRect=text_objects(msg,color,size)

   textRect.center=int((display_width/2)),int((display_height/2)+text_displacement)

   gameDisplay.blit(textSurf,textRect)



def score(score):
    text=medfont.render('Score: '+str(score),True,white)
    gameDisplay.blit(text,[0,0])

def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                        paused=False

                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(background,[0,0])
        message_to_screen('paused',white,'high',-100,)
        pygame.display.update()
        clock.tick(30)
def game_intro():
    intro=True
    while intro:
       gameDisplay.blit(background,(0,0))
       message_to_screen('welcome to snake',red,'high',-200)
       message_to_screen('by karan nakra',white,'high',-100)
       message_to_screen('press Enter to start',white,'small',50)
       message_to_screen('press Q to exit',white,'small',100)
       pygame.display.update()
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_q:
                   pygame.quit()
                   quit()
               if event.key==pygame.K_RETURN:
                   intro=False
                   gameLoop()
               if event.key==pygame.K_ESCAPE:
                   pygame.quit()
                   quit()
       clock.tick(30)

def snake(snake_list):
    if direction=="right":
        head=img
    if direction=='up':
        head=pygame.transform.rotate(img,90)
    if direction=='down':
        head=pygame.transform.rotate(img,270)
    if direction=='left':
        head=pygame.transform.rotate(img,180)

    gameDisplay.blit(head,(snake_list[-1][0],snake_list[-1][1]))
    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, white, [XnY[0], XnY[1], 10, 10])

def gameLoop():
    global direction
    mixer.music.load('audio/back_sound.mp3')
    mixer.music.play(-1)
    gameExit = False
    gameOver = False
    lead_x = int(display_height / 2 + 60)
    lead_y = int(display_width / 2 - 100)
    lead_x_change = 0
    lead_y_change = 0
    snake_list = []
    snake_length=5
    randApplex = round(random.randrange(50,display_width-100)/10)*10
    randAppley = round(random.randrange(50,display_height-100)/10)*10
    while not gameExit:
        while gameOver == True:
            message_to_screen('Game over',red,'high',-50,)
            message_to_screen('press ENTER to play again',white,'small',50)
            message_to_screen('press Q to quit',white,'small',140,)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_RETURN:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction='left'
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction='right'
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction='up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction='down'
                elif event.key==pygame.K_RETURN:
                    pause()

        if lead_x >= display_width - 10 or lead_x <= 0 or lead_y >= display_height - 10 or lead_y <= 0:
            gameOver = True
            mixer.music.load('audio/over_sound.mp3')
            mixer.music.play()
        appleThicness=30
        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(apple,(randApplex,randAppley))

        snake_head=[]
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        lead_x += lead_x_change
        lead_y += lead_y_change

        if len(snake_list)>snake_length:
            del snake_list[0]
        if snake_head in snake_list[:-1]:
            if snake_head==snake_list[0]:
                continue
            gameOver=True
            mixer.music.load('audio/over_sound.mp3')
            mixer.music.play()
        snake(snake_list)
        score(snake_length-5)
        pygame.display.update()
        if lead_x>=randApplex and lead_x<randApplex+appleThicness or lead_x+10>randApplex and lead_x+10 <randApplex+appleThicness:
                    if lead_y> randAppley and lead_y <randAppley+appleThicness:
                        randApplex = round(random.randrange(0, display_width-10) / 10) * 10
                        randAppley = round(random.randrange(0, display_height-10) / 10) * 10
                        snake_length+=1
                    elif lead_y +10>randAppley and lead_y +block_size<randAppley+appleThicness:
                        randApplex = round(random.randrange(0, display_width - 10) / 10) * 10
                        randAppley = round(random.randrange(0, display_height - 10) / 10) * 10
                        snake_length += 1
        clock.tick(fps)

    pygame.quit()
    quit()
game_intro()

