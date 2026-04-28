# SnowBlossomとは（雨や雪などを降らせる）

`SnowBlossom` は Ren'Py に標準搭載されている **パーティクル（粒子）エフェクト用クラス** です。

主に以下のような演出に使用できます：

* 雪
* 雨
* 花びら
* 落ち葉
* ほこり・光粒子

指定した画像を複数生成し、ランダムな位置と速度で画面内に落下させ続ける仕組みです。

---

# 基本構文

```renpy
image rain = SnowBlossom(
    "images/effect/rain.png",
    count=100,
    xspeed=( -20, 20 ),
    yspeed=( 500, 800 ),
    start=20
)
```

---

# 主なパラメータ

## `image`

使用する粒子画像のパス。

* 透過PNG推奨
* 細長い画像で雨向き
* 正方形で雪向き

---

## `count`

画面上に同時に存在する粒子の最大数。

| 値   | 雰囲気   |
| --- | ----- |
| 30  | 小雨・小雪 |
| 70  | 通常    |
| 150 | 本降り   |
| 300 | 豪雨    |

---

## `xspeed`

横方向の移動速度。

```renpy
xspeed=(-40, 40)
```

タプル指定でランダム範囲になります。

* 0 → 真下に落ちる
* 幅を持たせる → 風が吹いている表現

---

## `yspeed`

縦方向の落下速度。

```renpy
yspeed=(500, 800)
```

* 数値が大きいほど速く落ちる
* 幅を持たせると自然になる

---

## `start`

開始時にすでに存在している粒子数。

| 設定       | 効果       |
| -------- | -------- |
| 0        | 徐々に降り始める |
| countと同じ | 最初から本降り  |

---

# 表示方法

```renpy
show rain
```

消す場合：

```renpy
hide rain
```

---

# より自然に見せるコツ

## 1. 前後レイヤーを作る

```renpy
image rain_back = SnowBlossom("rain.png", count=60, yspeed=(400,600))
image rain_front = SnowBlossom("rain.png", count=40, yspeed=(800,1000))
```

```
show rain_back
show rain_front
```

奥行きが生まれます。

---

## 2. 透明度を調整する

```renpy
transform rain_fade:
    alpha 0.5
```

```
show rain_back at rain_fade
```

---

## 3. 小雨 → 豪雨の演出

```renpy
show rain_light
pause 3.0
hide rain_light
show rain_heavy
```

---

# SnowBlossomの正体

`SnowBlossom` は Ren'Py 内部に定義された **Displayable クラス**です。

内部では：

* 粒子をランダム配置
* 毎フレーム位置更新
* 画面外に出たら再生成

という処理を自動で行っています。

---

# 注意点

* countを増やしすぎると処理が重くなる
* 画像サイズが大きすぎると不自然になる
* 透過画像でないと背景が白くなる

---

# 使用例まとめ（雨）

```renpy
init:

    image rain_back = SnowBlossom(
        "images/effect/rain_light_tile.png",
        count=70,
        xspeed=(-20, 20),
        yspeed=(500, 700),
        start=10
    )

    image rain_front = SnowBlossom(
        "images/effect/rain_light_tile.png",
        count=40,
        xspeed=(-40, 40),
        yspeed=(800, 1000),
        start=20
    )
```

---

# まとめ

SnowBlossom は：

* Ren'Py標準のパーティクルクラス
* 雪や雨を簡単に実装できる
* count・速度・startで演出を調整可能
* 前後レイヤーで奥行きを作れる

---

# 🌸 SnowBlossom 演出テンプレ集

---

# 🌸 1. 花びらテンプレ（春・回想・優しいシーン）

## 粒子画像

* ピンクの小さめPNG
* 少し横長でもOK
* 軽く回転しても自然

---

## 定義

```renpy
init:

    image petals_back = SnowBlossom(
        "images/effect/petal.png",
        count=40,
        xspeed=(-30, 30),
        yspeed=(150, 250),
        start=10
    )

    image petals_front = SnowBlossom(
        "images/effect/petal.png",
        count=25,
        xspeed=(-60, 60),
        yspeed=(200, 300),
        start=15
    )
```

---

## 表示

```renpy
show petals_back
show petals_front
```

---

## ポイント

* yspeedは遅め
* xspeed大きめで「ひらひら感」
* countは控えめ

---

# 🌫 2. 霧・光粒子テンプレ（幻想・夢・神秘）

## 粒子画像

* ぼかした丸
* 半透明PNG
* 小さな光点

---

## 定義

```renpy
init:

    image mist = SnowBlossom(
        "images/effect/light_dot.png",
        count=60,
        xspeed=(-10, 10),
        yspeed=(-20, 20),
        start=40
    )
```

---

## 透明度調整

```renpy
transform mist_fade:
    alpha 0.3
```

```
show mist at mist_fade
```

---

## ポイント

* yspeedをマイナスにすると上昇演出も可能
* xspeedを小さくするとゆっくり漂う
* alphaを低めに

---

# ⚡ 3. 雷付き豪雨テンプレ（緊迫・クライマックス）

## 雨

```renpy
init:

    image heavy_rain = SnowBlossom(
        "images/effect/rain_heavy.png",
        count=200,
        xspeed=(-50, 50),
        yspeed=(900, 1200),
        start=200
    )
```

---

## 雷フラッシュ

```renpy
transform lightning_flash:
    alpha 0.0
    linear 0.1 alpha 1.0
    linear 0.2 alpha 0.0
```

---

## 雷表示

```renpy
image white_flash = Solid("#FFFFFF")
```

使用例：

```renpy
show white_flash at lightning_flash
play sound "audio/se/thunder.wav"
```

---

## ポイント

* countは多め
* yspeed高速
* 雷は短時間表示
* SEと同期させる

---

# 👻 4. ホラー向け演出テンプレ

## 微粒子（静かな不穏）

```renpy
init:

    image dust = SnowBlossom(
        "images/effect/dust.png",
        count=30,
        xspeed=(-5, 5),
        yspeed=(50, 100),
        start=10
    )
```

---

## 画面暗転トランスフォーム

```renpy
transform horror_tint:
    matrixcolor TintMatrix("#553333")
```

---

## 微フラッシュ（違和感）

```renpy
transform glitch_flash:
    alpha 0.0
    linear 0.05 alpha 0.2
    linear 0.05 alpha 0.0
    repeat
```

---

## 使用例

```renpy
show dust
scene bg_school at horror_tint
```

---

## ポイント

* 粒子は少なめ
* ゆっくり
* 色味で心理演出
* フラッシュは控えめ

---

# 🎭 演出パラメータ早見表

| 演出  | count | yspeed | xspeed |
| --- | ----- | ------ | ------ |
| 花びら | 少なめ   | 遅い     | 大きめ    |
| 霧   | 中     | ほぼ0    | 小      |
| 豪雨  | 多い    | 速い     | 中〜大    |
| ホラー | 少     | 遅い     | 小      |

---

# 🎬 応用アイデア

* 複数SnowBlossom重ねる
* 時間経過でcount変更
* 心情に応じて速度変化
* BGMと同期

---


