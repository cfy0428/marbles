import os, random, pygame
from pygame.locals import *
p = pygame







def collide_rect(recta,rectb):
    xla = round(recta[X],0)
    xra = round(recta[X] + recta[wid],0)
    yta = round(recta[Y],0)
    yba = round(recta[Y] + recta[hei],0)
    xlb = round(rectb[X],0)
    xrb = round(rectb[X] + rectb[wid],0)
    ytb = round(rectb[Y] ,0)
    ybb = round(rectb[Y] + rectb[hei],0)

    if xra >= xlb and xla <= xrb:
        if yba >= ytb and yta <= ybb:
            return True


def textprint(textname,textname2,textfond,textcolor,ypos,screen):
    textname = textfond.render(textname, True,textcolor)
    textname2 = textname.get_rect()
    textname2.centerx = screen.get_rect().centerx
    textname2.y = ypos
    screen.blit(textname, textname2)

def textprint2(textname,textname2,textfond,textcolor,screen):
    textname = textfond.render(textname, True,textcolor)
    textname2 = textname.get_rect()
    textname2.centerx = screen.get_rect().centerx
    textname2.centery = screen.get_rect().centery
    screen.blit(textname, textname2)

def gamein():
    texti = "弹球 v.2.0"
    textprint2(texti,"texti2",font3,RED,screen)
    p.display.update()
    p.time.wait(3000)

def gamequit():
    textqa = "欢迎游玩本游戏，本游戏由cfy制作。"
    textqb = "3秒后游戏将自动退出"
    screen.fill(BLACK)
    textprint(textqa,"textqa2",font2,WHITE,240,screen)
    textprint(textqb,"textqb2",font2,WHITE,340,screen)
    p.display.update()
    p.time.wait(3000)
    os._exit(0)


def not_too_fast(tick,time):
    if tick >= time:
        return True






p.init()
screen = p.display.set_mode((800,600))
p.display.set_caption("弹球 v.2.0")
timer = p.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

waiting = True
music = False
db_open = True
key_using = False
not_die = False
stop = False
over_best = True

db_text = "开启"
stop_text = "开始"
kt_text = ""

points=0
lives=5
points_max=0
game_vel = 1
timetick = 0
timetick2 = 0
fps = 30

photo = "photo"
X = "X"
Y = "Y"
velx = "velx"
vely = "vely"
wid = "width"
hei = "height"

ball = {photo:p.image.load("ball.bmp"),X:0,   Y:0,   velx:6,vely:6,wid:50, hei:50}
kt =   {photo:p.image.load("kt.bmp"),  X:18000,Y:18000,velx:0,vely:0,wid:50, hei:50}
db =   {photo:p.image.load("db.bmp"),  X:0,   Y:300, velx:5,vely:0,wid:300,hei:30}
db2 =  {photo:p.image.load("db2.bmp"), X:250, Y:0,   velx:0,vely:5,wid:30, hei:250}
paddle = {                             X:300, Y:550,               wid:105,hei:10}

photoball = p.image.load("ball.bmp")

colorkey = photoball.get_at((0,0))
photoball.set_colorkey(colorkey)

font = p.font.SysFont("华文宋体", 24)
font2 = p.font.SysFont("华文宋体", 50)
font3 = p.font.SysFont("华文彩云", 100)

timer = p.time.Clock()

try:
    p.mixer.init()
    popa=p.mixer.Sound("blip.wav")
    popb=p.mixer.Sound("blap.wav")
    music = True
except:
    print("因为不知道的原因，无法加载声音。")




gamein()

