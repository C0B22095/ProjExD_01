import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = [bg_img, pg.transform.flip(bg_img, True, False)]
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img]
    for i in range(2, 11, 2):
        kk_imgs.append(pg.transform.rotate(kk_img, i))
    
    for i in range(8, 1, -2):
        kk_imgs.append(pg.transform.rotate(kk_img, i))

    kk_imgs.append(kk_img)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        if (tmr//1600)%2==0:
            m = 0
            n = 1
        else:
            m = 1
            n = 0

        x = tmr%1600  
        screen.blit(bg_imgs[m], [-x, 0])
        screen.blit(bg_imgs[n], [1600-x, 0])
        screen.blit(kk_imgs[tmr%11], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()