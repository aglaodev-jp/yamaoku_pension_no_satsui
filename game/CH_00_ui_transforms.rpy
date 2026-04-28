# CH_00_ui_transforms.rpy

# -------- 文末アイコン --------------------------
define narrator_arrow = Character(
    None,
    ctc=ctc_switch,
    ctc_position="nestled-close",
    callback=ctc_reset_callback
)
# -------------------------------------------------

# どちらのアイコンを出すかを管理
default ctc_mode = "arrow"

init -1:
    transform blink:
        alpha 1.0
        linear 0.6 alpha 0.15
        linear 0.6 alpha 1.0
        repeat

init -1 python:
    # 点滅displayable
    ctc_arrow_blink = At(Transform("ui/arrow.png", zoom=0.1), blink)
    ctc_page_blink = At(Transform("ui/page_turn.png", zoom=0.1), blink)

    # 変数 ctc_mode に応じて、出すアイコンを切り替える
    ctc_switch = ConditionSwitch(
        "ctc_mode == 'page'", ctc_page_blink,
        "True", ctc_arrow_blink
    )


    # 発話が終わったら、自動で矢印モードに戻す（callback）
    def ctc_reset_callback(event, interact=True, **kwargs):
        if event == "end":
            store.ctc_mode = "arrow"

