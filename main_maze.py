# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

s = deque()

maze_csv_path = "labirinto1.txt"  # Substitua pelo caminho correto
maze = Maze() 

maze.load_from_csv(maze_csv_path)

# Exibir o lab
maze.run()
maze.init_player()

p = maze.get_init_pos_player()

maze.mov_player(p)

visited = set()
s.append(p)

found = False

while s:
    current_pos = s.pop()

    if current_pos in visited:
        continue
    visited.add(current_pos)

    if maze.find_prize(current_pos):
        maze.mov_player(current_pos)
        print("Prêmio encontrado em:", current_pos)
        found = True
        break

    maze.mov_player(current_pos)
    time.sleep(0.05)

    # Explorar vizinhos
    x, y = current_pos
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for nx, ny in neighbors:
        if (0 <= nx < maze.M.shape[0]) and (0 <= ny < maze.M.shape[1]):
            if maze.is_free((nx, ny)) and (nx, ny) not in visited:
                s.append((nx, ny))

if not found:
    print("Prêmio não encontrado.")
