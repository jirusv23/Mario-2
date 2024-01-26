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
jumpCount = 10

zacinajici_pozice_x = rozliseni_okna[0]/2
zacinajici_pozice_y = rozliseni_okna[1] + height

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and pozice_ctverce_x > velocity:  # Making sure the top left position of our character is greater than our velocity so we never move off the screen.
        pozice_ctverce_x -= velocity

    if keys[pygame.K_RIGHT] and pozice_ctverce_x < 500 - velocity - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        pozice_ctverce_x += velocity

    if isJump  == False: #pokuď neskače
        
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            pozice_ctverce_y -= (jumpCount*abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump  = False
    
    okno.fill((0,0,0))
    pygame.draw.rect(okno, (255,0,0), (pozice_ctverce_x, pozice_ctverce_y, width, height))   
    pygame.display.update() 
    
pygame.quit()