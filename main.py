import pygame
from sys import exit
class Game:
    def __init__(self):
        self.width = 800
        self.height = 400
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('YES OR NO!')
        self.clock = pygame.time.Clock()
        self.test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        self.sky_surface = pygame.image.load('graphics/Sky.png').convert()
        self.ground_surface = pygame.image.load('graphics/ground.png').convert()

        self.score_surface = self.test_font.render('My Game', False, (64,64,64))
        self.score_rect = self.score_surface.get_rect(center = (400, 50))

        self.snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
        self.snail_rect = self.snail_surface.get_rect(bottomright = (600, 300))

        self.player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.player_rect = self.player_surface.get_rect(midbottom = (80, 300))
        self.player_gravity = 0

        self.game_active = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if self.game_active:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.player_rect.collidepoint(event.pos):
                            print('collision')
                            self.player_gravity = -20
                    
                    if event.type == pygame.KEYDOWN and self.player_rect.bottom >= 300:
                        if event.key == pygame.K_SPACE:
                            self.player_gravity = -20     
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.game_active = True 
                        self.snail_rect.left = 800

            if self.game_active:
                self.screen.fill('black')
                self.screen.blit(self.sky_surface, (0, 0))
                self.screen.blit(self.ground_surface, (0, 300))
                pygame.draw.rect(self.screen, '#c0e8eC', self.score_rect)
                pygame.draw.rect(self.screen, '#c0e8eC', self.score_rect, 10)
                self.screen.blit(self.score_surface, self.score_rect)
        

                self.snail_rect.x -= 4
                if self.snail_rect.right <= 0: self.snail_rect.left = 800
                self.screen.blit(self.snail_surface, self.snail_rect)

                #PLAYER
                self.player_gravity += 1
                self.player_rect.y += self.player_gravity
                if self.player_rect.bottom >= 300:
                    self.player_rect.bottom = 300
                self.screen.blit(self.player_surface, self.player_rect)
            
                if self.snail_rect.colliderect(self.player_rect):
                    self.game_active = False
            else:

                self.screen.fill('Yellow')

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()