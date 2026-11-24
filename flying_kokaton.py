import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 練習1：背景画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")

    # 練習3：こうかとん画像の読み込みと左右反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習5：背景画像を右から左へ移動
        x = tmr
        screen.blit(bg_img, [-x, 0])

        # 練習7：2枚目の背景画像を描画
        screen.blit(bg_img, [-x + 1600, 0])

        # 練習4：こうかとん画像の描画
        screen.blit(kk_img, [300, 200])

        pg.display.update()
        tmr += 1

        # 練習6：FPSを200に変更
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

