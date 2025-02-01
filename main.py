@namespace
class SpriteKind:
    mushroom2 = SpriteKind.create()
    mushroom = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global coin
    coin = sprites.create(img("""
            . . f f f f . . 
                    . f e e e e f . 
                    f e e 5 5 e e f 
                    f e 5 5 5 5 e f 
                    f 9 5 5 5 5 e f 
                    f 9 e 5 5 e e f 
                    . f 9 9 e e f . 
                    . . f f f f . .
        """),
        SpriteKind.food)
    tiles.place_on_tile(coin, location)
    tiles.set_tile_at(location, assets.tile("""
        myTile4
    """))
    coin.follow(luigi)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_on_overlap(sprite6, otherSprite):
    sprites.destroy(otherSprite)
    info.change_score_by(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_b_pressed():
    luigi.set_image(assets.image("""
        myImage3
    """))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile2(sprite7, location6):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile27
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite2, location2):
    tiles.set_tile_at(location2, assets.tile("""
        myTile5
    """))
    tiles.set_tile_at(tiles.get_tile_location(225, 13),
        assets.tile("""
            myTile
        """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile32
    """),
    on_overlap_tile3)

def on_a_pressed():
    luigi.vy = -200
    luigi.set_image(assets.image("""
        myImage1
    """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    luigi.set_image(img("""
        .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                ......777777.....
                ....777777777....
                ......9299222....
                ....9992999292...
                ...99929992292...
                ....2222999922...
                .....9999999.....
                .......777877....
                ....7778778777...
                ...777788887777..
                ...9978e88e8799..
                ...999888888999..
                ...998888888899..
                .....888..888....
                ....777...777....
                ...7777..7777....
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_overlap_tile4(sprite8, location7):
    info.change_score_by(2000)
    tiles.set_tile_at(tiles.get_tile_location(243, 7),
        assets.tile("""
            myTile24
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 8),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 9),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 10),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 11),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 12),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 13),
        assets.tile("""
            myTile25
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile23
    """),
    on_overlap_tile4)

def on_on_overlap2(sprite3, otherSprite2):
    sprites.destroy(otherSprite2)
    info.change_life_by(1)
    info.change_score_by(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.mushroom, on_on_overlap2)

def on_overlap_tile5(sprite4, location4):
    info.change_score_by(5000)
    tiles.set_tile_at(tiles.get_tile_location(243, 7),
        assets.tile("""
            myTile24
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 8),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 9),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 10),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 11),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 12),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 13),
        assets.tile("""
            myTile25
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile9
    """),
    on_overlap_tile5)

def on_life_zero():
    game.splash("oh noooooooooo", "")
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_overlap_tile6(sprite5, location5):
    info.change_score_by(500)
    tiles.set_tile_at(tiles.get_tile_location(243, 7),
        assets.tile("""
            myTile24
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 8),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 9),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 10),
        assets.tile("""
            myTile26
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 11),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 12),
        assets.tile("""
            myTile25
        """))
    tiles.set_tile_at(tiles.get_tile_location(243, 13),
        assets.tile("""
            myTile25
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile8
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite9, location3):
    tiles.set_tile_at(location3, assets.tile("""
        myTile5
    """))
    tiles.set_tile_at(tiles.get_tile_location(211, 13),
        assets.tile("""
            myTile
        """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile31
    """),
    on_overlap_tile7)

def on_on_overlap3(sprite10, otherSprite22):
    if luigi.overlaps_with(bad_mushroom_guy_1):
        if luigi == bad_mushroom_guy_1:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_1)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_1)
    if luigi.overlaps_with(bad_mushroom_guy_2):
        if luigi == bad_mushroom_guy_2:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_2)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_2)
    if luigi.overlaps_with(bad_mushroom_guy_3):
        if luigi == bad_mushroom_guy_3:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_3)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_3)
    if luigi.overlaps_with(bad_mushroom_guy_4):
        if luigi == bad_mushroom_guy_4:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_4)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_4)
    if luigi.overlaps_with(bad_mushroom_guy_5):
        if luigi == bad_mushroom_guy_5:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_5)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_5)
    if luigi.overlaps_with(bad_mushroom_guy_6):
        if luigi == bad_mushroom_guy_6:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_6)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_6)
    if luigi.overlaps_with(bad_mushroom_guy_7):
        if luigi == bad_mushroom_guy_7:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_7)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_7)
    if luigi.overlaps_with(bad_mushroom_guy_8):
        if luigi == bad_mushroom_guy_8:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_8)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_8)
    if luigi.overlaps_with(bad_mushroom_guy_9):
        if luigi == bad_mushroom_guy_9:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_9)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_9)
    if luigi.overlaps_with(bad_mushroom_guy_10):
        if luigi == bad_mushroom_guy_10:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_10)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_10)
    if luigi.overlaps_with(bad_mushroom_guy_11):
        if luigi == bad_mushroom_guy_11:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_11)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_11)
    if luigi.overlaps_with(bad_mushroom_guy_12):
        if luigi == bad_mushroom_guy_12:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_12)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_12)
    if luigi.overlaps_with(bad_mushroom_guy_13):
        if luigi == bad_mushroom_guy_13:
            info.change_life_by(-1)
            sprites.destroy(bad_mushroom_guy_13)
        else:
            info.change_score_by(500)
            sprites.destroy(bad_mushroom_guy_13)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

