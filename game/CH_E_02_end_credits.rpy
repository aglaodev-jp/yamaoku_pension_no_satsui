# CH_E_02_end_credits.rpy
# ------------------------------------------------------------
# エンドロール（スタッフロール）関連
# EDごとに背景・影絵・アニメの内容を切り替えられる完成版
# ------------------------------------------------------------

# ------------------------------------------------------------
# どのエンディングだったかを保持
# 分岐先で "samoyed" / "kinoshita" を代入してから
# credits_scroll を呼んでください。
# ------------------------------------------------------------

default ending_type = "samoyed"

# ------------------------------------------------------------
# クレジット本文
# ------------------------------------------------------------

define ENDING_CREDITS_TEXT = """
制作

プログラム・シナリオ：
AglaoDev-jp／ChatGPT（AI）

画像作成：
AglaoDev-jp／ChatGPT 画像生成

画像制作補助：
Microsoft ペイント
ふわっとトリム（自作ツール）
透け影工房（自作ツール）

動画作成：
Sora 2 by OpenAI

動画変換：
FFmpeg

制作補助：
自作スクリプト（未公開を含む）

使用素材（敬称略）

音楽　効果音：
フリーBGM DOVA-SYNDROME

【使用楽曲】

【名前入力画面　エンディング】「ドラマティック・シティ」 蒲鉾さちこ
【館内BGM】「日曜日のカフェ」 くれっぷ
【コミカルシーン】「ぜんぜん余裕です」 キュス
【山小屋レストラン】「Secret Talk」 のる
【恐怖シーン１】「潜む怪奇」 とらさぶ
【恐怖シーン２】「ゾンビホラーパニック」 マニーラ
【エンディング】「Hello,_world」 のる

【使用効果音】

【電話コール】「電話の呼び出し音」 Sakuttipanda
【雨　野外】「雨の音」 Causality Sound
【雨　室内】「雨模様　Track1 … 普通の雨」 稿屋 隆
【ペンションに入る】「入店するときのベル」 MATSU

効果音：
効果音ラボ

使用エンジン:
Ren’Py
Copyright © 2004–2026 Tom Rothamel
License: MIT License

フォント:
Noto Sans JP
© 2014-2021 Adobe
© 2014 Google LLC
SIL Open Font License 1.1

使用エディター：
Visual Studio Code（VSC）

"""

# ------------------------------------------------------------
# エンディング別シーン定義
# ------------------------------------------------------------
# Samoyed 用と Kinoshita 用
# ------------------------------------------------------------

define CREDIT_SCENES_SAMOYED = [
    {
        "bg_type": "movie",
        "bg": "movies/movie_02.webm",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_road_sign_northframe_01",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "movie",
        "bg": "movies/bg/bg_loop_1.webm",
        "rain": True,
        "center": "sil_bg_pension_front",
        "left": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_second_floor_02",
        "rain": False,
        "left": None,
        "center": "sil_second_floor_02",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_to_the_lobby_05",
        "left": None,
        "center": "sil_bg_to_the_lobby_02",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_a_start_filming_04",
        "rain": False,
        "left": None,
        "center": "sil_a_start_filming_08",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "black",
        "anim": {
            "folder": "images/anim/yui_dash/",
            "speed": 0.05,
            "at": "center",
        },
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "movie",
        "bg": "movies/bg/bg_loop_6.webm",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_public_bath_01",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_scream_07",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_last_scene_01",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_last_scene_02",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_pension_entrance_01",
        "left": None,
        "center": None,
        "right": None,
    },
]

define CREDIT_SCENES_KINOSHITA = [
    {
        "bg_type": "movie",
        "bg": "movies/movie_01.webm",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_road_sign_northframe_01",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "movie",
        "bg": "movies/bg/bg_loop_1.webm",
        "rain": True,
        "center": "sil_bg_pension_front",
        "left": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_pension_entrance_04",
        "rain": False,
        "left": None,
        "center": "sil_pension_entrance_08",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_guest_room_05",
        "rain": False,
        "left": None,
        "center": "sil_bg_guest_room_06",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_to_the_lobby_05",
        "left": None,
        "center": "sil_bg_to_the_lobby_02",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_second_floor_03",
        "anim": {
            "folder": "images/anim/dash/",
            "speed": 0.05,
            "at": "center",
        },
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "movie",
        "bg": "movies/bg/bg_loop_7.webm",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_public_bath_03",
        "left": None,
        "center": "sil_public_bath_05",
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": None,
        "anim": {
            "folder": "images/anim/panch/",
            "speed": 0.05,
            "at": "center",
        },
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_last_scene_03",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_last_scene_06",
        "left": None,
        "center": None,
        "right": None,
    },
    {
        "bg_type": "image",
        "bg": "bg_last_scene_04",
        "left": None,
        "center": None,
        "right": None,
    },
]

