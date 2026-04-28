# CH_00_flag.rpy

# 客室 人影フラグ
default flag_seen_shadow = False

# ロビー 木下連絡フラグ
default flag_lobby_kino = False

# ロビー 直接行ったフラグ
default flag_lobby_direct = False

# ロビー 撮影フラグ
default flag_lobby_photo_taken = False

# ロビー 撮影aフラグ（物置の分岐で使った）
default flag_a_Start_filming = False

# ルート確定
default route_kino = False
default route_samoyed = False

# ---- つかいかた --------------------------------------------------

# ===== フラグを置く ============================================
#     $ choice_comment = "僕は……"

#     menu:
#         "１．ここで[heroine['first']]と一緒に一夜を過ごすのかとドギマギした。":
#             $ choice_comment = ""
#             jump CH_05_guest_room_c_1

#         "２．「ベッドどっちにする？僕、窓際がいい！」一緒になってはしゃいだ。":
#             $ flag_seen_shadow = True # ← 人影フラグ

#             $ choice_comment = ""
#             jump CH_05_guest_room_c_2

#         "３．部屋をひと通り見渡して、ロケハンの現実に引き戻された。":
#             $ choice_comment = ""
#             jump CH_05_guest_room_c_3


# ===== ルートチェック ============================================

# label route_check:

#     if flag_seen_shadow and flag_lobby_kino: # 人影を見た and ロビーで木下に連絡を取った場合
#         $ route_kino = True
#         jump CH_10_public_bath_kinoshita
#     else:　　　　　　　　　　　　　　　　　　　  # それ以外
#         $ route_samoyed = True
#         jump CH_10_public_bath_samoyed

# ===== 分岐出現フラグ ============================================

    # $ choice_comment = "僕は……"

    # menu:
    #     "１　今回の映画の撮影について考える":
    #         $ choice_comment = ""
    #         jump CH_10a_public_bath_samoyed

    #     "２　[heroine['first']]のことを考える":
    #         $ choice_comment = ""
    #         jump CH_10b_public_bath_samoyed

    #     "３　[heroine['first']]が見た人影のことを考える" if flag_seen_shadow: # 人影を見た場合のみ出現
    #         $ choice_comment = ""
    #         jump CH_10c_public_bath_samoyed

# ===== 簡易的なシナリオ分岐 ============================================

    # if flag_seen_shadow: # 人影を見た場合（flag_seen_shadowを利用）

    #     extend "「ねえさっき、部屋の窓から見た人影って……幽霊！？」\n"
    #     extend "僕は肩をすくめる。\n"
    #     extend "「ああ、森の方にいたってやつ？まさか！」\n"
    #     extend "「でも……」\n"
    #     extend "[heroine['first']]は納得していない顔で窓の外を見る。\n"

    # else: # それ以外

    #     extend "「……白い幽霊か」\n"
    #     extend "それから少し不安そうに周りを見る。\n"
    #     extend "「ねえ、あのペンション……本当に大丈夫かな」\n"

# -------------------------------------------------------------

    # 人影を見た時だけ表示するテキスト
    # if flag_seen_shadow:
    #     extend "そして――\n"
    #     extend "あの人影の話。\n"

    # それ以外の場合で、表示するテキストが特にない場合はそのまま。

    # extend "思考がグルグルとループする。\n"
    # extend "湯船に揺れる湯気をぼんやり見ながら、ふとひとつの考えが頭をよぎる。\n"


