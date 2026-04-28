# Ren’Py 効果音（SE）まとめ

## 1. 基本：SEは鳴らせる？

はい、鳴らせます。
Ren’Py では **`sound` チャンネル** を使って SE（効果音）を再生します。

---

## 2. ファイル配置の基本

```
game/
 └ sounds/
    └ se/
       ├ click.wav
       ├ door_open.ogg
       └ decision.mp3
```

* 対応形式：`wav` / `ogg` / `mp3`
* **おすすめ**：`wav` または `ogg`（遅延が少ない）

---

## 3. いちばん基本の鳴らし方

```renpy
play sound "sounds/se/click.wav"
```

### ポイント

* `sound` は **SE専用チャンネル**
* BGMとは独立して再生される
* 新しいSEが鳴ると、前のSEは止まる

---

## 4. よく使う実践パターン

### テキストと同時に鳴らす

```renpy
play sound "sounds/se/decision.wav"
e "さて、どうしようか……"
```

→ 分岐前・演出強化に有効

---

### 少し間を置いて鳴らす

```renpy
$ renpy.pause(0.5)
play sound "sounds/se/door_open.wav"
```

→ フェード・暗転後の「間」を作れる

---

### SEを止める

```renpy
stop sound
```

→ 演出切り替え時や緊急停止に使用

---

## 5. SEを重ねて鳴らす（重要）

`sound` チャンネルは **1音のみ**。
複数同時に鳴らしたい場合は **専用チャンネルを作る**。

### チャンネル登録（init）

```renpy
init python:
    renpy.music.register_channel(
        "ambient_se", # チャンネル名（play時に使う）
        mixer="ambient_se", # ミキサー設定
        loop=True # ループするかしないか
    )

default preferences.volume.ambient_se = 0.4 # デフォルトで音量を設定するならこれを置く

# 個別ならばチャンネル側を明示的に下げる。
label start:
    $ renpy.music.set_volume(0.4, channel="ambient_se")
    play ambient_se "audio/se/雨の音.mp3"

```

追加のseは volume 0.4 みたいなことができないみたいです。
mixer="sfx"だと、内部的に衝突する？っぽいです。  
今回は名前を付けましたが、場合によっては番号のほうがいいかも。

---

## 6. 音量調整（とても大事）

```renpy
play sound "sounds/se/click.wav" volume 0.4
```

### 目安

* SE音量：**0.3〜0.6**
* 「聞こえるけど主張しない」が正解

---

## 7. UI・選択肢と組み合わせる

### 選択肢表示時のSE

```renpy
play sound "sounds/se/menu_open.wav"
call screen choice(items)
```

---

### ホバー音（操作感が一気に向上）

```renpy
textbutton "調べる":
    action Jump("check")
    hovered Play("sound", "sounds/se/hover.wav")
```

* 短いSE推奨
* 連打してもうるさくならないものを選ぶ

---

## 8. よくある失敗と対策

| よくある失敗   | 対策                   |
| -------- | -------------------- |
| SEがうるさい  | volumeを下げる（0.3〜0.6）  |
| 連打で音が詰まる | 短いwavを使う             |
| BGMとぶつかる | 高音寄りのSEにする           |
| ファイル名が長い | `se_click.wav` など簡潔に |

---

## 9. 演出を一段上げる小ワザ

### 無音SE（間の演出）

```renpy
play sound "sounds/se/silence.wav"
```

→ 「何か起こる」予感を作れる

---

### SEにバリエーションを持たせる

```
click1.wav
click2.wav
click3.wav
```

→ ランダム再生で機械感を減らす

---