# ------------------------------------------------------------
# スタッフロール用 transform
# ------------------------------------------------------------

transform staff_roll_scroll(scroll_time=25.0):
    xalign 0.5
    ypos 1.1
    linear scroll_time ypos -3.5

# ------------------------------------------------------------
# END表示用：フェードイン
# ------------------------------------------------------------

transform end_block_fade_in(t=0.8):
    alpha 0.0
    linear t alpha 1.0

# ------------------------------------------------------------
# 便利関数群
# ------------------------------------------------------------

init python:
    # scene 定義から作った displayable をキャッシュする。
    # key は (scene_list_id, scene_index)。
    _credits_scene_cache = {}

    # フレーム一覧キャッシュ。key は (folder, ext, prefix)
    _credits_anim_frames_cache = {}

    def _credits_get_scene_list(ending_type):
        """
        エンディング種別に応じて、
        エンドロール用の scene 一覧を返す。
        """
        if ending_type == "kinoshita":
            return CREDIT_SCENES_KINOSHITA

        # 未定義や想定外は samoyed を返す
        return CREDIT_SCENES_SAMOYED

    def _credits_null():
        """
        表示物が無いとき用の透明ダミー。
        """
        return Null(width=config.screen_width, height=config.screen_height)

    def _credits_build_scene_bundle(scene_list, index):
        """
        指定 scene_list / index の scene を 1 回だけ構築して返す。

        返り値の中身:
        - bg         : 背景 displayable（画像名 or Movie or Null）
        - left       : 左影絵 displayable or Null
        - center     : 中央影絵 displayable or Null
        - right      : 右影絵 displayable or Null
        - anim_data  : アニメ設定 dict or None
        - rain       : 雨 displayable or Null
        """
        cache_key = (id(scene_list), index)

        if cache_key in _credits_scene_cache:
            return _credits_scene_cache[cache_key]

        scene = scene_list[index]

        # ---------- 背景 ----------
        bg = _credits_null()
        bg_type = scene.get("bg_type")
        bg_name = scene.get("bg")

        if bg_type == "image":
            if bg_name:
                bg = bg_name
        elif bg_type == "movie":
            if bg_name:
                bg = Movie(play=bg_name, loop=True)

        # ---------- 影絵 ----------
        left = scene.get("left") if scene.get("left") is not None else _credits_null()
        center = scene.get("center") if scene.get("center") is not None else _credits_null()
        right = scene.get("right") if scene.get("right") is not None else _credits_null()

        # ---------- アニメ ----------
        # ここでは Animation displayable 自体は作らず、
        # scene 内の経過時間から毎フレーム1枚を選ぶ。
        anim_data = scene.get("anim")

        # ---------- 雨 ----------
        rain = "rain_front" if scene.get("rain") else _credits_null()

        bundle = {
            "bg": bg,
            "left": left,
            "center": center,
            "right": right,
            "anim_data": anim_data,
            "rain": rain,
        }

        _credits_scene_cache[cache_key] = bundle
        return bundle

    def _credits_get_anim_frames(folder, ext=".png", prefix=None):
        """
        folder 配下の連番フレーム一覧を返す（キャッシュあり）。
        """
        key = (folder, ext, prefix)

        if key in _credits_anim_frames_cache:
            return _credits_anim_frames_cache[key]

        frames = []
        for f in renpy.list_files():
            if not f.startswith(folder):
                continue
            if not f.lower().endswith(ext):
                continue
            if prefix is not None:
                fname = f.split("/")[-1]
                if not fname.startswith(prefix):
                    continue
            frames.append(f)

        frames.sort()

        if not frames:
            raise Exception(
                "_credits_get_anim_frames: No frames found. folder='{}'".format(folder)
            )

        _credits_anim_frames_cache[key] = frames
        return frames

    def _credits_pick_anim_frame(folder, speed, elapsed, ext=".png", prefix=None):
        """
        ワンショットアニメの『今見せるべき1フレーム』を返す。

        - elapsed はそのシーンに入ってからの経過秒
        - 0 秒未満なら先頭フレーム
        - 最終フレーム到達後は最後のフレームで停止
        """
        frames = _credits_get_anim_frames(folder, ext=ext, prefix=prefix)

        if speed <= 0.0:
            return frames[0]

        if elapsed <= 0.0:
            return frames[0]

        index = int(elapsed / speed)

        if index < 0:
            index = 0
        if index >= len(frames):
            index = len(frames) - 1

        return frames[index]

    def _credits_scene_local_elapsed(scene_list, elapsed, total_scroll_time, scene_index):
        """
        指定 scene の開始から何秒経ったかを返す。
        """
        scene_count = len(scene_list)

        if scene_count <= 0:
            return 0.0

        scene_interval = float(total_scroll_time) / float(scene_count)
        if scene_interval <= 0.0:
            return 0.0

        return elapsed - (scene_index * scene_interval)

    def _credits_scene_math(scene_list, elapsed, total_scroll_time, fade_time):
        """
        経過時間から、現在の scene / 1つ前の scene / クロスフェード率を返す。

        return:
            current_index, previous_index_or_None, current_alpha, previous_alpha
        """
        scene_count = len(scene_list)

        # 念のため防御。scene が 0 個なら 0 固定。
        if scene_count <= 0:
            return 0, None, 1.0, 0.0

        # 1 scene あたりの時間。
        scene_interval = float(total_scroll_time) / float(scene_count)
        if scene_interval <= 0.0:
            return 0, None, 1.0, 0.0

        # 最後の scene を超えても、index は最終 scene に張り付く。
        raw_scene_pos = elapsed / scene_interval
        current_index = int(raw_scene_pos)

        if current_index < 0:
            current_index = 0
        if current_index > scene_count - 1:
            current_index = scene_count - 1

        # scene 内での経過秒。
        scene_start = current_index * scene_interval
        local_elapsed = elapsed - scene_start

        if local_elapsed < 0.0:
            local_elapsed = 0.0

        # フェード時間が 0 以下ならフェードなし。
        if fade_time <= 0.0 or current_index == 0:
            return current_index, None, 1.0, 0.0

        # scene の冒頭 fade_time 秒だけ、前 scene とクロスフェードする。
        if local_elapsed < fade_time:
            ratio = local_elapsed / fade_time

            if ratio < 0.0:
                ratio = 0.0
            if ratio > 1.0:
                ratio = 1.0

            return current_index, current_index - 1, ratio, 1.0 - ratio

        return current_index, None, 1.0, 0.0


