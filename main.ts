namespace SpriteKind {
    export const mushroom2 = SpriteKind.create()
    export const mushroom = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    coin = sprites.create(img`
        . . f f f f . . 
        . f e e e e f . 
        f e e 5 5 e e f 
        f e 5 5 5 5 e f 
        f 9 5 5 5 5 e f 
        f 9 e 5 5 e e f 
        . f 9 9 e e f . 
        . . f f f f . . 
        `, SpriteKind.Food)
    tiles.placeOnTile(coin, location)
    tiles.setTileAt(location, assets.tile`myTile4`)
    coin.follow(luigi)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite6, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeScoreBy(500)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    luigi.setImage(assets.image`myImage3`)
    info.startCountdown(2)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile27`, function (sprite7, location6) {
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile32`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`myTile5`)
    tiles.setTileAt(tiles.getTileLocation(225, 13), assets.tile`myTile`)
    info.changeLifeBy(-1)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    luigi.vy = -200
    luigi.setImage(assets.image`myImage1`)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    luigi.image.flipX()
})
info.onCountdownEnd(function () {
    luigi.setImage(assets.image`myImage2`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile23`, function (sprite8, location7) {
    info.changeScoreBy(2000)
    tiles.setTileAt(tiles.getTileLocation(243, 7), assets.tile`myTile24`)
    tiles.setTileAt(tiles.getTileLocation(243, 8), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 9), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 10), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 11), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 12), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 13), assets.tile`myTile25`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    luigi.setImage(assets.image`myImage2`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.mushroom, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    info.changeLifeBy(1)
    info.changeScoreBy(1000)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile9`, function (sprite4, location4) {
    info.changeScoreBy(5000)
    tiles.setTileAt(tiles.getTileLocation(243, 7), assets.tile`myTile24`)
    tiles.setTileAt(tiles.getTileLocation(243, 8), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 9), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 10), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 11), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 12), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 13), assets.tile`myTile25`)
})
info.onLifeZero(function () {
    game.splash("oh noooooooooo", "")
    game.gameOver(false)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile8`, function (sprite5, location5) {
    info.changeScoreBy(500)
    tiles.setTileAt(tiles.getTileLocation(243, 7), assets.tile`myTile24`)
    tiles.setTileAt(tiles.getTileLocation(243, 8), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 9), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 10), assets.tile`myTile26`)
    tiles.setTileAt(tiles.getTileLocation(243, 11), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 12), assets.tile`myTile25`)
    tiles.setTileAt(tiles.getTileLocation(243, 13), assets.tile`myTile25`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile31`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`myTile5`)
    tiles.setTileAt(tiles.getTileLocation(211, 13), assets.tile`myTile`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite10, otherSprite2) {
    if (luigi.overlapsWith(bad_mushroom_guy_1)) {
        if (luigi.vy == bad_mushroom_guy_1.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_1)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_1)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_2)) {
        if (luigi.vy == bad_mushroom_guy_2.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_2)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_2)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_3)) {
        if (luigi.vy == bad_mushroom_guy_3.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_3)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_3)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_4)) {
        if (luigi.vy == bad_mushroom_guy_4.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_4)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_4)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_5)) {
        if (luigi.vy == bad_mushroom_guy_5.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_5)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_5)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_6)) {
        if (luigi.vy == bad_mushroom_guy_6.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_6)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_6)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_7)) {
        if (luigi.vy == bad_mushroom_guy_7.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_7)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_7)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_8)) {
        if (luigi.vy == bad_mushroom_guy_8.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_8)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_8)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_9)) {
        if (luigi.vy == bad_mushroom_guy_9.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_9)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_9)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_10)) {
        if (luigi.vy == bad_mushroom_guy_10.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_10)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_10)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_11)) {
        if (luigi.vy == bad_mushroom_guy_11.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_11)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_11)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_12)) {
        if (luigi.vy == bad_mushroom_guy_12.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_12)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_12)
        }
    }
    if (luigi.overlapsWith(bad_mushroom_guy_13)) {
        if (luigi.vy == bad_mushroom_guy_13.vy) {
            info.changeLifeBy(-1)
            sprites.destroy(bad_mushroom_guy_13)
        } else {
            info.changeScoreBy(500)
            sprites.destroy(bad_mushroom_guy_13)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile15`, function (sprite3, location3) {
    effects.confetti.startScreenEffect()
    game.gameOver(true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile28`, function (sprite, location) {
    mushroom = sprites.create(img`
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
        `, SpriteKind.mushroom)
    tiles.placeOnTile(mushroom, tiles.getTileLocation(73, 9))
    tiles.setTileAt(location, assets.tile`myTile4`)
    mushroom.setVelocity(85, 0)
    mushroom.ay = 150
})
let mushroom: Sprite = null
let coin: Sprite = null
let bad_mushroom_guy_13: Sprite = null
let bad_mushroom_guy_12: Sprite = null
let bad_mushroom_guy_11: Sprite = null
let bad_mushroom_guy_10: Sprite = null
let bad_mushroom_guy_9: Sprite = null
let bad_mushroom_guy_8: Sprite = null
let bad_mushroom_guy_7: Sprite = null
let bad_mushroom_guy_6: Sprite = null
let bad_mushroom_guy_5: Sprite = null
let bad_mushroom_guy_4: Sprite = null
let bad_mushroom_guy_3: Sprite = null
let bad_mushroom_guy_2: Sprite = null
let bad_mushroom_guy_1: Sprite = null
let luigi: Sprite = null
luigi = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(luigi, 100, 0)
luigi.ay = 410
tiles.setCurrentTilemap(tilemap`level 1 world 1    1-1`)
tiles.placeOnTile(luigi, tiles.getTileLocation(53, 13))
scene.cameraFollowSprite(luigi)
info.setLife(1)
music.setVolume(6)
bad_mushroom_guy_1 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_2 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_3 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_4 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_5 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_6 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_7 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_8 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_9 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_10 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_11 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_12 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
bad_mushroom_guy_13 = sprites.create(assets.image`myImage`, SpriteKind.Enemy)
tiles.placeOnTile(bad_mushroom_guy_1, tiles.getTileLocation(76, 14))
tiles.placeOnTile(bad_mushroom_guy_2, tiles.getTileLocation(105, 14))
tiles.placeOnTile(bad_mushroom_guy_3, tiles.getTileLocation(106, 14))
tiles.placeOnTile(bad_mushroom_guy_4, tiles.getTileLocation(133, 6))
tiles.placeOnTile(bad_mushroom_guy_5, tiles.getTileLocation(135, 6))
tiles.placeOnTile(bad_mushroom_guy_6, tiles.getTileLocation(164, 14))
tiles.placeOnTile(bad_mushroom_guy_7, tiles.getTileLocation(165, 14))
tiles.placeOnTile(bad_mushroom_guy_8, tiles.getTileLocation(172, 14))
tiles.placeOnTile(bad_mushroom_guy_9, tiles.getTileLocation(173, 14))
tiles.placeOnTile(bad_mushroom_guy_10, tiles.getTileLocation(176, 14))
tiles.placeOnTile(bad_mushroom_guy_11, tiles.getTileLocation(177, 14))
tiles.placeOnTile(bad_mushroom_guy_12, tiles.getTileLocation(221, 14))
tiles.placeOnTile(bad_mushroom_guy_13, tiles.getTileLocation(222, 14))
game.onUpdateInterval(1000, function () {
    if (luigi.vy < 0) {
        luigi.setImage(assets.image`myImage1`)
    } else {
    	
    }
    if (luigi.vx < 0) {
    	
    }
})
