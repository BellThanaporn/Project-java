import pygame  ##line 1-6 Importing various modules of the game And start the Pygame library.
from paddle import Paddle 
from ball import Ball
from brick import Brick

pygame.init() 

GRAY = ('#EBEBD3') #line8-14 กำหนดค่าสีต่างๆที่เราจะใช้ 
BLACK = (0,0,0)
DRAKBLUE = ('#292F36')
YELLOW = ('#FFE66D')
PINK = ('#FF6B6B')
WHITE = ('#F7FFF7')
BLUE =('#4ECDC4')

screen = pygame.display.set_mode((800,600)) ### line16-20 กำหนดขนาดหน้าต่าง เซตชื่อเกมและไอคอนเกม โหลดภาพที่ใช้ ###
background = pygame.image.load('bg.jpg') 
icon = pygame.image.load('ball.png') 
pygame.display.set_icon(icon)
pygame.display.set_caption("Breakout Game")

score = 0 #line 22-23 กำหนดตัวแปรหลักที่จะโชว์ที่หน้าต่าง ###
lives =5

all_sprites_list = pygame.sprite.Group() #line 25 เก็บตัวละครต่างๆในเกมเพื่อแสดงผล


paddle = Paddle(DRAKBLUE, 110, 10) # line 28-34 สร้าง paddle และ Ball โดยคลาส paddle และ คลาสball
paddle.rect.x = 350 
paddle.rect.y = 560

ball = Ball(GRAY,20,20)
ball.rect.x = 345
ball.rect.y = 245

all_bricks = pygame.sprite.Group()  #line36-60 สร้าง brick โดยคลาส brick และเก็บเข้ากลุ่มของ brick กับ กลุ่มของ สไปร์ท
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 50 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(6):
    brick = Brick(PINK,80,30)
    brick.rect.x = 75 + i* 110
    brick.rect.y = 100 
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(WHITE,80,30)
    brick.rect.x = 50 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(6):
    brick = Brick(BLUE,80,30)
    brick.rect.x = 75 + i* 110
    brick.rect.y = 180
    all_sprites_list.add(brick)
    all_bricks.add(brick)

all_sprites_list.add(paddle) #line62-63 เพิ่ม sprite ที่สร้างเข้ากลุ่มสไปร์ท
all_sprites_list.add(ball)

clock = pygame.time.Clock() #line 65 นาฬิกาจะใช้เพื่อควบคุมความเร็วในการอัปเดตหน้าจอ##

carryOn = True 
# -------- Main Program Loop -----------
while carryOn: #69-139 Main Program Loop 
    # --- Main event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(8) 
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(8)
   
    # --- Game logic should go here
    all_sprites_list.update()

    if ball.rect.x>=780:
        ball.vel[0] = -ball.vel[0]
        
    if ball.rect.x<=0:
        ball.vel[0] = -ball.vel[0]
        
    if ball.rect.y>580:
        ball.vel[1] = -ball.vel[1]
        lives -= 1

        if lives == 0:
            font = pygame.font.Font('manaspc.ttf', 70) 
            textt = font.render("GAME OVER",1, WHITE) 
            screen.blit(textt, (190,250))
            pygame.display.flip()
            pygame.time.delay(3000)

            #Stop the Game
            carryOn=False

    if ball.rect.y<40:
       ball.vel[1] = -ball.vel[1]

    if pygame.sprite.collide_mask(ball, paddle): 
       ball.bounce()
        
        
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,True) 
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      if len(all_bricks)==0:
            font = pygame.font.Font('manaspc.ttf', 60)
            text = font.render("LEVEL COMPLETE", 10, WHITE)
            screen.blit(text, (120,250))
            pygame.display.flip()
            pygame.time.delay(3000)

            #Stop the Game
            carryOn=False

    screen.blit(background, [0, 0])  ##line125-136 ส่วนที่ทำให้หน้าจอมีการแสดงผลทางหน้าจอ เช่น background ,line,text,sprite 
    pygame.draw.line(screen, GRAY, [0, 38], [800, 38],3)

    font = pygame.font.Font('manaspc.ttf', 23)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10)) 
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()

    clock.tick(60) #- Limit to 60 frames per second

pygame.quit() #ใช้เพื่อออกจากโปรแกรมทั้งหมด##
