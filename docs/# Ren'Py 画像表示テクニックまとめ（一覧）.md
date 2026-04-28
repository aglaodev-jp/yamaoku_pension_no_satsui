# Ren'Py 画像表示テクニックまとめ（一覧）
# ChatGPTの出力なので正しくないものもあるかも？
## 0. 基本：image 定義と表示
---

# 実際に使って有用だったもの
画像だけ黒く消したい（重要！）

show black at fullscreen_bg with {"master": dissolve}
master レイヤー = 画像が載っているレイヤー

---

### 画像を定義して表示

```renpy
# 画像定義（例：images/bg_room.png）
image bg room = "images/bg_room.png"

# 表示
label start:
    scene bg room
```

### キャラ立ち絵を表示

```renpy
image yui normal = "images/yui/normal.png"

label start:
    show yui normal
```

### 画像を消す

```renpy
hide yui
```

---

## 1. scene と show の違い（超重要）

### scene：背景切り替え（基本的に画面をリセット）

```renpy
scene bg room
```

### show：上に重ねる（キャラ・小物・UIなど）

```renpy
show yui normal
show expression "images/props/book.png"
```

---

## 2. レイヤー感：背景→キャラ→前景（fg）

### 前景（手前に重ねる）を作る例

```renpy
image fg vignette = "images/fg_vignette.png"

label start:
    scene bg room
    show yui normal
    show fg vignette
```

---

## 3. 位置指定（at / Position / align）

### ざっくり「左・中央・右」

```renpy
show yui normal at left
show yui normal at center
show yui normal at right
```

### 画面比率で指定（align）

```renpy
show yui normal:
    xalign 0.2
    yalign 1.0
```

### ピクセルで指定（pos）

```renpy
show yui normal:
    xpos 200
    ypos 100
```

---

## 4. 拡大縮小（zoom / xzoom / yzoom）

### 全体ズーム

```renpy
show yui normal:
    zoom 0.85
```

### 横反転（左右反転）もここで

```renpy
show yui normal:
    xzoom -1.0
```

### 横だけ縮める／縦だけ伸ばす

```renpy
show yui normal:
    xzoom 0.9
    yzoom 1.1
```

---

## 5. 透過（alpha）

```renpy
show yui normal:
    alpha 0.7
```

---

## 6. トランジション（with / dissolve / fade）

### 背景切り替えを自然に

```renpy
scene bg room
with fade
```

### キャラ表示をふわっと

```renpy
show yui normal
with dissolve
```

### 個別に指定もできる

```renpy
show yui normal with dissolve
hide yui with dissolve
```

---

## 7. 画像を動かす（ATL：Animation and Transformation Language）

### フェードイン

```renpy
show yui normal:
    alpha 0.0
    linear 0.4 alpha 1.0
```

### スライドイン（左から入る）

```renpy
show yui normal:
    xalign -0.2
    yalign 1.0
    linear 0.4 xalign 0.2
```

### ちょい揺れ（会話中の息づかい）

```renpy
show yui normal:
    yoffset 0
    linear 0.8 yoffset -6
    linear 0.8 yoffset 0
    repeat
```

---

## 8. Transform を作って再利用（おすすめ）

```renpy
transform yui_left:
    xalign 0.2
    yalign 1.0
    zoom 0.85

transform yui_right:
    xalign 0.8
    yalign 1.0
    zoom 0.85
```

使う：

```renpy
show yui normal at yui_left
```

---

## 9. キャラ差分（表情差分・服差分）

### 命名ルールを揃えると強い

```renpy
image yui normal = "images/yui/normal.png"
image yui smile  = "images/yui/smile.png"
image yui angry  = "images/yui/angry.png"

show yui normal
show yui smile
```

※差分を切り替えるなら `show yui smile` で上書きされます（同じタグ `yui` 扱いになるため）。

---

## 10. tag と属性（同一キャラを上書き表示）

Ren'Py は `show yui smile` の `yui` を「タグ」として扱い、同じタグの表示は自動で差し替えになります。

```renpy
show yui normal
"……"
show yui smile
```

---

## 11. 複数キャラを同時に出す（位置固定運用）

```renpy
show yui normal at left
show aki normal at right
```

より管理しやすくするなら Transform 化（例：`yui_left`, `aki_right`）が安定です。

---

## 12. zorder（手前・奥の順番を強制）

```renpy
show yui normal zorder 10
show fg vignette zorder 100
```

数字が大きいほど手前になります。

---

## 13. behind（特定の表示より後ろに置く）

```renpy
show fog behind yui
```

---

## 14. 画像を合成する（レイヤー合成）

### ConditionSwitch（状態で画像を変える）

```renpy
image yui mood = ConditionSwitch(
    "happy", "images/yui/smile.png",
    "angry", "images/yui/angry.png",
    "True",  "images/yui/normal.png",
)
```

### LiveComposite（パーツ合成：髪＋顔など）

```renpy
image yui composite = LiveComposite(
    (800, 1200),
    (0, 0), "images/yui/base.png",
    (0, 0), "images/yui/face_smile.png",
)
```

---

## 15. 連番アニメ（ぱらぱら）表示

### かんたん版：Animation

```renpy
image yui idle = Animation(
    "images/yui/idle/frame_0000.png", 0.05,
    "images/yui/idle/frame_0001.png", 0.05,
    "images/yui/idle/frame_0002.png", 0.05,
)
```

※ループするのが基本。
※「ループしない」演出は `show` ではなく、状況によって `pause` や `renpy.pause()`、イベント制御、あるいはムービー扱いなど設計で切るのが安定。

---

## 16. シーン演出：カメラっぽいズーム（背景を寄る）

```renpy
scene bg room:
    zoom 1.0
    linear 1.2 zoom 1.08
```

---

## 17. ぼかし・暗転（雰囲気づくり）

### 背景を暗く（簡易）

```renpy
show expression Solid("#000"):
    alpha 0.4
```

### 一部だけ暗く（ビネット等）

```renpy
show fg vignette:
    alpha 0.6
```

---

## 18. 画面揺れ（衝撃演出）

```renpy
with hpunch
with vpunch
```

---

## 19. よく使う “現場の定番” テンプレ

### 背景→暗転→キャラ登場

```renpy
scene bg room with fade
show expression Solid("#000") as shade:
    alpha 0.3
show yui normal at center with dissolve
```

### 左右配置で会話開始

```renpy
scene bg room with fade
show yui smile at left with dissolve
show aki normal at right with dissolve
```

---

## 20. 事故りやすいポイント（短い注意）

* `scene` は基本的に画面リセット（キャラが消えて「あれ？」となりやすい）
* 同じキャラタグ（例：`yui`）は `show yui smile` で差し替えになる
* 手前/奥が思った通りにならない時は `zorder` が最強
* 位置・サイズは Transform 化して統一すると運用が一気に安定