def on_overlap_tile8(sprite32, location32):
    effects.confetti.start_screen_effect()
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile15
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite11, location8):
    global mushroom3
    mushroom3 = sprites.create(img("""
            . . . . . . 6 6 6 6 . . . . . . 
                    . . . . . 6 6 6 6 7 7 . . . . . 
                    . . . . 6 6 6 6 7 7 7 7 . . . . 
                    . . . 6 6 6 6 6 7 7 7 7 7 . . . 
                    . . 6 6 6 6 6 6 6 7 7 7 6 6 . . 
                    . 6 6 7 7 7 6 6 6 6 6 6 6 6 6 . 
                    . 6 7 7 7 7 7 6 6 6 6 6 6 6 6 . 
                    6 6 7 7 7 7 7 6 6 6 6 6 7 7 6 6 
                    6 6 7 7 7 7 7 6 6 6 6 6 7 7 7 6 
                    6 6 6 7 7 7 6 6 6 6 6 6 6 7 7 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                    . 6 7 7 7 1 1 1 1 1 1 7 7 7 6 . 
                    . . . d 1 1 1 1 1 1 1 1 d . . . 
                    . . . d 1 1 1 1 1 1 6 1 d . . . 
                    . . . d 1 1 1 1 1 1 6 1 d . . . 
                    . . . . d 1 1 1 1 6 1 d . . . .
        """),
        SpriteKind.mushroom)
    tiles.place_on_tile(mushroom3, tiles.get_tile_location(73, 9))
    tiles.set_tile_at(location8, assets.tile("""
        myTile4
    """))
    mushroom3.set_velocity(85, 0)
    mushroom3.ay = 150
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile28
    """),
    on_overlap_tile9)

mushroom3: Sprite = None
coin: Sprite = None
bad_mushroom_guy_13: Sprite = None
bad_mushroom_guy_12: Sprite = None
bad_mushroom_guy_11: Sprite = None
bad_mushroom_guy_10: Sprite = None
bad_mushroom_guy_9: Sprite = None
bad_mushroom_guy_8: Sprite = None
bad_mushroom_guy_7: Sprite = None
bad_mushroom_guy_6: Sprite = None
bad_mushroom_guy_5: Sprite = None
bad_mushroom_guy_4: Sprite = None
bad_mushroom_guy_3: Sprite = None
bad_mushroom_guy_2: Sprite = None
bad_mushroom_guy_1: Sprite = None
luigi: Sprite = None
luigi = sprites.create(img("""
        .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .................
            .....777777......
            ....777777777....
            ....2229929......
            ...2929992999....
            ...29229992999...
            ...2299992222....
            .....9999999.....
            ....778777.......
            ...7778778777....
            ..777788887777...
            ..9978e88e8799...
            ..999888888999...
            ..998888888899...
            ....888..888.....
            ....777...777....
            ....7777..7777...
    """),
    SpriteKind.player)
controller.move_sprite(luigi, 100, 0)
luigi.ay = 410
tiles.set_current_tilemap(tilemap("""
    level 1 world 1    1-1
"""))
tiles.place_on_tile(luigi, tiles.get_tile_location(53, 13))
scene.camera_follow_sprite(luigi)
info.set_life(1)
music.set_volume(6)
bad_mushroom_guy_1 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_2 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_3 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_4 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_5 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_6 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_7 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_8 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_9 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_10 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_11 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_12 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
bad_mushroom_guy_13 = sprites.create(assets.image("""
    myImage
"""), SpriteKind.enemy)
tiles.place_on_tile(bad_mushroom_guy_1, tiles.get_tile_location(76, 14))
tiles.place_on_tile(bad_mushroom_guy_2, tiles.get_tile_location(105, 14))
tiles.place_on_tile(bad_mushroom_guy_3, tiles.get_tile_location(106, 14))
tiles.place_on_tile(bad_mushroom_guy_4, tiles.get_tile_location(133, 6))
tiles.place_on_tile(bad_mushroom_guy_5, tiles.get_tile_location(135, 6))
tiles.place_on_tile(bad_mushroom_guy_6, tiles.get_tile_location(164, 14))
tiles.place_on_tile(bad_mushroom_guy_7, tiles.get_tile_location(165, 14))
tiles.place_on_tile(bad_mushroom_guy_8, tiles.get_tile_location(172, 14))
tiles.place_on_tile(bad_mushroom_guy_9, tiles.get_tile_location(173, 14))
tiles.place_on_tile(bad_mushroom_guy_10, tiles.get_tile_location(176, 14))
tiles.place_on_tile(bad_mushroom_guy_11, tiles.get_tile_location(177, 14))
tiles.place_on_tile(bad_mushroom_guy_12, tiles.get_tile_location(221, 14))
tiles.place_on_tile(bad_mushroom_guy_13, tiles.get_tile_location(222, 14))

def on_update_interval():
    luigi.set_image(img("""
        .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .................
                .....777777......
                ....777777777....
                ....2229929......
                ...2929992999....
                ...29229992999...
                ...2299992222....
                .....9999999.....
                ....778777.......
                ...7778778777....
                ..777788887777...
                ..9978e88e8799...
                ..999888888999...
                ..998888888899...
                ....888..888.....
                ....777...777....
                ....7777..7777...
    """))
    if luigi.vy < 0:
        luigi.set_image(assets.image("""
            myImage1
        """))
    if luigi.vx < 0:
        luigi.image.flip_x()
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    pass
game.on_update_interval(500, on_update_interval2)
