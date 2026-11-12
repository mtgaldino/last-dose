import pygame, sys
from pygame.locals import QUIT, KEYDOWN

pygame.init()
clock = pygame.time.Clock()

escala = 3                  
tile_size = 16 * escala     
velocidade = 0.15

mapa = []
arquivo = open("mapa.txt", "r")
for linha in arquivo:
    if linha[-1] == "\n":
        linha = linha[:-1]
    if len(linha) > 0:
        mapa.append(linha)
arquivo.close()

screen = pygame.display.set_mode((len(mapa[0]) * tile_size, len(mapa) * tile_size))
pygame.display.set_caption("Last Dose")


def carrega_imagem(caminho):
    imagem = pygame.image.load(caminho)
    imagem = pygame.transform.scale(imagem, (imagem.get_width() * escala, imagem.get_height() * escala))
    return imagem


def eh_solido(letra):
    return letra == "M" or letra == "C" or letra == "A" or letra == "T" or letra == "W"


def colide_com_mapa(collider):
    for i in range(len(colliders_mapa)):
        if collider.colliderect(colliders_mapa[i]):
            return True
    return False


terra = carrega_imagem("assets/sprites/tiles/terra_0.png")
terra_seca = carrega_imagem("assets/sprites/tiles/terra_2.png")
flores = carrega_imagem("assets/sprites/tiles/flores_0.png")
caminho_h = carrega_imagem("assets/sprites/tiles/caminho_2.png")
caminho_v = carrega_imagem("assets/sprites/tiles/caminho_3.png")
caminho_cruz = carrega_imagem("assets/sprites/tiles/caminho_1.png")
muro = carrega_imagem("assets/sprites/tiles/muro_0.png")
cerca = carrega_imagem("assets/sprites/tiles/cerca_9.png")
arbusto = carrega_imagem("assets/sprites/tiles/arbusto_1.png")
arvore = carrega_imagem("assets/sprites/tiles/arvore_0.png")

agua_list = []
for i in range(3):
    agua_list.append(carrega_imagem(f"assets/sprites/tiles/agua_{i}.png"))

jogador_list = []
for i in range(12):
    jogador_list.append(carrega_imagem(f"assets/sprites/jogador/andar_{i}.png"))
passos = [0, 1, 0, 2]       


colliders_mapa = []
pos_x = 0
pos_y = 0
for i in range(len(mapa)):              
    for j in range(len(mapa[i])):       
        if eh_solido(mapa[i][j]):
            colliders_mapa.append(pygame.Rect(j * tile_size, i * tile_size, tile_size, tile_size))
        elif mapa[i][j] == "J":
            pos_x = j * tile_size + 9
            pos_y = i * tile_size + 29


larg_collider = 30
alt_collider = 18

primeiro_frame = 0          
curr_frame = 0
anim_time = 0
curr_frame_agua = 0
anim_time_agua = 0
mostrar_colliders = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_F1:
                if mostrar_colliders:
                    mostrar_colliders = False
                else:
                    mostrar_colliders = True

    clock.tick(60)
    dt = clock.get_time()

    
    keys = pygame.key.get_pressed()
    andando = False

    old_pos_x = pos_x
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        pos_x = pos_x - velocidade * dt
        primeiro_frame = 3
        andando = True
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        pos_x = pos_x + velocidade * dt
        primeiro_frame = 9
        andando = True
    if colide_com_mapa(pygame.Rect(pos_x, pos_y, larg_collider, alt_collider)):
        pos_x = old_pos_x

    old_pos_y = pos_y
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        pos_y = pos_y - velocidade * dt
        primeiro_frame = 6
        andando = True
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        pos_y = pos_y + velocidade * dt
        primeiro_frame = 0
        andando = True
    if colide_com_mapa(pygame.Rect(pos_x, pos_y, larg_collider, alt_collider)):
        pos_y = old_pos_y

    if andando:
        anim_time = anim_time + dt
        if anim_time / 1000 > 0.15:
            curr_frame = curr_frame + 1
            if curr_frame > len(passos) - 1:
                curr_frame = 0
            anim_time = 0
    else:
        curr_frame = 0

    anim_time_agua = anim_time_agua + dt
    if anim_time_agua / 1000 > 0.3:
        curr_frame_agua = curr_frame_agua + 1
        if curr_frame_agua > len(agua_list) - 1:
            curr_frame_agua = 0
        anim_time_agua = 0

    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            x = j * tile_size
            y = i * tile_size
            screen.blit(terra, (x, y))      # chão embaixo de tudo
            if mapa[i][j] == ",":
                screen.blit(terra_seca, (x, y))
            elif mapa[i][j] == "F":
                screen.blit(flores, (x, y))
            elif mapa[i][j] == "H":
                screen.blit(caminho_h, (x, y))
            elif mapa[i][j] == "V":
                screen.blit(caminho_v, (x, y))
            elif mapa[i][j] == "+":
                screen.blit(caminho_cruz, (x, y))
            elif mapa[i][j] == "M":
                screen.blit(muro, (x, y))
            elif mapa[i][j] == "C":
                screen.blit(cerca, (x, y))
            elif mapa[i][j] == "A":
                screen.blit(arbusto, (x, y))
            elif mapa[i][j] == "T":
                screen.blit(arvore, (x, y))
            elif mapa[i][j] == "W":
                screen.blit(agua_list[curr_frame_agua], (x, y))

    sprite = jogador_list[primeiro_frame + passos[curr_frame]]
    sprite_x = pos_x + larg_collider // 2 - sprite.get_width() // 2
    sprite_y = pos_y + alt_collider - sprite.get_height()
    screen.blit(sprite, (sprite_x, sprite_y))

    if mostrar_colliders:
        for i in range(len(colliders_mapa)):
            pygame.draw.rect(screen, (0, 0, 255), colliders_mapa[i], 2)
        pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, larg_collider, alt_collider), 2)

    pygame.display.update()
