import pygame
from pygame.locals import *
from cursor import Cursor
from settings import IMAGES_DIR, DIRECTIONS, FONT, FONT_SIZE

class Menu(object):
    """docstring for Menu"""
    def __init__(self, screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.buffer = pygame.Surface(self.screen.get_size())
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.menu_items = ['Items','Equip','Magic','Status','Save','Close','Quit']
        self.menu_image = pygame.image.load(IMAGES_DIR+'menu.png').convert_alpha()
        self.cursor = Cursor(ypos=[5,30,55,80,105,130,155])

        
    def open_menu(self):
        menu = True
        pygame.key.set_repeat()
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        self.cursor.move_down()
                    if event.key == K_UP:
                        self.cursor.move_up()
                    if event.key == K_RETURN:
                        if self.cursor.position.y == 30:
                            self.open_equipment()
                        if self.cursor.position.y == 55:
                            self.open_magic()
                        if self.cursor.position.y == 80:
                            self.open_status()
                        if self.cursor.position.y == 105:
                            self.save()
                        if self.cursor.position.y == 130:
                            menu = False
                        if self.cursor.position.y == 155:
                            pygame.quit()

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_cursor()
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.key.set_repeat(1,5)



    def render_menu(self):
        pos = 5
        for item in self.menu_items:
            self.buffer.blit(self.font.render(item, 0, pygame.Color("white")), (self.buffer.get_width()-110,pos))
            pos += 25

    def render_cursor(self, animate=True):
        if animate:
            self.cursor.update()
        self.buffer.blit(self.cursor.image, self.cursor.position)


    def save(self):
        # Save function goes here !
        print "Game Save"

    def open_magic(self):
        # MAGIC ! TODO
        popup = True
        while popup:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("You don't have any magic... Yet...", 0,pygame.Color("white")), (10, 50))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def open_equipment(self):
        # EQUIPMENT ! TODO
        popup = True
        while popup:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("You don't have any equipment...", 0,pygame.Color("white")), (10, 50))
            self.buffer.blit(self.font.render("(Yes I'm a lazy developper...)", 0,pygame.Color("white")), (10, 65))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def open_status(self):
        menu = True
        statuscursor = Cursor(ypos=[25, 85, 145, 205], xpos=[0])
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        statuscursor.move_down()
                    if event.key == K_UP:
                        statuscursor.move_up()
                    if event.key == K_RETURN:
                        if statuscursor.position.y == 25:
                            self.status(self.team[0])
                        if statuscursor.position.y == 85:
                            self.status(self.team[1])
                        if statuscursor.position.y == 145:
                            self.status(self.team[2])
                        if statuscursor.position.y == 205:
                            self.status(self.team[3])

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            statuscursor.update()
            self.buffer.blit(statuscursor.image, statuscursor.position)
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def status(self, char):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_char(char, 1)
            self.buffer.blit(self.font.render("Skills", 0,(255,255,255)), (60, 45))
            self.buffer.blit(self.font.render("Stats", 0,(255,255,255)), (60, 60))
            self.buffer.blit(self.font.render("Strength : %d" % char.str, 0,(255,255,255)), (60, 75))
            self.buffer.blit(self.font.render("Defense : %d" % char.defense, 0,(255,255,255)), (300, 75))
            self.buffer.blit(self.font.render("Intelligence : %d" % char.int, 0,(255,255,255)), (60, 90))
            self.buffer.blit(self.font.render("Magic Defense : %d" % char.mdefense, 0,(255,255,255)), (300, 90))
            self.buffer.blit(self.font.render("Dexterity : %d" % char.dex, 0,(255,255,255)), (60, 105))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)




