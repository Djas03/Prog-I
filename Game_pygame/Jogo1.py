import random, time, pygame, os
from pygame.locals import *
from pygame import mixer
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.font.init()
pygame.display.set_caption('INTO DA ROCK')
icon = pygame.image.load('therock.png')
pygame.display.set_icon(icon)
#---------------------FPS---------------------
pos = 0
framerate = 60
last_time = time.time()
#---------------------FPS---------------------

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (26, 235, 235)
pink = (222, 4, 204)
roxo = (158, 3, 152)

score = 0
cont = 0
guarda = 0

#---------------------FONTE---------------------
fonte = pygame.font.SysFont("bahnschrift", 35)
fonte2 = pygame.font.SysFont("bahnschrift", 100)






def texto (msg,cor):
    texto1 = fonte.render (msg,True,cor)
    screen.blit(texto1,[750, 690])


def Your_score(score):
    value = fonte.render("Pontuação: " + str(score)+"!!!", True, blue)
    screen.blit(value, [random.randint(28, 30), random.randint(148, 150)])
    Your_score.speed = (3)

def METROS(score):
    value = fonte.render("Metros: " + str(score)+"m", True, pink)
    screen.blit(value, [random.randint(28, 30), random.randint(98, 100)])
    METROS.speed = (3)

#---------------------TELA FINAL---------------------
def Your_scoreFINAL(score):
    value = fonte2.render("Total de: " + str(score)+" pontos!", True, blue)
    screen.blit(value, [random.randint(98, 102), random.randint(192, 196)])
    Your_score.speed = (3)

def METROSfinal(score):
    value = fonte2.render("Máximo de: " + str(score)+"m!", True, roxo)
    screen.blit(value, [random.randint(98, 102), random.randint(98, 102)])
    METROS.speed = (3)
#---------------------FONTE---------------------


#---------------------Player---------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((650, 2))
        self.surf.fill((255, 0, 0))
        
        self.rect = self.surf.get_rect(
        center=(683,760)
        )


#---------------------BALA---------------------
class SERRA(pygame.sprite.Sprite):
    def __init__(self):
        super(SERRA, self).__init__()
        self.surf = pygame.Surface((70, 100))
        self.surf.fill((255, 0, 0))

        self.rect = self.surf.get_rect(
        center=(683,868)
        )
    def update(self, KEYDOWN):
        K_SPACE == True

        if KEYDOWN[K_SPACE]:

            self.rect.top = 568
            som_serraON.play()
        else:
            self.rect.top = 868
            som_serraON.stop()


#---------------------Enemy---------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((60, 45)) #Definição do retangulo
        self.surf.fill(blue) #Preenche com cor branca (RGB)
        self.rect = self.surf.get_rect( #Coloca na extrema direita (entre 820 e 900) e
                                        #sorteia sua posição em relacao à coordenada y
                                        #(entre 0 e 600)
            center=(random.randint(0, 1366), 100)
        )
        self.speed = random.uniform(2, 3)
            
        
        if int(pos/50) > 20:
            self.speed = random.uniform(2, 4)
        if int(pos/50) > 50:
            self.speed = random.uniform(4, 5)
        if int(pos/50) > 100:
            self.speed = random.uniform(6, 9)

    def update(self, pressed_keys):
        self.rect.move_ip(0, +self.speed)
        if self.rect.right < 0:
            self.kill()

        if pressed_keys[K_e]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_q]:
            self.rect.move_ip(2, 0)
        # Mantém o jogador nos limites da tela do jogo
    

# Inicializa pygame
pygame.init()
screen = pygame.display.set_mode((1366, 768))
#---------------------IMAGEM---------------------
fundo = pygame.image.load('fundo.png')
bg = pygame.image.load('therock.png')

#---------------------MUSICA---------------------
som_fundo = pygame.mixer.Sound('mscFUNDO.wav')
som_fundo.play()
som_colisao = pygame.mixer.Sound('crush.wav')
som_serraON = pygame.mixer.Sound('serraON.wav')
som_serraCON= pygame.mixer.Sound('serraCON.wav')
som_morte = pygame.mixer.Sound('morte.wav')

#---------------------VOLUME---------------------
som_fundo.set_volume(0.7)
som_serraON.set_volume(0.2)
som_serraCON.set_volume(0.5)
som_colisao.set_volume(0.2)

player = Player()
TIRO = SERRA()
background = pygame.Surface(screen.get_size())

# Cria um evento para adição de inimigos
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 2300) #Define um intervelao para a criação de cada
                                     #inimigo (milisegundos)
# Cria o jogador (nosso retangulo)


background.blit(fundo, (0,0))
enemies = pygame.sprite.Group() #Cria o grupo de inimigos
all_sprites = pygame.sprite.Group() #Cria o grupo de todos os Sprites
all_sprites.add(player)
all_sprites.add(TIRO)

Gameover = False
running = True #Flag para controle do jogo


#---------------------LOOP---------------------
while running:
    while Gameover:
        screen.fill((91, 7, 133))
        lose = pygame.image.load('lose.png')
        screen.blit(lose,(0,0))
        som_fundo.set_volume(0.3)
        texto("Game Over pressione Esc para sair", (white))
        METROSfinal(int(pos/50))
        Your_scoreFINAL(int(score)+ int((pos/25)))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
            

        
                if event.key == K_ESCAPE: #Verifica se a tecla ESC foi pressionada
                    running = False
                    Gameover = False
                    
                    
#---------------------FRAMERATE E SEC---------------------
    dt = time.time() - last_time
    dt *= 20
    last_time = time.time()
    pos += 3 * dt
#---------------------FRAMERATE E SEC---------------------

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            

            if event.key == K_SPACE:
                TIRO.image = pygame.image.load('serraON.png')
                TIRO.surf = TIRO.image
    
            if event.key == K_ESCAPE: #Verifica se a tecla ESC foi pressionada
                running = False
        elif event.type == QUIT: #Verifica se a janela foi fechada
            running = False
        elif(event.type == ADDENEMY): #Verifica se é o evento de criar um inimigo
            new_enemy = Enemy() #Cria um novo inimigo
            new_enemy.image = pygame.image.load('zz.png')
            new_enemy.surf = new_enemy.image
            enemies.add(new_enemy) #Adiciona o inimigo no grupo de inimigos
            all_sprites.add(new_enemy) #Adiciona o inimigo no grupo de todos os
                                        #Sprites

  

    screen.blit(background, (0, 0)) #Atualiza a exibição do plano de fundo do jogo
                                    #(neste caso não surte efeito)
    pressed_keys = pygame.key.get_pressed() #Captura as teclas pressionadas
    enemies.update(pressed_keys)
    TIRO.update(pressed_keys) 
    
     #Atualiza a posição do player conforme teclas usadas
    #enemies.update() #Atualiza posição dos inimigos

    

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect) #Atualiza a exibição de todos os Sprites
    
    if pygame.sprite.spritecollide(TIRO, enemies, True):
        if TIRO:
            score+=10
            som_serraON.stop()
            som_serraCON.play()
            som_colisao.play()  
            TIRO.image = pygame.image.load('serraBLOOD.png')
            TIRO.surf = TIRO.image
            

    if pygame.sprite.spritecollideany(player, enemies):
        som_morte.play()
        screen.fill((91, 7, 133))
        Gameover = True
        pass
        
    Your_score(int(score)+ int((pos/25)))
    METROS(int(pos/50))

    pygame.display.flip() #Atualiza a projeção do jogo