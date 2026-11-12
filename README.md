# Last Dose

> Um vírus transformou a cidade em uma horda de zumbis. Você é o último que pode criar a cura.
> Explore o mapa, colete os ingredientes da vacina e sobreviva até preparar a **última dose**.

Roguelike 2D com visão de cima (top-down), feito em **Python + pygame** como projeto final da disciplina **INF1034** (PUC-Rio, 2026.2).

<!-- Coloque aqui um GIF do jogo: ![Gameplay](docs/gameplay.gif) -->

## Controles

| Tecla | Ação |
|---|---|
| Setas ou W A S D | Mover o personagem |
| F1 | Mostrar/esconder as caixas de colisão |

## Como o mapa funciona

O cenário é uma matriz de letras lida do [`mapa.txt`](mapa.txt). Cada letra vira um tile de 16×16 px, desenhado 3× maior na tela:

| Letra | Tile | Bloqueia? |
|---|---|---|
| `.` `,` | Chão | |
| `F` | Flores | |
| `H` `V` `+` | Trilha (horizontal, vertical, cruzamento) | |
| `M` | Muro | ✔ |
| `C` | Cerca | ✔ |
| `A` | Arbusto | ✔ |
| `T` | Árvore | ✔ |
| `W` | Água (animada) | ✔ |
| `J` | Posição inicial do jogador | |

## Créditos

- Gráficos: **[Zombie Apocalypse Tileset](https://ittaimanero.itch.io/zombie-apocalypse-tileset)**, de **Ittai Manero**.
- Código: Matheus Galdino --> https://github.com/mtgaldino
