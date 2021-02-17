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
    texti = "弹球 v.3.0"
    textprint2(texti,"texti2",font3,RED,screen)
    p.display.update()
    p.time.wait(3000)

def gamequit():
    textqa = "欢迎游玩本游戏，本游戏由cfy制作。"
    textqb = "3秒后游戏将自动退出"
    screen.fill(BLACK)
    textprint(textqa,"textqa2",font2,WHITE,350,screen)
    textprint(textqb,"textqb2",font2,WHITE,500,screen)
    p.display.update()
    p.time.wait(3000)
    os._exit(0)


def not_too_fast(tick,time):
    if tick >= time:
        return True






p.init()
screen = p.display.set_mode((1200,900))
p.display.set_caption("弹球 v.3.0")
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
ball_f = True
ball_s = True  

db_text = "开启"
stop_text = "开始"
kt_text = ""

points=0
lives=5
points_max=0
game_vel = 1
timetick = 0
timetick2 = 0
timetick3 = 0
timetick4 = 0
timetick5 = 0
timetick6 = 0
timetick7 = 0
fps = 60


photo = "photo"
X = "X"
Y = "Y"
velx = "velx"
vely = "vely"
wid = "width"
hei = "height"

ball = {photo:p.image.load("ball.bmp"),X:0,     Y:0,     velx:4,  vely:4,  wid:50, hei:50}
ball2 ={photo:p.image.load("ball2.bmp"),X:1149, Y:1,     velx:-4, vely:4,  wid:50, hei:50}
kt =   {photo:p.image.load("kt.bmp"),  X:18000, Y:18000, velx:0  ,vely:0,  wid:50, hei:50}
db =   {photo:p.image.load("db.bmp"),  X:0,     Y:400,   velx:7/2,vely:0,  wid:300,hei:30}
db2 =  {photo:p.image.load("db2.bmp"), X:350,   Y:0,     velx:0  ,vely:7/2,wid:30, hei:250}
paddle = {                             X:400,   Y:850,                     wid:150,hei:15}

photoball = p.image.load("ball.bmp")

colorkey = photoball.get_at((0,0))
photoball.set_colorkey(colorkey)


photoball2 = p.image.load("ball2.bmp")

colorkey2 = photoball2.get_at((0,0))
photoball2.set_colorkey(colorkey2)


