import pygame
import math
import random


#this code is not bad,ITS FUCKING HORRIBLE!!

#every sprite class in this game
#__init__() -> prepare the required sprite
#update(x,y) -> change sprite position to (x,y)

class player_walk(pygame.sprite.Sprite):
    def __init__(self):
        super(player_walk,self).__init__()

        self.walk=[]
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk1b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk2b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk3b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk4b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk4b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk4b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk4b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk4b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk5b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk6b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))
        self.walk.append(pygame.image.load('assasin/walk/walk7b.png'))

        self.index = 0

        self.image = self.walk[self.index]

        # creating a rect at pos_x,pos_y,image_width,image_height
        self.rect = pygame.Rect(130, 558, 48, 62)

    def update(self,x,y,ijump):
        self.index += 1  # going through the array containing sprites

        if self.index >= len(self.walk):  # if index reaches the end of the array then start again from index 0
            self.index = 0 
        
        self.rect= pygame.Rect(x,y,48,62)

        self.image = self.walk[self.index]

class player_jump(pygame.sprite.Sprite):  # sprite collection of jumping man
    def __init__(self):
        super(player_jump, self).__init__()

        self.jump = []
        self.jump.append(pygame.image.load('assasin/jump/jump1b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump2b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump3b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump4b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jumpe1b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jumpe2b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jumpe3b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jumpe4b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump5b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump6b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump7b.png'))
        self.jump.append(pygame.image.load('assasin/jump/jump8b.png'))

        self.index = 0

        self.image = self.jump[self.index]

        # creating a rect at pos_x,pos_y,image_width,image_height
        self.rect = pygame.Rect(130, 518, 48, 62)

    def update(self,x,y,ijump=1):
        self.index += ijump


        self.rect = pygame.Rect(x,y,48,62)

        if self.index >= len(self.jump):  # if index reaches the end of the array then start again from index 0
            self.index = 0
        if ijump == 0:
            self.index = 1

        self.image = self.jump[self.index]
        

class player_roll(pygame.sprite.Sprite):
    def __init__(self):
        super(player_roll,self).__init__()
        self.roll=[]
        
        for i in range (0,30):
            self.roll.append(pygame.image.load("assasin/roll/rolle1b.png"))
            self.roll.append(pygame.image.load("assasin/roll/rolle3b.png"))

        self.index=0

        self.image=self.roll[self.index]
        self.rect = pygame.Rect(130, 558, 48, 30)
        
    def update(self,x,y,ijump):
        self.index +=1 # going through the array containing sprites

        if self.index >= len(self.roll):  # if index reaches the end of the array then start again from index 0
            self.index = 0 
        
        self.rect= pygame.Rect(x,y,48,30)

        self.image = self.roll[self.index]
        


class enemy_walk(pygame.sprite.Sprite):  # sprite collection of walking wolf
    def __init__(self,offset):
        super(enemy_walk, self).__init__()

        self.walk = []
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk1.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk2.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk3.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk4.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk5.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))
        self.walk.append(pygame.image.load('wolf/walk/walk6.png'))

        self.index = 0 + 3*offset

        self.image = self.walk[self.index]

        # creating a rect at position x,y (5,5) of size (100,198) which is the size of sprite
        self.rect = pygame.Rect(-55 , 558,100, 198)

    def update(self,x,y):
        self.index += 1

        self.rect = pygame.Rect(x,y,100,198)

        if self.index >= len(self.walk):  # if index reaches the end of the array then start again from index 0
            self.index = 0

        self.image = self.walk[self.index]

class obstacles(pygame.sprite.Sprite):
    def __init__(self,x,y,obstype):
        super(obstacles,self).__init__()

        self.imglist=[]
        self.imglist.append(pygame.image.load('obstacle.png'))
        self.imglist.append(pygame.image.load('obstacle2.png'))
        self.image = self.imglist[obstype]
        if not obstype:
            self.rect = pygame.Rect(x,y,138,174)
        else:
            self.rect = pygame.Rect(x,y-180,97,253)

    def update(self,x,y,obstype):
        if not obstype:
            self.rect = pygame.Rect(x,y,138,174)
        else:
            self.rect = pygame.Rect(x,y-180,97,253)
        self.image= self.imglist[obstype]

