import pygame
pygame.init()


rozliseni_okna = (500,500)
okno = pygame.display.set_mode(rozliseni_okna)
pygame.display.set_caption("First Game")

width = 50
height = 50

pozice_ctverce_x = ((rozliseni_okna[0]/2) - width/2)
pozice_ctverce_y = (rozliseni_okna[1]-height)

velocity = 4
isJump = False

velikost_pohybu = 8  
jumpCount = velikost_pohybu

zacinajici_pozice_x = rozliseni_okna[0]/2 #doproštred obrazovky
zacinajici_pozice_y = rozliseni_okna[1] + height #na spodek obrazovky

run = True

while run:
    pygame.time.delay(10) #framerate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    stisknuté_klavesy = pygame.key.get_pressed()
    
    if stisknuté_klavesy[pygame.K_LEFT] and pozice_ctverce_x > velocity:  #pohyb vlevo a kontrola zdi
        pozice_ctverce_x -= velocity

    if stisknuté_klavesy[pygame.K_RIGHT] and pozice_ctverce_x < 500 - velocity - width:  #pohyb pravo a kontrola zdi
        pozice_ctverce_x += velocity

    if isJump  == False: #pokuď neskače
        
        if stisknuté_klavesy[pygame.K_SPACE]: 
            isJump = True
    else:
        if jumpCount >= -velikost_pohybu:
            pozice_ctverce_y -= (jumpCount*abs(jumpCount)) * 0.5 #snižuje rychlost skoku nahoru
            jumpCount -= 1 #snižuje čas skoku
        else:
            jumpCount = velikost_pohybu #resetuje a připravý na nový skok
            isJump  = False 
    
    okno.fill((0,0,0))
    pygame.draw.rect(okno, (255,0,0), (pozice_ctverce_x, pozice_ctverce_y, width, height))   
    pygame.display.update() 
    
pygame.quit()