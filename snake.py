import pygame
import time
import random
pygame.init() 
screen_width=640
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
speed=4
bigfoodstatus=False
screen_height=480
gamewindow=pygame.display.set_mode((screen_width,screen_height))
gameclock=pygame.time.Clock()
gamefont=pygame.font.SysFont(None,36)
pygame.display.set_caption("Snake game")
icon=pygame.image.load("snake.png")
pygame.display.set_icon(icon)
# game variables
foodSize=15
bigfoodSize=20
foodX=random.randint(1,screen_width-foodSize)
foodY=random.randint(1,screen_height-foodSize)
bigfoodX=random.randint(1,screen_width-bigfoodSize)
bigfoodY=random.randint(1,screen_height-bigfoodSize)
gameRunning=True
headX=100
headY=100
headSize=25
changeX=0
changeY=0
score=0
snake_list=[]
snake_length=1
gameover=False
x=random.randint(0,255)
y=random.randint(0,255)
z=random.randint(0,255)
score_color=(x,y,z)
while gameRunning:
    eventList=pygame.event.get()
    for event in eventList:
        if event.type==pygame.QUIT:
            gameRunning=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN and gameover==True:
                gameover=False
                headX=100
                headY=100
                speed=4
                changeX=0
                changeY=0
                snake_length=1
                foodX=random.randint(1,screen_width)
                foodY=random.randint(1,screen_height)
                snake_list=[]
                score=0
            elif event.key==pygame.K_RIGHT and changeX!= -4:
                changeX=speed
                changeY=0
            elif event.key==pygame.K_LEFT and changeX != 4:
                changeX=-speed
                changeY=0
            elif event.key==pygame.K_DOWN and changeY != -4:
                changeY=speed
                changeX=0
            elif event.key==pygame.K_UP and changeY!= 4:
               changeY=-speed
               changeX=0

    if headY<0 or headY>screen_height-headSize or headX<0 or headX>screen_width-headSize:
        gamewindow.fill(white)
        gameover=True
        final_text=gamefont.render("GAMEOVER, press enter to continue", True,red)
        gamewindow.blit(final_text,(100,100))
    elif [headX,headY] in snake_list[:len(snake_list)-1]:
        gameover=True
        gamewindow.fill(white)
        gameover=True
        final_text=gamefont.render("GAMEOVER, press enter to continue", True,red)
        gamewindow.blit(final_text,(100,100))
    else:

        headX= headX+ changeX
        headY= headY+ changeY
        #adding these updated coordinates to the snake coordinate list
        snake_list.append([headX,headY])
        if len(snake_list)>snake_length:
            del snake_list[0]
        # setting the window colour to white
        gamewindow.fill(white)
        pygame.draw.rect(gamewindow,red,[foodX,foodY,foodSize,foodSize])
        if bigfoodstatus==True:
            pygame.draw.rect(gamewindow,blue,[bigfoodX,bigfoodY,bigfoodSize,bigfoodSize])
            stopwatch.start()
            if stopwatch.duration>5:
                stopwatch.stop()
                stopwatch.reset()
                bigfoodstatus=False
            if abs(headX-bigfoodX)<=22 and abs(headY-bigfoodY)<=22:
                score=score+5
                bigfoodstatus=False
        for x,y in snake_list:
            pygame.draw.rect(gamewindow,black,[x,y,headSize,headSize])
        # collision code
        if abs(headX-foodX)<=22 and abs(headY-foodY)<=22:
            score=score+1
            if score%5==0 and score!=0:
                speed=speed+0.5
                bigfoodstatus=True
            snake_length=snake_length+5
            x=random.randint(0,255)
            y=random.randint(0,255)
            z=random.randint(0,255)
            score_color=(x,y,z)
            foodX=random.randint(1,screen_width-foodSize)
            foodY=random.randint(1,screen_height-foodSize)
        score_text=gamefont.render(f"The score is {score}",True,score_color)
        gamewindow.blit(score_text,[5,5])
    
    #updating the game window
    gameclock.tick(60)
    #to put 1 surface object over another, we use blit function
    pygame.display.update()

pygame.quit()
quit()