#function to determine score
def scores(x,y,score_value):
    font = pygame.font.Font('score_font2.ttf',64)
    score_value*=100
    score = font.render("Distance:"+ str(int(score_value)/10)+" m",True,(0,0,255))
    return score

#function to determine whether man has collided or tripped on an obstacle
def collided(s1,s2,py,oy,tripped,obsno):    
    for il in s2.sprites():
        for jl in s1.sprites():
            if pygame.sprite.collide_mask(il,jl) and (py>oy or tripped>1 or obsno):
                    return 1
            elif pygame.sprite.collide_mask(il,jl):
                    return -1
    return 0

#ze jumper quadratic function    
def f(x):
    return 300-(x*x/300)

#the main game
def main():
    # initialize
    pygame.mixer.pre_init(44100,-16,2,512)
    pygame.mixer.quit()
    pygame.mixer.init(44100,-16,2,512)
    pygame.init()
    pygame.fastevent.init()
    clock = pygame.time.Clock()

    # create the screen
    screen = pygame.display.set_mode((1024,768))
    
    #display the icon
    pygame.display.set_caption("Werewolf Run")
    icon =pygame.image.load("werewolf.png")
    pygame.display.set_icon(icon)

    #load the background
    background = pygame.image.load("bg_enhanced.png")
    bg_x=0
    bg_x2=background.get_rect().width
    rec_width=background.get_rect().width
    bgmf=2*rec_width

    #start the music
    pygame.mixer.music.load("music/choice1.mp3")
    pygame.mixer.music.play(-1)

    #place the player and the enemy
    playerX = 130-130
    playerY = 768-210
    playerX_change=0
    enemyX=-55-130 
    enemyY=768-140

    #set the player near the enemy
    closecount=2000
    tripped=1

    #load the obstacles at appropiate positions
    my_group_obstacles=[pygame.sprite.Group(obstacles(3024,528,0)),pygame.sprite.Group(obstacles(3624,528,0)),pygame.sprite.Group(obstacles(4224,528,0))]
    obstacleX= [3024,3624,4224]
    obsnum= [0,0,0]
    obsXlists = [[1048,1648,2248],[1048,1548,2048],[1148,1696,1948],[1048,1648,2148]]
    obstacleY=708-200
    obsnoslist=[[0,1,0],[1,0,1],[1,0,0],[0,0,1]]
    obstacleX_change=-6

    #prepare the player and wolves sprites
    my_group_man_walk = pygame.sprite.Group(player_walk())
    my_group_man_jump = pygame.sprite.Group(player_jump())
    my_group_man_roll = pygame.sprite.Group(player_roll())
    my_group_man=[my_group_man_walk,my_group_man_jump,my_group_man_roll]
    my_group_wolf_walk_list = [pygame.sprite.Group(enemy_walk(0)),pygame.sprite.Group(enemy_walk(1)),pygame.sprite.Group(enemy_walk(2))]
    
    #create the sounds
    wolf_cry=pygame.mixer.Sound(file="music/wolfcry.wav")
    wolf_break=pygame.mixer.Sound(file="music/stonecrack.wav")
    man_jump_Sound=pygame.mixer.Sound(file="music/man_jump.wav")
    man_roll_Sound=pygame.mixer.Sound(file="music/roll.wav")
    man_death_Sound=pygame.mixer.Sound(file="music/death.wav")

    #accomodate the sound channels to play the sounds
    wolf_cry_channel=pygame.mixer.Channel(0)
    wolf_break_channel=pygame.mixer.Channel(1)
    man_jump_sound_channel=pygame.mixer.Channel(2)
    man_roll_sound_channel=pygame.mixer.Channel(3)
    man_death_sound_channel=pygame.mixer.Channel(4)

    #intro of the run
    wolf_cry_channel.play(wolf_cry)
    while playerX<132:
        
        #move the background
        bg_x=(bg_x+int(obstacleX_change))%bgmf - rec_width
        bg_x2=(bg_x2+int(obstacleX_change))%bgmf - rec_width

        #check if the game is ruuning
        for event in pygame.fastevent.get():
            if event.type == pygame.QUIT:
                exit()

        #draw the background
        screen.blit(background,(bg_x,0))
        screen.blit(background,(bg_x2,0))

        #draw the man and the wolves
        my_group_man_walk.draw(screen)
        my_group_man_walk.update(playerX,playerY,0)
        k=0
        for jk in my_group_wolf_walk_list:
            jk.draw(screen)
            jk.update(enemyX+k,enemyY)
            k=pow(-1,k)*29

        #move the man and enemies
        playerX-=obstacleX_change/2
        enemyX-=obstacleX_change/2

        #update the display
        pygame.display.update()
        clock.tick(60)

    #initialise the remaining variables
    score_value=0
    textX = 10
    textY = 10

    obstacleX_change=-9
    i=300
    l=30
    jumping=False
    rolling=False
    man_jump=1
    running = True
    while running:
        #move the background
        bg_x=(bg_x+int(obstacleX_change))%bgmf - rec_width
        bg_x2=(bg_x2+int(obstacleX_change))%bgmf - rec_width
        
        #check whether game is running
        for event in pygame.fastevent.get():
            if event.type == pygame.QUIT:
                exit()

        #draw the background
        screen.blit(background,(bg_x,0))
        screen.blit(background,(bg_x2,0))

        #detect the keys pressed
        keys=pygame.key.get_pressed()

        #roll
        if not(rolling or jumping):
            if keys[pygame.K_SPACE]:
                man_jump_sound_channel.play(man_jump_Sound)
                i=-300
                jumping=True
                rolling=False
            elif keys[pygame.K_DOWN]:
                l=-100
                man_roll_sound_channel.play(man_roll_Sound)
                rolling=True

        spriteval=2*rolling+jumping
        #check for collision between man and obstacles
        for j in range(0,3):
            if obstacleX[j]<250 and obstacleX[j]>0:    
                if collided(my_group_man[spriteval],my_group_obstacles[j],playerY,obstacleY,tripped,obsnum[j]) == 1:
                            man_death_Sound.play()
                            pygame.display.quit()
                            return score_value*100
                elif collided(my_group_man[spriteval],my_group_obstacles[j],playerY,obstacleY,tripped,obsnum[j]) == -1:
                            tripped+=1
                            closecount=1
                            wolf_cry.play()
                            if tripped>1:
                                continue
                            i=-100 
            if(closecount>0 and closecount<3000):
                    closecount+=1
                    enemyX+=1
                    if enemyX>0:
                        enemyX=0
            
            #take enemies back
            elif(closecount>=3000 or closecount==0):
                    closecount=0
                    tripped=0   
                    enemyX-=1
                    if enemyX<-55:
                        enemyX=-55 
            
            #move the obstacles
            obstacleX[j] += int(obstacleX_change)
            
            #if obstacles cross the wolf
            if obstacleX[j] <= enemyX + 80 and obstacleX[j] > 0 and enemyY>obstacleY and obsnum[j]==0:
                wolf_break.play()
                obstacleX[j] = -142
                #wolf_break_channel.play(wolf_break)

            #if pattern finished load new pattern    
            if obstacleX[2] <= -142:
                obsno=random.randint(0,3)
                obstacleX = obsXlists[obsno] + []
                obsnum = obsnoslist[obsno] + []

            #draw the obstacles
            my_group_obstacles[j].draw(screen)
            my_group_obstacles[j].update(obstacleX[j],obstacleY,obsnum[j])
       
        my_group_man[spriteval].draw(screen)
        my_group_man[spriteval].update(playerX,playerY,man_jump)

        if jumping:
            playerY=558-f(i)
            if i>=300:
                #jump complete
                jumping=False
            #only for jump sprites    
            elif i>-296 and i<225:
                man_jump=0
            else:
                man_jump=1
            i-=int(obstacleX_change)    
            if i>= 300 and playerY>=558:
                playerY=558

        elif rolling:
            #draw the rolling man
            l+=5
            if l>=50:
                #roll complete
                rolling=False

        #increment speed of obstacle movement        
        obstacleX_change-=0.001

        #increment score
        score_value+=0.01 -(obstacleX_change + 2)/100

        #display score  
        screen.blit(scores(textX,textY,score_value),(textX,textY))

        #draw the wolves
        k=0
        for jk in my_group_wolf_walk_list:
            jk.draw(screen)
            jk.update(enemyX+k,enemyY)
            k=pow(-1,k)*29

        #limit the speed of both
        if obstacleX_change <= -20:
            obstacleX_change = -20
        clock.tick(60)

        #update the display
        pygame.display.update()

if(__name__=="__main__"):
    main()