while True:    
    for event in p.event.get(): 
        if event.type == p.QUIT: 
            gamequit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP and game_vel <=3:
                if not stop and lives > 0:
                    game_vel +=0.2

            elif event.key == p.K_DOWN and game_vel >=0.6:
                if not stop and lives > 0:
                    game_vel -=0.2    

            elif event.key == p.K_RETURN:
                if db_open:
                    ball[velx] *= (5/3)
                    ball[vely] *= (5/3)
                    db_text = "关闭"
                else:
                    ball[velx] /= (5/3)
                    ball[vely] /= (5/3)
                    db_text = "开启"
                db_open = not db_open
            
            elif event.key ==p.K_LEFT:
                if not stop and not waiting and lives>0:
                    key_using = True
                    paddle[X] -=100
            
            elif event.key ==p.K_RIGHT:
                if not stop and not waiting and lives>0:
                    key_using = True
                    paddle[X] +=100
            
            elif event.key == p.K_SPACE:
                if waiting:
                    waiting = False
                    key_using = True
                elif lives == 0:
                    if over_best:
                        points_max = points
                    points=0
                    lives=5
                    ball = {photo:p.image.load("ball.bmp"),X:0,   Y:0,   velx:6,vely:6,wid:50, hei:50}
                    kt =   {photo:p.image.load("kt.bmp"),  X:18000,Y:18000,velx:0,vely:0,wid:50, hei:50}
                    db =   {photo:p.image.load("db.bmp"),  X:0,   Y:300, velx:5,vely:0,wid:300,hei:30}
                    db2 =  {photo:p.image.load("db2.bmp"), X:250, Y:0,   velx:0,vely:5,wid:30, hei:250}
                    paddle = {                             X:300, Y:550,               wid:105,hei:10}
                    game_vel = 1
                elif not waiting and lives > 0:
                    if key_using:
                        key_using = False
                    stop = not stop
                else:
                    stop = not stop 

            elif event.key == p.K_ESCAPE:
                gamequit()

        if event.type == p.MOUSEBUTTONDOWN:
            if p.mouse.get_pressed()[0]:
                if waiting:
                    waiting = False
                    key_using = False
                elif lives == 0:
                    if over_best:
                        points_max = points
                    points=0
                    lives=5
                    ball = {photo:p.image.load("ball.bmp"),X:0,   Y:0,   velx:6,vely:6,wid:50, hei:50}
                    kt =   {photo:p.image.load("kt.bmp"),  X:18000,Y:18000,velx:0,vely:0,wid:50, hei:50}
                    db =   {photo:p.image.load("db.bmp"),  X:0,   Y:300, velx:3,vely:0,wid:300,hei:30}
                    db2 =  {photo:p.image.load("db2.bmp"), X:250, Y:0,   velx:0,vely:3,wid:30, hei:250}
                    paddle = {                             X:300, Y:550,               wid:105,hei:10}
                    game_vel = 1
                elif not waiting and lives > 0:
                    if key_using:
                        key_using = False
                    stop = not stop
                else:
                    stop = not stop

            elif p.mouse.get_pressed()[2]:
                if db_open:
                    ball[velx] *= (5/3)
                    ball[vely] *= (5/3)
                    db_text = "关闭"
                else:
                    ball[velx] /= (5/3)
                    ball[vely] /= (5/3)
                    db_text = "开启"
                db_open = not db_open






    if paddle[X] > 800 - paddle[wid]:
        paddle[X] = 800 - paddle[wid]
    if paddle[X] < 0:
        paddle[X] = 0
    
    if not waiting:
        if not key_using:
            paddle[X] = p.mouse.get_pos()[0]
            paddle[X] -= paddle[wid]/2





    if not stop and not waiting and lives>0:
        ball[X] += ball[velx]
        ball[Y] += ball[vely]
        db[X] += db[velx]
        db2[Y] += db2[vely]
        timetick += 1
        timetick2 += 1




    if ball[X] < 0 or ball[X] +ball[wid] > 800:
        ball[velx] *= -1

    if ball[Y] < 0:
        ball[vely] *= -1

    if ball[Y] >= 550:
        if not not_die:
            lives -= 1
            ball[X] = paddle[X] + paddle[wid]
            stop_text = "继续"
            waiting = True

            if game_vel > 1.2:
                game_vel -= 0.4
            if game_vel > 1.6:
                game_vel -= 0.2
            if game_vel > 2:
                game_vel = 1.2
            
            if music:
                popb.play()

            if db_open:
                ball[velx] = 6
                ball[vely] = -6
            else:
                ball[velx] = 10
                ball[vely] = -10
            
            ball[Y] = 499

            if ball[X] < 0:
                ball[X] = 0
            if ball[X] > 750:
                ball[X] = 750
    




    if kt[Y] > 15000  or kt[X] > 15000:
        if lives > 0 and not stop and not waiting:
            not_die = False
            kt_text = ""
            paddle[wid] = 105
            kt[X] = random.randint(0,800)
            kt[Y] = 0
            kt[velx] = random.randint(-20,20)
            kt[vely] = random.randint(80,100)
    
    kt[X] += kt [velx]
    kt[Y] += kt [vely]
    if collide_rect(kt, paddle):
        choose = random.randint(1,5)
        if choose == 1:
            lives+=2
            kt_text = "你增加了2条命！"

        elif choose == 2:
            paddle[wid] *= 2
            kt_text = "你的挡板增长了一倍！"

        elif choose == 3:
            ball[velx] /=1.5
            ball[vely] /=1.5
            kt_text = "你的球速除以了1.5！"

        elif choose == 4:
            aaa = random.randint(1,3)
            if aaa ==1:
                ball[velx] *= -1

            elif aaa ==2:
                ball[vely] *= -1

            else:
                ball[velx] *= -1
                ball[vely] *= -1

            kt_text = "改变球的方向！"

        else:
            not_die = True
            kt_text = "你获得了暂时的无敌！"





    if collide_rect(ball,paddle):
        points += game_vel
        ball[velx] *= 1.1
        ball[vely] *= -1.1
        if music:
            popa.play()
    




    if db[X] >= 500 or db[X] <= 0:
        db[velx] *= -1*random.randint(90,110)/100
    
    if db2[Y] >= 350 or db2[Y] <= 0:
        db2[vely] *= -1*random.randint(90,110)/100
    
    if db_open :
        if collide_rect(ball,db):
            if not_too_fast(timetick,fps//2):
                timetick = 0
                ball[vely] *= -1
            timetick = 0

        if collide_rect(ball,db2):
            if not_too_fast(timetick2,fps//2):
                ball[velx] *= -1
            timetick2 = 0
   

    if lives <1:
        points = round(points,1)
        points_dif = points - points_max

        if points_dif > 0:
            kt_text = "恭喜你创造了纪录，超过最高记录："+str(round(abs(points_dif),1))+"分!"
            over_best = True
        else:
            kt_text = "你离最高纪录："+str(points_max)+"还差"+str(abs(points_dif))+"分，加油!"

    if not waiting:          
        text = "生命数: " + str(lives) + " 分数: " + str(round(points,1))
        text +=" 倍速："+str(round(game_vel,1))
        text +=" 速度："+str(round(abs(ball[velx])*fps*(2**0.5),1))

    if waiting:
        text = "等待状态中，按下鼠标左键或空格"+stop_text+"游戏。"

    if key_using:
        mode = " 键盘模式"
    else: mode = " 鼠标模式"

    text +=mode
    text +=" 挡板"
    text +=db_text
                       
    if lives <1:
        ball[velx] = ball[vely] = 0
        text="游戏结束。你的分数是："+str(points)
        text+="。请按鼠标左键或空格键重新开始。"
        waiting = False
    if stop:
        text="已暂停，按鼠标左键或空格继续。"
        
 
    





    fps = 30*game_vel
    timer.tick(fps)
    ticks = p.time.get_ticks()

    screen.fill(BLACK)

    if db_open:
        screen.blit(db[photo],(db[X],db[Y]))
        screen.blit(db2[photo],(db2[X],db2[Y]))

    textprint(text,"texta",font,WHITE,10,screen)
    textprint(kt_text,"textkt",font,WHITE,550,screen)  
    p.draw.rect(screen, RED, (paddle[X],paddle[Y],paddle[wid],paddle[hei]))
    screen.blit(photoball,(ball[X],ball[Y]))
    screen.blit(kt[photo],(kt[X],kt[Y]))
   
    
    p.display.update()      