import pygame
from sys import exit
from random import randint, choice
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("TEPT Hunter")

##
## Importa os arquivos necessários
##

# Carrega o plano de fundo
plano_fundo = pygame.image.load('background/background1.png').convert_alpha()
nuvens = pygame.image.load('background/background2.png').convert_alpha()
montanha = pygame.image.load('background/background3.png').convert_alpha()
linha_azul = pygame.image.load('background/background4.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
nuvens = pygame.transform.scale(nuvens, tamanho)
montanha = pygame.transform.scale(montanha, tamanho)
linha_azul = pygame.transform.scale(linha_azul, tamanho)

## Personagem
jogador_index = 0

# Carrega as imagens do personagem parado
personagem_parado_surfaces = []
for imagem in range(1, 9):
    img = pygame.image.load(f'personagem/parado/parado{imagem}.png').convert_alpha()
    personagem_parado_surfaces.append(img)

# Carrega as imagens do personagem correndo
personagem_correndo_surfaces = []
for imagem in range(1, 9):
    img = pygame.image.load(f'personagem/correndo/correndo{imagem}.png').convert_alpha()
    personagem_correndo_surfaces.append(img)

# Carrega as imagens do personagem pulando
personagem_pulando_surfaces = []
for imagem in range(1, 9):
    img = pygame.image.load(f'personagem/pulando/pulando{imagem}.png').convert_alpha()
    personagem_pulando_surfaces.append(img)

# Carrega as imagens do personagem ataque
personagem_ataque_surfaces = []
for imagem in range(1, 5):
    img = pygame.image.load(f'personagem/ataque/ataque{imagem}.png').convert_alpha()
    personagem_ataque_surfaces.append(img)

# Carrega as imagens do personagem morto
personagem_morto_surfaces = []
for imagem in range(1, 4):
    img = pygame.image.load(f'personagem/morto/morto{imagem}.png').convert_alpha()
    personagem_morto_surfaces.append(img)

jogador_surfaces_retangulo = personagem_parado_surfaces[jogador_index].get_rect(center = (100, 430))

## Bicho
bicho_index = 0

# Carrega as imagens do bicho
bicho_surfaces = []
for imagem in range(1, 10):
    img = pygame.image.load(f'bicho/lobo{imagem}.png').convert_alpha()
    bicho_surfaces.append(img)

bicho_surfaces_retangulo = bicho_surfaces[bicho_index].get_rect(center = (100, 430))

# Cria um relógico para controlar os FPS
relogio = pygame.time.Clock()

# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0
movimento_bicho = 0
vida = 3
caça = 0

#Loop principal do jogo
while True:
    ## EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_d:
                movimento_personagem = 5
                direcao_personagem = 1

            if evento.key == pygame.K_a:
                movimento_personagem = -5
                direcao_personagem = 0

            if evento.key == pygame.K_DOWN:
                movimento_personagem = 0
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

    # Desenha o fundo na tela
    tela.blit(plano_fundo, (0,0))
    tela.blit(nuvens, (0,0))
    tela.blit(montanha, (0,0))
    tela.blit(linha_azul, (0,0))

    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)