font = p.font.SysFont("华文宋体", 36)
font2 = p.font.SysFont("华文宋体", 72)
font3 = p.font.SysFont("华文彩云", 128)

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
                    ball2[velx] *= (5/3)
                    ball2[vely] *= (5/3)
                    db_text = "关闭"
                else:
                    ball[velx] /= (5/3)
                    ball[vely] /= (5/3)
                    ball2[velx] /= (5/3)
                    ball2[vely] /= (5/3)
                    db_text = "开启"
                db_open = not db_open
            
            elif event.key ==p.K_LEFT:
                if not stop and not waiting and lives>0:
                    key_using = True
                    paddle[X] -=140
            
            elif event.key ==p.K_RIGHT:
                if not stop and not waiting and lives>0:
                    key_using = True
                    paddle[X] +=140
            
            elif event.key == p.K_SPACE:
                if waiting:
                    waiting = False
                    key_using = True
                elif lives == 0:
                    if over_best:
                        points_max = points
                    points=0
                    lives=5 
                    ball = {photo:p.image.load("ball.bmp"),X:0,     Y:0,     velx:4,  vely:4,  wid:50, hei:50}
                    ball2 ={photo:p.image.load("ball2.bmp"),X:1149, Y:1,     velx:-4, vely:4,  wid:50, hei:50}
                    kt =   {photo:p.image.load("kt.bmp"),  X:18000, Y:18000, velx:0  ,vely:0,  wid:50, hei:50}
                    db =   {photo:p.image.load("db.bmp"),  X:0,     Y:400,   velx:7/2,vely:0,  wid:300,hei:30}
                    db2 =  {photo:p.image.load("db2.bmp"), X:350,   Y:0,     velx:0  ,vely:7/2,wid:30, hei:250}
                    paddle = {                             X:400,   Y:850,                     wid:150,hei:15}
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
                    ball = {photo:p.image.load("ball.bmp"),X:0,     Y:0,     velx:4,  vely:4,  wid:50, hei:50}
                    ball2 ={photo:p.image.load("ball2.bmp"),X:1149, Y:1,     velx:-4, vely:4,  wid:50, hei:50}
                    kt =   {photo:p.image.load("kt.bmp"),  X:18000, Y:18000, velx:0  ,vely:0,  wid:50, hei:50}
                    db =   {photo:p.image.load("db.bmp"),  X:0,     Y:400,   velx:7/2,vely:0,  wid:300,hei:30}
                    db2 =  {photo:p.image.load("db2.bmp"), X:350,   Y:0,     velx:0  ,vely:7/2,wid:30, hei:250}
                    paddle = {                             X:400,   Y:850,                     wid:150,hei:15}
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
                    ball2[velx] *= (5/3)
                    ball2[vely] *= (5/3)
                    db_text = "关闭"
                else:
                    ball2[velx] /= (5/3)
                    ball2[vely] /= (5/3)
                    db_text = "开启"
                db_open = not db_open






    if paddle[X] > 1200 - paddle[wid]:
        paddle[X] = 1200 - paddle[wid]
    if paddle[X] < 0:
        paddle[X] = 0
    
    if not waiting:
        if not key_using:
            paddle[X] = p.mouse.get_pos()[0]
            paddle[X] -= paddle[wid]/2





    if not stop and not waiting and lives>0:
        if ball_f:
            ball[X] += ball[velx]
            ball[Y] += ball[vely]
        if ball_s:
            ball2[X] += ball2[velx]
            ball2[Y] += ball2[vely]
        db[X] += db[velx]
        db2[Y] += db2[vely]
        timetick += 1
        timetick2 += 1
        timetick3 += 1
        timetick4 += 1
        timetick5 += 1
        timetick6 += 1
        timetick7 += 1



    if ball[X] < 0 or ball[X] +ball[wid] > 1200:
        ball[velx] *= -1

    if ball[Y] < 0:
        ball[vely] *= -1

    if ball[Y] >= 850:
        if not not_die:
            if not ball_s :
                lives -= 1
                ball[X] = paddle[X] + paddle[wid]
                stop_text = "继续"
                waiting = True
            if ball_f and ball_s:
                ball_f = False
                timetick3 = 0

            if game_vel > 1.2:
                game_vel -= 0.4
            if game_vel > 1.6:
                game_vel -= 0.2
            if game_vel > 2:
                game_vel = 1.2
            
            if music:
                popb.play()

            if db_open:
                ball[velx] = 4
                ball[vely] = -4
            else:
                ball[velx] = 20/3
                ball[vely] = -20/3
            
            ball[Y] = 799

            if ball[X] < 0:
                ball[X] = 0
            if ball[X] > 1150:
                ball[X] = 1150
        else:
            ball[vely] *= -1








    if ball2[X] < 0 or ball2[X] +ball2[wid] > 1200:
        ball2[velx] *= -1

    if ball2[Y] < 0:
        ball2[vely] *= -1

    if ball2[Y] >= 850:
        if not not_die:
            if not ball_f :
                lives -= 1
                ball2[X] = paddle[X] + paddle[wid]
                stop_text = "继续"
                waiting = True
            if ball_f and ball_s:
                ball_s = False
                timetick3 = 0

            if game_vel > 1.2:
                game_vel -= 0.4
            if game_vel > 1.6:
                game_vel -= 0.2
            if game_vel > 2:
                game_vel = 1.2
            
            if music:
                popb.play()

            if db_open:
                ball2[velx] = 4
                ball2[vely] = -4
            else:
                ball2[velx] = 20/3
                ball2[vely] = -20/3
            
            ball2[Y] = 799

            if ball2[X] < 0:
                ball2[X] = 0
            if ball2[X] > 1150:
                ball2[X] = 1150
        else:
            ball2[vely] *= -1








    if kt[Y] > 30000  or kt[X] > 30000:
        if lives > 0 and not stop and not waiting:
            not_die = False
            kt_text = ""
            paddle[wid] = 150
            kt[X] = random.randint(0,1200)
            kt[Y] = 0
            kt[velx] = random.randint(-10,10)
            kt[vely] = random.randint(30,80)
    
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
            ball2[velx] /=1.5
            ball2[vely] /=1.5
            kt_text = "你的球速除以了1.5！"

        elif choose == 4:
            aaa = random.randint(1,3)
            if aaa ==1:
                ball[velx] *= -1
                ball2[velx] *= -1

            elif aaa ==2:
                ball[vely] *= -1
                ball2[vely] *= -1

            else:
                ball[velx] *= -1
                ball[vely] *= -1
                ball2[velx] *= -1
                ball2[vely] *= -1

            kt_text = "改变球的方向！"

        else:
            not_die = True
            kt_text = "你获得了暂时的无敌！"





    if collide_rect(ball,paddle):
        if not_too_fast(timetick6,fps//2):
            points += game_vel
            ball[velx] *= 1.1
            ball[vely] *= -1.1
            if music:
                popa.play()
        timetick6 = 0


    if collide_rect(ball2,paddle):
        if not_too_fast(timetick7,fps//2):
            points += game_vel
            ball2[velx] *= 1.1
            ball2[vely] *= -1.1
            if music:
                popa.play()
        timetick7 = 0
    




    if db[X] >= 700 or db[X] <= 0:
        db[velx] *= -1*random.randint(90,110)/100
    
    if db2[Y] >= 650 or db2[Y] <= 0:
        db2[vely] *= -1*random.randint(90,110)/100
    



    if db[velx] > 0:
        if db[velx] > 7:db[velx] = 7
        if db[velx] < 3/2:db[velx] = 3/2
        
    else:
        if db[velx] < -7:db[velx] = -7
        if db[velx] > -3/2:db[velx] = -3/2


    if db2[vely] > 0:
        if db2[vely] > 7:db2[vely] = 7
        if db2[vely] < 3/2:db2[vely] = 3/2
    
    else:
        if db2[vely] < -7:db2[vely] = -7
        if db2[vely] > -3/2:db2[vely] = -3/2







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
   

    if db_open :
        if collide_rect(ball2,db):
            if not_too_fast(timetick4,fps//2):
                timetick = 0
                ball2[vely] *= -1
            timetick4 = 0

        if collide_rect(ball2,db2):
            if not_too_fast(timetick5,fps//2):
                ball2[velx] *= -1
            timetick5 = 0



    if not ball_s:
        if ball_f:
            if timetick3 == 1800:
                ball_s = True
                ball2[Y]= 1

    if not ball_f:
        if ball_s:
            if timetick3 == 1800:
                ball_f = True
                ball[Y]= 1



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
        if ball_f and ball_s:
            text +=" 速度："+str(round(abs(ball[velx])*fps*(2**0.5),1))+","+str(round(abs(ball2[velx])*fps*(2**0.5),1))
        else:
            if ball_f:
                text +=" 速度："+str(round(abs(ball[velx])*fps*(2**0.5),1))+" 恢复时间："+str(round(((1800-timetick3)/60),1))+"s"
            if ball_s:
                text +=" 速度："+str(round(abs(ball2[velx])*fps*(2**0.5),1))+" 恢复时间："+str(round(((1800-timetick3)/60),1))+"s"
        



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
        ball2[velx] = ball2[vely] = 0
        text="游戏结束。你的分数是："+str(points)
        text+="。请按鼠标左键或空格键重新开始。"
        waiting = False
    if stop:
        text="已暂停，按鼠标左键或空格继续。"
        
 
    





    fps = 60*game_vel
    timer.tick(fps)
    ticks = p.time.get_ticks()

    screen.fill(BLACK)

    if db_open:
        screen.blit(db[photo],(db[X],db[Y]))
        screen.blit(db2[photo],(db2[X],db2[Y]))

    textprint(text,"texta",font,WHITE,10,screen)
    textprint(kt_text,"textkt",font,WHITE,850,screen)  
    p.draw.rect(screen, RED, (paddle[X],paddle[Y],paddle[wid],paddle[hei]))
    if ball_f:
        screen.blit(photoball,(ball[X],ball[Y]))
    if ball_s:
        screen.blit(photoball2,(ball2[X],ball2[Y]))
    screen.blit(kt[photo],(kt[X],kt[Y]))
   

    p.display.update()      