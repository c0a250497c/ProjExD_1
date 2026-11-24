import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像の読み込みと左右反転
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img, True, False)

    # こうかとん画像の読み込みと左右反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    # こうかとんの初期座標
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 背景画像の無限スクロール
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])

        # 全キーの押下状態を取得
        key_lst = pg.key.get_pressed()

        # 演習1：背景と同じ速度で左に流す
        dx = -1
        dy = 0

        # 上矢印キーによる移動量
        if key_lst[pg.K_UP]:
            dy -= 1

        # 下矢印キーによる移動量
        if key_lst[pg.K_DOWN]:
            dy += 1

        # 左矢印キーによる移動量
        if key_lst[pg.K_LEFT]:
            dx -= 1

        # 右矢印キーによる移動量
        if key_lst[pg.K_RIGHT]:
            dx += 2

        # 演習2：移動量をまとめて1回で反映する
        kk_rct.move_ip(dx, dy)

        # こうかとんの描画
        screen.blit(kk_img, kk_rct)

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
