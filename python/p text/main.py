import pygame
import sys

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player.png")
        self.inventory = []

class TileMap:
    def __init__(self, filename):
        self.tiles = []
        with open(filename, "r") as f:
            for line in f:
                self.tiles.append(list(line.strip()))

    def draw(self, surface):
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                tile = self.tiles[y][x]
                if tile != "0":
                    surface.blit(pygame.image.load(f"{tile}.png"), (x * 32, y * 32))

class Object:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        self.tile_map = TileMap("tilemap.txt")
        self.player = Player(100, 100)
        self.objects = []

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.y -= 32
                    if event.key == pygame.K_DOWN:
                        self.player.y += 32
                    if event.key == pygame.K_LEFT:
                        self.player.x -= 32
                    if event.key == pygame.K_RIGHT:
                        self.player.x += 32

                    if event.key == pygame.K_SPACE:
                        # Interact with the object in front of the player
                        for object in self.objects:
                            if object.x == self.player.x and object.y == self.player.y:
                                object.interact(self.player)

            self.screen.fill((0, 0, 0))

            self.tile_map.draw(self.screen)

            for object in self.objects:
                self.screen.blit(object.image, (object.x, object.y))

            self.screen.blit(self.player.image, (self.player.x, self.player.y))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
