# CH_00_effects.rpy

# ------------ 雨を作る --------------------------------------
# 公式の`SnowBlossom`を使いました。
# 詳しくは docs'SnowBlossomとは（雨や雪などを降らせる）'

# initブロックで雨の画像と挙動の定義
init:
    # （遠い雨・薄く・遅め）
    image rain_back = SnowBlossom(
        "images/effect/rain_light_tile.png",
        count=70, # 粒の数
        xspeed=( -20, 20 ),   # 横方向ランダム
        yspeed=( 1500, 1700 ),  # 落下速度に幅
        start=10 # 開始時にすでに存在している粒の数
    )

    # （近い雨・やや濃い・速め）
    image rain_front = SnowBlossom(
        "images/effect/rain_light_tile.png",
        count=40,
        xspeed=( -40, 40 ),
        yspeed=( 1800, 2000 ),
        start=20
    )

# ちょっと透明にしてみる
transform rain_fade: # アルファ落とす
    alpha 0.4

# # 小雨なら
# count=50
# # 大雨なら
# count=200

# シンプルでいいならこれでも動く
# image rain = SnowBlossom("images/effect/rain_light_tile.png",
#                          count=100, xspeed=10, yspeed=2000, start=20)

# startは、開始時にすでに存在している粒の数
# start=10
# なら、
# まず10粒が最初から画面にある状態でスタート
# そこから徐々に count まで増えていく

# ----------------------------------------------------

# =========================
# シェード機能
# =========================

# 状態フラグ
default shade_on = False


# -------------------------
# シェード表示
# -------------------------
screen shade_overlay():
    if shade_on:
        add Solid("#00000080")


# -------------------------
# キー入力
# -------------------------
screen key_listener():
    key "K_b" action ToggleVariable("shade_on")


# -------------------------
# 常時有効化
# -------------------------
init python:
    config.overlay_screens.append("shade_overlay")
    config.overlay_screens.append("key_listener")

# ----------------------------------------------------

# 画面切り替え用の共通演出をまとめるファイル

# ■ フェード速度を調整する
# fadeは中身としてはこうなっています：
# Fade(0.5, 0.0, 0.3)
# 意味はこうです👇

# 値	内容
# 0.5	フェードアウト時間
# 0.0	画像や色の維持時間
# 0.3	フェードイン時間

# ■ 色も変えられます（超重要）
# 👉 白フェード（フラッシュ演出）
# with Fade(0.2, 0.0, 0.5, color="#fff")

# --- 使用中 ----------------------------

# スローなフェードアウト＆フェードイン
define slow_fade = Fade(2.0, 0.5, 2.0)

# シェードは**イメージ**で定義！（これ大事）
image shade = Solid("#0008")

# scene bg_sumaho_01 at fullscreen_bg
# show shade onlayer master  ←　必ず画像の後においてください。
# with fade

# フラッシュ用
image white = Solid("#fff") # 白画像

label punch_hit:

    show white
    with None
    pause 0.03
    hide white
    with None

    pause 0.05

    return

# ---------------------------------------

# --- 未使用 -----------------------------

define fade_fast = Fade(0.3, 0.0, 0.3)
define fade_normal = Fade(0.7, 0.0, 0.7)
define fade_slow = Fade(1.5, 0.0, 1.5)
define fade_very_slow = Fade(2.5, 0.0, 2.5)

# フェードアウトだけ強め
define fade_out_slow = Fade(2.0, 0.0, 0.3)
# フェードインだけ強め
define fade_in_slow = Fade(0.3, 0.0, 2.0)

# 画像のみ（dissolve）系
define dissolve_fast = Dissolve(0.2)
define dissolve_normal = Dissolve(0.5)
define dissolve_slow = Dissolve(1.0)

# 一瞬白く光るような演出
define flash_white = Fade(0.1, 0.0, 0.2, color="#fff")

# 不穏な場面転換向け
define ominous_fade = Fade(1.8, 0.2, 1.2)

# =========================================
# 赤系演出
# =========================================

# 軽いダメージ
define red_flash_light = Fade(0.1, 0.0, 0.3, color="#f00")

# 強めのダメージ
define red_flash = Fade(0.2, 0.0, 0.6, color="#f00")

# じわっと血の気が引く感じ（おすすめ）
define red_fade_slow = Fade(0.8, 0.5, 1.5, color="#800")

# 一瞬で真っ赤 → すぐ戻る（ショック）
define red_shock = Fade(0.05, 0.0, 0.2, color="#f00")

# つかいかた
# play sound "se/impact.wav"
# with red_flash

# -----------------------------------------


# ----- memo -----------------------------------------
# ■ オーバーレイ方式（かなり強い）

# これはワンランク上のやり方です👇

# image red_overlay = Solid("#ff000088")

# 表示：

# show red_overlay
# with Dissolve(0.5)

# 消す：

# hide red_overlay
# with Dissolve(1.0)

# ■ 脈動っぽい（ドクン…ドクン…）👉
# ・画面に赤フィルターをかける感じ
# ・「ずっと赤い」状態も作れる

# show red_overlay
# with Dissolve(0.3)
# hide red_overlay
# with Dissolve(0.6)

# ■ ちょっとしたコツ（重要）
# 赤は強すぎると安っぽくなる
# 少し暗め（#800 とか #400）を混ぜると一気に上品になる