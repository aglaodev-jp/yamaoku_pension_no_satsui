# transforms.rpy
# ----------------------------
# transform は init で定義（壊れにくい）
# ※ label の中で transform を書くと、処理のたび再定義になり事故りやすい
#
# 設計方針:
# - 位置(pos) と サイズ(scale) と 向き(facing) を分ける
# - show ... at A, B, C のように「部品」を合成して使う
#   → アニメでも静止画でも挙動がブレにくい
# ----------------------------
init -2:

    # --------------------------------------------------------
    # 背景をフルスクリーンで表示する transform
    # --------------------------------------------------------
    transform fullscreen_bg:
        xysize (config.screen_width, config.screen_height)

    # --------------------------------------------------------
    # 立ち絵を中央・足元基準で表示する transform
    # --------------------------------------------------------
    transform char_center:
        xalign 0.5
        yalign 1.0
        zoom 0.6

    # =========================================
    # 1) 位置（pos）: 左 / 中央 / 右
    #    - yalign 1.0 で「足元基準」
    #    - xalign は 0.0(左)〜1.0(右) の割合
    # =========================================
    transform char_pos_left:
        xalign 0.25      # 左寄せ（好みで 0.20〜0.30 など調整）
        yalign 1.0       # 足元基準

    transform char_pos_center:
        xalign 0.5       # 中央
        yalign 1.0       # 足元基準

    transform char_pos_right:
        xalign 0.75      # 右寄せ（好みで 0.70〜0.80 など調整）
        yalign 1.0       # 足元基準


    # =========================================
    # 2) サイズ（scale）: 60% / 80%
    #    - zoom は等倍=1.0
    #    - 直書きで事故りやすいので、部品として分離
    # =========================================
    transform char_scale_60:   # 直張りは不安定になりやすいので transform で分離
        zoom 0.6

    transform char_scale_80:
        zoom 0.8


    # =========================================
    # 3) 向き（facing）: 正面 / 左右反転
    #    - xzoom は横方向の倍率
    #    - -1.0 にすると左右反転（ミラー）
    #    - 画像の向き変更を「部品」にしておくと運用が楽
    # =========================================
    transform char_face_normal:
        xzoom 1.0        # 通常（反転なし）

    transform char_face_flip:
        xzoom -1.0       # 左右反転（右向き画像を左向きに、など）


    # =========================================
    # 4) 合成プリセット（任意）
    #    - よく使う組み合わせを「名前付き」で用意しておく
    #    - 使わないなら show 側で at を並べる運用でもOK
    # =========================================
    transform char_left_60:
        char_pos_left
        char_scale_60
        char_face_normal

    transform char_left_80:
        char_pos_left
        char_scale_80
        char_face_normal

    transform char_center_60:
        char_pos_center
        char_scale_60
        char_face_normal

    transform char_center_80:
        char_pos_center
        char_scale_80
        char_face_normal

    transform char_right_60:
        char_pos_right
        char_scale_60
        char_face_normal

    transform char_right_80:
        char_pos_right
        char_scale_80
        char_face_normal


    # =========================================
    # 5) 反転版プリセット（任意）
    #    - 「左に置くけど右向きにしたい」などの用途に使える
    # =========================================
    transform char_left_80_flip:
        char_pos_left
        char_scale_80
        char_face_flip

    transform char_center_80_flip:
        char_pos_center
        char_scale_80
        char_face_flip

    transform char_right_80_flip:
        char_pos_right
        char_scale_80
        char_face_flip

# 使い方（おすすめ2パターン）
# A) 「合成プリセット」を使う（短く書けて読みやすい）
# show yui idle at char_left_80
# show yui idle at char_right_80_flip

# B) at に部品を並べる（自由度が高い）
# show yui idle at char_pos_left, char_scale_80, char_face_flip