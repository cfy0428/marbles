import pygame,random,os
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



def rungame():
    pygame.init()
    p=pygame
    screen = p.display.set_mode([800,600])
    p.display.set_caption("弹球 v.1.0")
    pic = p.image.load("xiaolian2.bmp")
    puc = p.image.load("kt.bmp")
    phc = p.image.load("db.bmp")
    phc2 = p.image.load("db2.bmp")
    colorkey = pic.get_at((0,0))
    pic.set_colorkey(colorkey)
    picx = 325
    picy = 500
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    timer = p.time.Clock()
    sx = 6
    sy = -6
    pw = 105
    ph = 10
    px = 300
    py = 550
    picw = 50
    pich = 50
    points = 0
    lives = 5
    sxx=0
    syy=0
    x=1
    y=1
    kty=1
    ktx=1
    kt1=8000
    kt2=8000
    x9 = 0
    y5 = 0
    godie = True
    waiting = True
    music = False
    db = True
    keyusing = False
    ob = None
    phx = 0
    phy = 200
    phvel = 4
    phx2 = 250
    phy2 = 0
    phvel2 = 4
    tb = 0
    dr = ""
    sors = "开始"
    dsr = "鼠标模式"
    dbtext = "开启"
    font = p.font.SysFont("华文宋体", 24)
    font2 = p.font.SysFont("华文宋体", 50)
    font3 = p.font.SysFont("华文彩云", 100)
    try:
        p.mixer.init()
        popa=p.mixer.Sound("blip.wav")
        popb=p.mixer.Sound("blap.wav")
        music = True
    except:
        print("因为不知道的原因，无法加载声音。")
    def gamein():
        texti = "弹球 v.1.0"
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
        
    
    gamein()
    while True:    
        for event in p.event.get(): 
            if event.type == p.QUIT: 
                gamequit()
            if event.type == p.KEYDOWN:
                if event.key ==p.K_UP and x <=3:
                    if y%2==1:
                        if lives>0:
                            x +=0.2
                if event.key ==p.K_DOWN and x>=0.5:
                    if y%2==1:
                        if lives>0:
                            x -=0.2
                if event.key ==p.K_RETURN:
                    if db:
                        sx *= (5/3)
                        sy *= (5/3)
                        dbtext = "关闭"
                    else:
                        sx *= (3/5)
                        sy *= (3/5)
                        dbtext = "开启"
                    db = not db
                if event.key ==p.K_LEFT:
                    if y%2==1 and not waiting:
                        if lives>0:
                            keyusing = True
                            px -= 100
                if event.key ==p.K_RIGHT:
                    if y%2==1 and not waiting:
                        if lives>0:
                            keyusing = True
                            px += 100
                if event.key ==p.K_SPACE :
                    if waiting:
                        waiting = False
                        keyusing = True
                    elif lives == 0:
                        if ob:
                            tb = points
                        points=0
                        lives=5
                        picx=0
                        picy=0
                        sx=6
                        sy=6
                        x=1
                        y=1
                        phvel = 4
                        phvel2 =4
                        px = 300
                        dr = ""
                        db = True
                    else:
                        y+=1
                if event.key == p.K_ESCAPE:
                    gamequit()
                   
 
            if event.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0]:
                    if waiting:
                        waiting = False
                        keyusing = False
                    elif lives == 0:
                        if ob:
                            tb = points
                        points=0
                        lives=5
                        picx=0
                        picy=0
                        sx=6
                        sy=6
                        x=1
                        y=1
                        phvel = 4
                        phvel2 = 4
                        px = 300
                        dr = ""
                        db = True
                    elif lives>0 and waiting == False:
                        if keyusing:
                            keyusing = False
                        else:
                            y+=1
                elif p.mouse.get_pressed()[2]:
                    if db:
                        sx *= (5/3)
                        sy *= (5/3)
                        dbtext = "关闭"
                    else:
                        sx *= (3/5)
                        sy *= (3/5)
                        dbtext = "开启"
                    db = not db



        if px > 800-pw:
            px = 800-pw
        if px < 0:
            px = 0

        if kt2>6000 and lives >0 and y%2==1 and waiting == False :
            pw = 105
            godie = True
            dr = ""
            kt1 = random.randint(0,800)
            kt2 = 0
            x9=random.randint(20,30)
            y5=random.randint(-10,10)
            
        kt1 +=y5
        kt2 +=x9
        
        if kt2 + 50 >= py and kt2 + 50 <= py + ph and x9 > 0:
            if kt1 + 50 / 2 >= px and kt1 + 50 / 2 <= px + pw:
                kt2 = 700
                choose = random.randint(1,5)
                if choose == 1:
                    lives+=2
                    dr = "你增加了2条命！"
                elif choose == 2:
                    pw += 100
                    dr = "你的挡板暂时变成了2倍！"
                elif choose == 3:
                    sx /=1.5
                    sy /=1.5
                    dr = "你的球速除以了1.5！"
                elif choose == 4:
                    aaa = random.randint(1,3)
                    if aaa ==1:
                        sx=-sx
                    elif aaa ==2:
                        sy=-sy
                    else:
                        sx=-sx
                        sy=-sy
                    dr = "改变球的方向！"
                else:
                    godie = False
                    dr = "你获得了暂时的无敌！"
                    
        fps=30 * x
        
        if y%2==1 and waiting == False and lives>0:
            picx += sx
            picy += sy
            phx += phvel
            phy2 += phvel2
    
        if picx <= 0 or picx + pic.get_width() >= 800:
            sx = -sx
        if picy <= 0:
            sy = -sy 
        if picy >= 550:
            if godie:
                lives -= 1
                picx = px+pw
                sors = "继续"
                waiting = True
                if x >1.2 and x<1.9:
                    x -=0.4
                if x <2.1 and x>=1.9:
                    x -=0.6
                if x >2.1:
                    x =1.4
            if music:
                popb.play()
            if db :
                sy = -6
                sx = 6
            else:
                sy = -10
                sx = 10
            picy = 499
            if picx < 0 :
                picx = 0
            if picx > 750:
                picx = 750
        
        screen.fill(BLACK)    
        screen.blit(pic, (picx, picy))
        screen.blit(puc, (kt1, kt2))
        if not waiting:
            if not keyusing:
                px = p.mouse.get_pos()[0]
                px -= pw/2
        p.draw.rect(screen, RED, (px, py, pw, ph))
        if picy + pich >= py and picy + pich <= py + ph and sy > 0:
            if picx + picw / 2 >= px and picx + picw / 2 <= px + pw:
                points += x
                sy = -sy*1.1
                sx = sx*1.1
                if music:
                    popa.play()
        if db == True :
            if sy > 0 :
                if picy <= phy and picy + pich > phy:
                    if picx + picw / 2 >= phx and picx + picw / 2 <= phx + 300:
                        sy = -sy
                        sx = sx
                if sx > 0 :
                    if picx <= phx2 and picx +picw >= phx2:
                        if picy + pich / 2 >= phy2 and picy + pich / 2 <= phy2 +250:
                            sy = sy
                            sx = -sx
                else:
                    if picx >=phx2 and picx < phx2 + 30:
                        if picy + pich / 2 >= phy2 and picy + pich / 2 <= phy2 +250:
                            sy = sy
                            sx = -sx
            else:
                if picy >= phy  and picy < phy + 30:
                    if picx + picw / 2 >= phx and picx + picw / 2 <= phx + 250:
                        sy = -sy
                        sx = sx
                
                if sx > 0 :
                    if picx <= phx2 and picx + picw>= phx2:
                        if picy + pich / 2 >= phy2 and picy + pich / 2 <= phy2 +30:
                            sy = sy
                            sx = -sx
                else:
                    if picx >=phx2 and picx < phx2 + 30:
                        if picy + pich / 2 >= phy2 and picy + pich / 2 <= phy2 +250:
                            sy = sy
                            sx = -sx
        
        if phx >=500 or phx <0:
            phvel = -phvel*random.randint(90,110)/100
        if phy2 >=350 or phy2 <0:
            phvel2 = -phvel2*random.randint(90,110)/100
        
        if lives < 1:
            points = round(points,1)
            bp = points-tb
            if bp > 0:
                dr = "恭喜你创造了纪录，超过最高记录："+str(round(abs(bp),1))+"分!"
                ob = True
            else:
                dr = "你离最高纪录："+str(tb)+"还差"+str(abs(bp))+"分，加油!"
                ob = False
        
                
        if not waiting:          
            ds = "生命数: " + str(lives) + " 分数: " + str(round(points,1))
            ds +=" 倍速："+str(round(x,1))
            ds +=" 速度："+str(round(abs(sx)*fps*(2**0.5),1))

        if waiting:
            ds = "等待状态中，按下鼠标左键或空格"+sors+"游戏。"

        if keyusing:
            dsr = " 键盘模式"
        else: dsr = " 鼠标模式"

        ds +=dsr
        ds +=" 挡板"
        ds +=dbtext
                       
        if lives <1:
            sx=sy=0
            ds="游戏结束。你的分数是："+str(points)
            ds+="。请按鼠标左键或空格键重新开始。"
            waiting = False
        if y%2==0:
            ds="已暂停，按鼠标左键或空格继续。"
        
        textprint(ds,"ds2",font,WHITE,10,screen)
        textprint(dr,"dr2",font,WHITE,550,screen)
        if db == True:
            screen.blit(phc, (phx, phy))
            screen.blit(phc2, (phx2, phy2))
        p.display.update()
        timer.tick(fps)


rungame()