# ------------------------------------------------------------
# 映画エンド型 スタッフロール screen
# ------------------------------------------------------------

screen credits_scroll(scroll_time=25.0, fade_time=1.0, music_fade=2.0):

    modal True

    # 今回のエンディングに応じたシーン一覧を固定する。
    # screen 実行中に内容がぶれないよう、起動時点で決める。
    default active_credit_scenes = _credits_get_scene_list(ending_type)

    # スタッフロールが終わったかどうか
    default roll_done = False

    # 経過時間。scene 切替はこれだけで管理する。
    default credit_elapsed = 0.0

    # screen 開始時に scene bundle キャッシュだけクリアする。
    # フレーム一覧キャッシュは共通利用で問題ないので残す。
    on "show" action Function(_credits_scene_cache.clear)

    # 0.05 秒ごとに経過時間を進める。
    # ここでは scene_index 自体は直接いじらない。
    timer 0.05 repeat True action If(
        not roll_done,
        SetScreenVariable("credit_elapsed", min(credit_elapsed + 0.05, scroll_time))
    )

    # 一定時間でロール完了扱いにする
    timer scroll_time action SetScreenVariable("roll_done", True)

    # --------------------------------------------------------
    # 現在 scene とクロスフェード状態を計算
    # --------------------------------------------------------
    $ current_index, previous_index, current_alpha, previous_alpha = _credits_scene_math(active_credit_scenes, credit_elapsed, scroll_time, fade_time)
    $ current_bundle = _credits_build_scene_bundle(active_credit_scenes, current_index)
    $ previous_bundle = _credits_build_scene_bundle(active_credit_scenes, previous_index) if previous_index is not None else None

    # --------------------------------------------------------
    # 背景・影絵・アニメ・雨
    # 「前の scene」を薄く残しつつ、「今の scene」を被せる
    # --------------------------------------------------------

    # 各 scene の中での経過秒。
    $ current_local_elapsed = _credits_scene_local_elapsed(active_credit_scenes, credit_elapsed, scroll_time, current_index)
    $ previous_local_elapsed = _credits_scene_local_elapsed(active_credit_scenes, credit_elapsed, scroll_time, previous_index) if previous_index is not None else 0.0

    # --- 前 scene ---
    if previous_bundle is not None and previous_alpha > 0.0:
        add previous_bundle["bg"] at fullscreen_bg alpha previous_alpha
        add previous_bundle["left"] at sil_left alpha previous_alpha
        add previous_bundle["center"] at sil_center alpha previous_alpha
        add previous_bundle["right"] at sil_right alpha previous_alpha

        if previous_bundle.get("anim_data"):
            $ _prev_anim = previous_bundle["anim_data"]
            $ _prev_anim_elapsed = previous_local_elapsed

            if _prev_anim_elapsed < 0.0:
                $ _prev_anim_elapsed = 0.0

            $ _prev_frame = _credits_pick_anim_frame(
                _prev_anim["folder"],
                _prev_anim.get("speed", 0.05),
                _prev_anim_elapsed
            )

            if _prev_anim.get("at", "center") == "left":
                add _prev_frame at sil_left alpha previous_alpha
            elif _prev_anim.get("at", "center") == "right":
                add _prev_frame at sil_right alpha previous_alpha
            else:
                add _prev_frame at sil_center alpha previous_alpha

        add previous_bundle["rain"] at rain_fade alpha previous_alpha

    # --- 現 scene ---
    add current_bundle["bg"] at fullscreen_bg alpha current_alpha
    add current_bundle["left"] at sil_left alpha current_alpha
    add current_bundle["center"] at sil_center alpha current_alpha
    add current_bundle["right"] at sil_right alpha current_alpha

    if current_bundle.get("anim_data"):
        $ _cur_anim = current_bundle["anim_data"]

        # フェードイン中にアニメを進めたくないので fade_time を引く。
        $ _cur_anim_elapsed = current_local_elapsed - fade_time

        if _cur_anim_elapsed < 0.0:
            $ _cur_anim_elapsed = 0.0

        $ _cur_frame = _credits_pick_anim_frame(
            _cur_anim["folder"],
            _cur_anim.get("speed", 0.05),
            _cur_anim_elapsed
        )

        if _cur_anim.get("at", "center") == "left":
            add _cur_frame at sil_left alpha current_alpha
        elif _cur_anim.get("at", "center") == "right":
            add _cur_frame at sil_right alpha current_alpha
        else:
            add _cur_frame at sil_center alpha current_alpha

    add current_bundle["rain"] at rain_fade alpha current_alpha

    # --------------------------------------------------------
    # 薄い黒ベール
    # --------------------------------------------------------
    add Solid("#0008")

    # --------------------------------------------------------
    # スクロール中の本文
    # --------------------------------------------------------
    if not roll_done:
        text ENDING_CREDITS_TEXT:
            at staff_roll_scroll(scroll_time)
            xalign 0.5
            text_align 0.5
            size 36
            line_spacing 8

    # --------------------------------------------------------
    # ロール完了後は END 表示
    # --------------------------------------------------------
    else:
        vbox:
            xalign 0.5
            yalign 0.57
            spacing 12
            at end_block_fade_in(0.8)

            text "〜 END 〜":
                xalign 0.5
                size 54

            text "Presented by ChatGPT（AI）／AglaoDev-jp":
                xalign 0.5
                size 26

            text "v1":
                xalign 0.5
                size 24

            text "© 2026 AglaoDev-jp":
                xalign 0.5
                size 24

            null height 10

            text "（クリックで戻る）":
                xalign 0.5
                size 24

        key "mouseup_1" action [
            Stop("music", fadeout=music_fade),
            Hide("credits_scroll"),
            With(Fade(fade_time, 0.0, fade_time)),
            Return(True),
        ]