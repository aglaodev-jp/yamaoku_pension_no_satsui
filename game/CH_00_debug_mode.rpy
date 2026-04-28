# CH_00_debug_mode.rpy

# デバックモードのオンオフは、"CH_01_start_point.rpy"にあります。

label CH_00_debug:

    # デバックモード用ネーム
    # ===== 主人公 =====
    $ player.clear()

    $ player["last"] = "デバ谷"
    $ player["first"] = "モド夫"

    # フルネーム（全角スペース）
    $ player["full"] = f"{player['last']}　{player['first']}"

    # ===== 彼女 =====
    $ heroine.clear()

    $ heroine["last"] = "デバ沢"
    $ heroine["first"] = "モド子"

    $ heroine["full"] = f"{heroine['last']}　{heroine['first']}"

    $ choice_comment = "ようこそ、デバッグモードへ！お好きな場面にご案内します。"

    menu:
        "CH_01_名前入力":
            return
        "エンドロール":
            jump last_scene_kino
        "CH_01_オープニングシーン":
            jump CH_01_start_point
        "CH_02_ペンション前":
            jump CH_02_pension_front
        "CH_03_ペンション玄関＆フロント":
            jump CH_03_pension_entrance
        "CH_04_二階へ":
            jump CH_04_second_floor
        "CH_05_客室":
            jump CH_05_guest_room
        "客室選択肢":
            jump CH_00_k
        "サモエドルート":
            jump CH_00_a
        "人影フラグ":
            $ flag_seen_shadow = True # 人影フラグ（詳細は CH_00_flag.rpy）
            jump CH_00_b
        "タイトルへ":
            $ renpy.full_restart()

    $ choice_comment = ""  

label CH_00_k:
    $ choice_comment = "客室選択肢"
    menu:
        "客室選択肢１":
            jump CH_05_guest_room_c_1
        "客室選択肢２":
            jump CH_05_guest_room_c_2
        "客室選択肢３":
            jump CH_05_guest_room_c_3
        "客室選択肢２の１":
            jump CH_05_guest_room_c_2_1
        "室選択肢２の２":
            jump CH_05_guest_room_c_2_2
        "室選択肢２の３":
            jump CH_05_guest_room_c_2_3
        "もどる":
            jump CH_00_debug

    $ choice_comment = ""  

label CH_00_a:
    $ choice_comment = "サモエドシナリオ"
    menu:
        "ロビーへ":
            jump CH_06_To_the_lobby
        "ロビー選択肢２":
            jump CH_07b_Start_filming
        "レストラン":
            jump CH_08_restaurant_scene
        "客室に戻る":
            jump CH_09_return_to_room
        "お風呂サモエド":
            jump CH_10_public_bath_samoyed
        "悲鳴とサモエドへの邂逅":
            jump CH_11_scream
        "エンディングA":
            jump CH_10_last_scene
        "ひとつ前にもどる":
            jump CH_00_debug
    $ choice_comment = ""  

label CH_00_b:
    $ choice_comment = "人影フラグあり"
    menu:
        "ロビーへ":
            jump CH_06_To_the_lobby
        "ロビー選択肢１":
            jump CH_07a_Start_filming
        "レストラン":
            jump CH_08_restaurant_scene
        "客室に戻る":
            # $ flag_lobby_kino = True # フラグ２ 木下ルート確定へ（詳細は CH_00_flag.rpy）
            jump CH_09_return_to_room
        "お風呂木下":
            jump CH_10_public_bath_kinoshita
        "エンディングB":
            $ flag_lobby_kino = True # フラグ２ 木下ルート確定へ（詳細は CH_00_flag.rpy）
            jump CH_10_last_scene
        "ひとつ前にもどる":
            jump CH_00_debug

    $ choice_comment = ""  