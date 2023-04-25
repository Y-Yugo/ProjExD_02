import random
import sys
import time

import pygame as pg

delta = {                      # 練習4以下こうかとんの移動量の指定
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
        }


def check_bound(scr_rct: pg.Rect, obj_rct: pg.Rect) -> tuple[bool, bool]: # 練習5 画面内or外の判定
    """
    オブジェクトの位置が画面内か外かを判別し、真理値タプルを
    返す関数
    引数１：画面surfaceのRect
    引数２：こうかとん、または爆弾surfaceのRect
    戻り値：横方向、縦方向のはみ出し判定結果
    """

    yoko, tate = True, True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate

 
def main():
    r = 255
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_fin = pg.image.load("ex02/fig/8.png")
    kk_img_fin = pg.transform.rotozoom(kk_img_fin, 0, 2.3)
    kk_rct = kk_img.get_rect() # 練習4

    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (r, 0, 0), (10, 10), 10) # 追加機能５ rを変数にして色を変えたかった
    bb_img.set_colorkey((0, 0, 0)) # 黒色を透過させる
    x, y = random.randint(0, 1600), random.randint(0, 900) # 練習2
    screen.blit(bb_img, [x, y]) 
    vx ,vy = +1, +1
    bb_rct = bb_img.get_rect() # 練習３
    bb_rct.center = x, y       # 練習2 爆弾の初期位置
    kk_rct.center = 900, 400   # 練習4 こうかとんの初期位置
    r -= 1 # 追加機能5　爆弾の色を変えたかった
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        tmr += 1

        key_lst = pg.key.get_pressed() # 練習4
        for k, mv in delta.items():    # 練習4 for文で辞書の中を回す
            if key_lst[k]:
               kk_rct.move_ip(mv)       
        if check_bound(screen.get_rect(), kk_rct) != (True, True):
            for k, mv in delta.items():    # 練習4 for文で辞書の中を回す
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0], -mv[1])
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct) # 練習4
        bb_rct.move_ip(vx, vy)
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko: # 横方向にはみ出していたら
            vx *= -1
        if not tate: # 縦方向にはみ出していたら
            vy *= -1

        screen.blit(bb_img, bb_rct) # 練習3

        if kk_rct.colliderect(bb_rct):  # 練習6 接触判定
            end = tmr
            timer = end + 1             #　追加機能3 未完
            kk_img = kk_img_fin
            vx, vy = 0, 0
            if timer <= tmr:
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()