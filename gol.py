import numpy as np
import mathlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import argparse

def makeGrid(cols,rows,theme):
    world = np.zeros((cols,rows))

    if theme == 1:
        for i in range(0,cols):
            for j in range(0,rows):
                world[i,j] = random.randint(0,1)

    elif theme == 2:
        beacon = [[1, 1, 0, 0],
                  [1, 1, 0, 0],
                  [0, 0, 1, 1],
                  [0, 0, 1, 1]]
                  
        world[1:5, 1:5] = beacon

    elif theme == 3:  
        glider = [[0, 1, 0, 0],
                  [0, 0, 1, 0],
                  [1, 1, 1, 0],
                  [0, 0, 0, 0]]

        world[1:5, 1:5] = glider

    return(world)

def neighbours(i, j, world):
    neighbours = 0
    neighbours = np.sum(world[i - 1:i + 2, j - 1:j + 2])
    neighbours -= world[i,j]

    if world[i, j] == 1:
        if neighbours < 2 or neighbours > 3:
            return 0

    elif world[i, j] == 0:
        if neighbours == 3:
            return 1
    return world[i,j]

def gen(world):
    new_world = np.copy(world)

    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            new_world[i, j] = neighbours(i, j, world)
    return new_world


def animate(world):
    fig = plt.figure()
    plt.axis('on')
    ims = []
    i = 0
    rotation = 100

    for n in range(rotation):
        ims.append((plt.imshow(world, cmap='binary'),))
        world = gen(world)
        i+=1
        print(i,'/',rotation)
    im_ani = animation.ArtistAnimation(fig, ims, interval=100,
    repeat_delay=10000, blit=True)
    plt.show()


if __name__ == '__main__':
    cols = 40
    rows = 40
    theme = 1

    #parses
    #parser = argparse.ArgumentParser(description="Conway's Game of Life")
    #parser.add_argument('--grid-size cols', dest='cols', required=False)
    #parser.add_argument('--grid-size rows', dest='rows', required=False)

    world = makeGrid(cols,rows,theme)
    animate(world)
