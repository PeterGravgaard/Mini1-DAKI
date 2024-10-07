import pygame
import math
from datetime import datetime

pygame.init()
pygame.display.set_caption("Molbo Ur = Tiden går baglæns")

screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size)
start_position = (screen_size[0]/2, screen_size[1]/2)#Start positionen til urskiven i en tupel. (x, y)
radius = 200
font = pygame.font.SysFont(None, 36)

#Funktionen der tegner viser
def viser(angle, length, color, width):
    end_offset = [length * math.cos(math.radians(angle - 90)),
                  length * math.sin(math.radians(angle - 90))]
    end_position = (start_position[0] + end_offset[0], start_position[1] + end_offset[1])
    pygame.draw.line(screen, color, start_position, end_position, width)

def draw_line():
    #Tegner de 12 streger på urskiven
    for i in range(12):
        # Beregn vinkel 
        angle = 360 / 12 * i - 90  # 360 grader i en time, -90 for at starte i midten.
        
        # Beregn start og slutt offset
        start_offset = [(radius - 20) * math.cos(math.radians(angle)),
                        (radius - 20) * math.sin(math.radians(angle))]#
        end_offset = [radius * math.cos(math.radians(angle)),
                      radius * math.sin(math.radians(angle))]
        
        # Beregn den faktiske position på skærmen
        start_position_line = (start_position[0] + start_offset[0], start_position[1] + start_offset[1])
        end_position_line = (start_position[0] + end_offset[0], start_position[1] + end_offset[1])
        
        # Tegner linjerne 
        pygame.draw.line(screen, (0, 0, 0), start_position_line, end_position_line, 4)

def tegn_numre():
    position = {
        "12": (start_position[0], start_position[1] - radius + 40),#Start positionen til urskiven i en tupel. (x, y)
        "3": (start_position[0] + radius - 30, start_position[1]),
        "6": (start_position[0], start_position[1] + radius - 30),
        "9": (start_position[0] - radius + 30, start_position[1])
    }
    for numre, pos in position.items():
        text = font.render(numre, True, (0, 0, 0))
        text_rect = text.get_rect(center=pos)# centrerer teksten
        screen.blit(text, text_rect)# tegner teksten

while True:
    screen.fill((255, 255, 255))
    
    draw_line()
    pygame.draw.circle(screen, (0, 0, 0), start_position, radius +10, 6) #Tegner urskiven. color, position, radius, width
    pygame.draw.circle(screen, (0, 0, 0), start_position, 10)
    tegn_numre()
    s = datetime.now().second #Henter tiden fra datetime modulet
    m = datetime.now().minute
    h = datetime.now().hour % 12 # Modulus 12 for at gøre 0-11
    angle_second = 360 - (360 / 60 * s) #360 - for at det går baglæns
    angle_minute = 360 - (360 / 60 * m + (360 / 60) * (s / 60))
    angle_hour = 360 - (360 / 12 * h + (360 / 12) * (m / 60) ) 
    
    viser(angle_second, radius - 30, (0, 0, 0), 2) #argumenter: angle, length, color, width
    viser(angle_minute, radius - 60, (0, 0, 0), 5)
    viser(angle_hour, radius - 100, (0, 0, 0), 8)
    
    pygame.display.flip()

    #Programmet kører i et loop til der trykkes escape eller programmet lukkes
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()