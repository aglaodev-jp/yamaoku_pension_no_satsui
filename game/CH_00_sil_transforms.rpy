# game/CH_00_sil_transforms.rpy

# ==================================================
#  Silhouette Transforms
# ==================================================

# 中央配置（基本形）
transform sil_center:
    xysize (config.screen_width, config.screen_height) # 00_transforms.rpyと同じ方法です。
    xalign 0.5
    yalign 1.0
    zoom 1.0
    alpha 0.85

# 左配置
transform sil_left:
    # xysize (config.screen_width, config.screen_height)
    xalign 0.0
    yalign 1.0
    zoom 1.0
    alpha 0.85

# 右配置
transform sil_right:
    # xysize (config.screen_width, config.screen_height)
    xalign 0.9
    yalign 1.0
    zoom 0.95
    alpha 0.85

# 少しフェードイン
transform sil_fadein:
    alpha 0.0
    linear 0.4 alpha 0.85

# 少しフェードアウト（基本alpha 0.85 → 0へ）
transform sil_fadeout:
    alpha 0.85
    linear 0.4 alpha 0.0

# -----つかいかた-----------

# # 表示(フェードイン)
# show sil_yui_idle at sil_center, sil_fadein
# narrator_arrow "影が、静かに現れる。"

# # フェードアウトして消す
# show sil_yui_idle at sil_center, sil_fadeout
# pause 0.4
# hide sil_yui_idle
