"""
Ferramenta (não faz parte do jogo): organiza o pacote "Zombie Apocalypse Tileset"
de Ittai Manero nas pastas e nomes que o main.py usa.

Uso, a partir da pasta do projeto:
    python ferramentas/organizar_assets.py

Antes, baixe o pacote em https://ittaimanero.itch.io/zombie-apocalypse-tileset
e extraia o zip dentro da pasta assets/, ficando assim:
    assets/Zombie Apocalypse Tileset/Organized separated sprites/...
"""
import os, shutil, sys
import pygame

ORIGEM = os.path.join("assets", "Zombie Apocalypse Tileset", "Organized separated sprites")
DESTINO = os.path.join("assets", "sprites")

# "pasta de destino/prefixo do arquivo": "pasta original do pacote"
MAPA = {
    "jogador/andar": "Player Character Walking Animation Frames",
    "jogador/dano": "Damaged Player Animation Frames",
    "zumbis/magro/andar": "Skinny Walking Zombie Animation",
    "zumbis/magro/dano": "Damaged Skinny Zombie Animation Frames",
    "zumbis/crianca/andar": "Kid Zombie Animation Frames",
    "zumbis/crianca/dano": "Damaged Kid Zombie Animation Frames",
    "zumbis/grande/andar": "Big Zombie Walking Animation Frames",
    "zumbis/grande/dano": "Damaged Big Zombie Animation Frames",
    "zumbis/atirador/andar": "Turret Zombie Animation Frames",
    "zumbis/atirador/dano": "Damaged Turret Zombie Animation Frames",
    "zumbis/atirador/vomito": "Turret Zombie Vomit Shooting Animation Frames_",
    "tiles/terra": "Terrain Variations",
    "tiles/flores": "Grass with Flowers",
    "tiles/muro": "Terrain wall",
    "tiles/caminho": "Modular Terrain Path",
    "tiles/estrada": "Modular Road",
    "tiles/agua": "Water animation frames",
    "tiles/arbusto": "Modular Bushes",
    "tiles/arvore": "Trees",
    "tiles/cerca": "Modular Fences",
    "tiles/predio_pequeno": "Modular Small Building",
    "objetos/carro_quebrado": "Broken Cars and Tires",
    "objetos/urbano": "Urban Assets",
    "objetos/barril": "Exploding Barrel Animation Frames",
    "objetos/caixa": "Spawning Item Box Animation Frames + Broken Box Pieces",
    "objetos/lapide": "Tombstone",
    "objetos/cadaver": "Dead Corpses With Flies Animation Frames",
    "itens/item": "Pickable Items and Weapons",
    "itens/dinheiro": "Spawning Money Animation Frames",
    "efeitos/sangue": "Blood Animation Frames",
    "efeitos/mancha_sangue": "Random Blood Stains",
    "efeitos/explosao": "Explosion Animation Frames",
    "efeitos/fumaca": "Smoke Animation Frames",
    "efeitos/faca": "Knife Attack Animation Frames",
    "efeitos/tiro_pistola": "Pistol Shooting Animation Frames",
    "efeitos/tiro_espingarda": "Shotgun Shooting Animation Frames",
    "ui/ui": "UI Elements",
    "ui/inventario": "Inventory interface",
}


def copiar_pacote():
    total = 0
    for novo, pasta in MAPA.items():
        origem = os.path.join(ORIGEM, pasta)
        arquivos = sorted(f for f in os.listdir(origem) if f.endswith(".png"))
        pasta_dest, prefixo = os.path.split(novo)
        os.makedirs(os.path.join(DESTINO, pasta_dest), exist_ok=True)
        for i, f in enumerate(arquivos):
            shutil.copy2(os.path.join(origem, f), os.path.join(DESTINO, pasta_dest, f"{prefixo}_{i}.png"))
            total += 1
    return total


def gerar_frames_direita():
    # O pacote só tem o personagem virado para a direita (frames 3-5).
    # Os frames 9-11 são esses mesmos espelhados, para andar para a esquerda.
    pasta = os.path.join(DESTINO, "jogador")
    for i in range(3):
        img = pygame.image.load(os.path.join(pasta, f"andar_{3 + i}.png"))
        pygame.image.save(pygame.transform.flip(img, True, False), os.path.join(pasta, f"andar_{9 + i}.png"))
    return 3


if not os.path.isdir(ORIGEM):
    print("Pacote não encontrado em:", ORIGEM)
    print("Baixe em https://ittaimanero.itch.io/zombie-apocalypse-tileset e extraia dentro de assets/")
    sys.exit(1)

copiados = copiar_pacote()
gerados = gerar_frames_direita()
print(f"{copiados} sprites copiados e {gerados} frames gerados em {DESTINO}")
