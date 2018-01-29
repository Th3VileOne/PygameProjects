import pygame,random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImg
        #self.image.fill(green)
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius = 15
        #pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.centerx = displayw/2
        self.rect.bottom = displayh * 0.90
        self.speedx = 0
        self.hp = 100
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > displayw - 5:
            self.rect.right = displayw - 5
        if self.rect.left < 5:
            self.rect.left = 5
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        pewOgg.play()
class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob1Img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.radius = 20
        #pygame.draw.circle(self.image, red, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, displayw - self.rect.width)
        self.rect.y = random.randrange(-150, -40) #random spawnpoint above screen
        self.maxSpeed = 8
        self.minSpeed = 1
        self.speedy = random.randrange(self.minSpeed, self.maxSpeed)  # customizeable speed
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > displayh + 10:
            self.rect.x = random.randrange(0, displayw - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)  # customizeable speed
class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob2Img
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.radius = 230 #config this later
        self.offscreenCoord = self.radius - 50
        self.speedy = 3  # customizeable speed
        self.rect.x = random.choice([random.randint(0-self.offscreenCoord, 0 + self.radius),random.randint(displayw - self.radius,displayw + self.offscreenCoord)])
        self.rect.y = self.speedy * fps * 18 #the number in this line is the number of seconds per spawn
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > displayh + 10:
            self.speedy = 3  # customizeable speed
            self.rect.x = random.choice([random.randint(0 - self.offscreenCoord, 0 + self.radius),
                                         random.randint(displayw - self.radius, displayw + self.offscreenCoord)])
            self.rect.y = self.speedy * fps * 18  # the number in this line is the number of seconds per spawn
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bulletImg
        self.image.set_colorkey(black)
        #self.image.fill((204, 204, 0))  # yellow
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
class hpPlus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mntdewImg
        self.rect = self.image.get_rect()
        self.image.set_colorkey(black)
        self.radius = 20
        self.rect.x = random.randrange(0,displayw - self.rect.width)
        self.rect.y = -1500
        self.speedy = 5
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > 500 + 10:
            self.rect.x = random.randrange(0, displayw - self.rect.width)
            self.rect.y = -1500
            self.speedy = 5

displayw = 800
displayh = 500
fps = 60
highscore = 0
title = "???-???-???-???-???"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#score color codes
wood =(130, 82, 1)
stone=(139,141,122)
iron = (230, 227, 226)
gold =(255,215,0)
sapphire =(6,32,73)

mlgPlayed = False
ddlcPlayed = False

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((displayw,displayh))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

#graphics
bgImg = pygame.image.load("assets/space.jpg").convert()
bgImg_rect = bgImg.get_rect()
playerImg = pygame.image.load("assets/spaceship.png").convert()
mob1Img = pygame.image.load("assets/rock.png").convert()
mob2Img = pygame.image.load("assets/tem.png").convert()
bulletImg = pygame.image.load("assets/bullet1.png").convert()
mntdewImg = pygame.image.load("assets/mntdew.jpg").convert()

#sounnds
pewOgg = pygame.mixer.Sound("assets/pew.wav")
wowOgg = pygame.mixer.Sound("assets/wow.ogg")
rektWav = pygame.mixer.Sound("assets/rekt.wav")
rektWav.set_volume(5) #adjust volue, 1 is normal
plus50 = pygame.mixer.Sound("assets/plus50.ogg")
bgMusic = pygame.mixer.Sound("assets/space.wav")
spMusic = pygame.mixer.Sound("assets/bgmusic.ogg")

fontname = pygame.font.match_font('arial')

def draw_text(canvas, text,size,x,y,color):
    font = pygame.font.Font(fontname, size)
    textsurf = font.render(text,True,color)
    textrect = textsurf.get_rect()
    textrect.midtop = (x,y)
    canvas.blit(textsurf,textrect)
def newmob():
    m = Mob1()
    all_sprites.add(m)
    mobs.add(m)
def moreHp():
    h = hpPlus()
    all_sprites.add(h)
    mntdew.add(h)
def drawHpBar(canvas,x,y,pct):
    if pct < 0:
        pct = 0
    length = 100
    height = 10
    fill = (pct/100) * length
    olrect = pygame.Rect(x,y,length,height)
    fill_rect = pygame.Rect(x,y,fill,height)
    pygame.draw.rect(canvas, red, fill_rect)
    pygame.draw.rect(canvas, white, olrect, 2)
def goscreen():
    screen.blit(bgImg, (0, 0))
    draw_text(screen, title, 69, displayw/2, displayh/4,white)
    draw_text(screen, "Arrow keys to move, Spacebar to shoot", 30, displayw/2, displayh/2,white)
    draw_text(screen, "Presss any key to begin !!!", 25,displayw/2, displayh*3/4,white)
    draw_text(screen, "Current Highscore: " + str(highscore), 36, displayw/2, (displayh*3/4)+30, green)
    pygame.display.flip()
    wait = True

    while wait:
        clock.tick(fps)
        pygame.time.delay(3 * 1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                player.hp = 100
                wait = False
def pausescreen():
    draw_text(screen, "PAUSED", 50, displayw/2, displayh/2, red)
    pygame.display.flip()
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    wait = False

#stuff to call when restarting game
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()
mobs2 = pygame.sprite.Group()
score = 0
bullets = pygame.sprite.Group()
mntdew = pygame.sprite.Group()
for i in range(8):
    newmob()
for i in range(1):
    moreHp()
#end of stuff to call when restarting game
bgMusic.play(loops = -1)

game_over = True
running = True
while running:
    if game_over:
        goscreen() #special
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        score = 0
        for i in range(8):
            newmob()
        for i in range(1):
            moreHp()
    clock.tick(fps)
    #list of events that can occur, can be detected, and what to do
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_p:
                pausescreen()

    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True) #mobs hitting bullets
    for hit in hits:
        wowOgg.play()
        score += 1
        newmob()
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle) #player hitting mobs
    for hit in hits:
        player.hp -= 10
        rektWav.play()
        if score == 0:
            score = 0
        else:
            score -=1
        newmob()
        #running = False
        if player.hp <= 0:
            if score > highscore:
                highscore = score
            score = 0
            if ddlcPlayed == True:
                spMusic.stop()
                ddlcPlayed = False

            goscreen()
    hits = pygame.sprite.spritecollide(player, mntdew, True, pygame.sprite.collide_circle) #player hitting mntdew
    for hit in hits:
        if player.hp == 100:
            player.hp = 100
        else:
            player.hp += 5
        if score <= 0:
            score = 0
        else:
            score -= 2
        moreHp()

    screen.fill(black)
    screen.blit(bgImg,(0,0))
    all_sprites.draw(screen)
    drawHpBar(screen, 5, 5, player.hp)

    if score >= 100:
        draw_text(screen, str(score), 40, displayw/2, 10, sapphire)
        bgMusic.stop()
        if ddlcPlayed == False:
            spMusic.play(-1)
            ddlcPlayed = True
    elif score >= 50:
        draw_text(screen, str(score), 40, displayw/2, 10, gold)
        bgMusic.stop()
        # spMusic.play(-1)
        if mlgPlayed == False:
            plus50.play()
            mlgPlayed = True
    elif score >= 25:draw_text(screen, str(score), 40, displayw/2, 10, iron)
    elif score >= 11:draw_text(screen, str(score), 40, displayw/2, 10, stone)
    else:            draw_text(screen,str(score),40, displayw/2, 10,wood)
    pygame.display.flip()
