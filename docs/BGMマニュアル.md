# Ren’Py BGM再生テクニックまとめ（Markdown）

## 1. BGMの基本（再生・停止）

### 再生（ループが基本）

```renpy
play music "audio/bgm/theme.ogg"
```

### 停止

```renpy
stop music
```

### フェードアウト付き停止

```renpy
stop music fadeout 2.0
```

### 再生時にフェードイン

```renpy
play music "audio/bgm/theme.ogg" fadein 1.5
```

---

## 2. 「曲を切り替える」基本

### 曲を差し替え（前の曲は自動で止まる）

```renpy
play music "audio/bgm/next_theme.ogg"
```

### 切り替えを自然にしたい（フェードアウト → フェードイン）

```renpy
stop music fadeout 1.5
pause 1.5
play music "audio/bgm/next_theme.ogg" fadein 1.0
```

> **ポイント**：`pause` は「フェードアウトが終わるまで待つ」ために入れると、唐突感が減ります。
> ただし演出方針によっては、あえて待たずに次を入れてテンポ重視でもOKです。

---

## 3. ループさせたくない（BGMをワンショットで流す）
Ren’Pyの `play music` は基本ループします。
**ループさせたくない場合**

方法①：noloop を使う（公式・推奨）
```
play music "audio/bgm/intro.ogg" noloop
```

✅ これが正解です

loop → ループする

noloop → 1回再生で終了

方法②：queue music を使う（自然に終わらせたい場合）
```
queue music "audio/bgm/intro.ogg"
```

1回再生のみ

次の音楽がなければ、そのまま終了

エンディング・余韻向き


~`loop` を明示的に `False` にします。~**これは間違い**

---

## 4. 「イントロだけ一回」→「ループ曲へ」みたいな構成

### A案：intro（非ループ）→終わったらループ曲へ

```renpy
play music "audio/bgm/intro.ogg" noloop
$ renpy.music.queue("audio/bgm/loop.ogg", channel="music", loop=True)
```

* `play`：いま流す
* `queue`：次に流すものを予約

> **ポイント**：`queue` は「曲が終わったら次へ」を作れるので、自然につながります。

---

## 5. 特定のタイミングで「BGMだけ一時停止」したい

Ren’Pyには「一時停止/再開」もあります。
（ただし、プロジェクトやRen’Pyバージョン/環境によって挙動確認は必要です）

### 一時停止

```renpy
$ renpy.music.set_pause(True, channel="music")
```

### 再開

```renpy
$ renpy.music.set_pause(False, channel="music")
```

> **用途例**：ムービー演出中だけBGMを止めて、終わったら同じ位置から再開したい時。

---

## 6. 音量（フェード含む）を操作する

### その場で音量を変える（0.0〜1.0）

```renpy
$ renpy.music.set_volume(0.4, channel="music")
```

### じわっと音量を変える（フェード）

```renpy
$ renpy.music.set_volume(0.4, delay=1.0, channel="music")
```

> **用途例**：会話シーンは小さめ、盛り上げで戻す、など。

---

## 7. 「同じ曲をもう一度最初から鳴らしたい」

同じファイルを `play music` しても、状況によっては“鳴り直し”にならないことがあります。
確実に「最初から」にしたい場合は、いったん止めてから再生すると安定します。

```renpy
stop music
play music "audio/bgm/theme.ogg"
```

フェード演出を入れるなら：

```renpy
stop music fadeout 0.2
pause 0.2
play music "audio/bgm/theme.ogg" fadein 0.2
```

---

## 8. チャンネル（music）を意識して管理するコツ

Ren’PyのBGMは通常 `music` チャンネルに流れます。
複数系統のBGM（例：通常BGMと戦闘BGMを別管理）をしたい場合は、**別チャンネルを増やす設計**も可能です。

例（コンセプト）：

* `music`：通常BGM
* `battle`：戦闘BGM（独立）

ただしこの場合は `define config.channels` など設計が絡むため、必要になったタイミングで整理すると安全です。

---

## 9. よくある「演出テンプレ」

### 緊張感：BGMを薄くして間を作る

```renpy
$ renpy.music.set_volume(0.25, delay=0.8, channel="music")
pause 0.8
```

### 場面転換：暗転→フェードアウト→少し溜め→次曲フェードイン

```renpy
scene black
with fade

stop music fadeout 2.0
pause 0.8

play music "audio/bgm/new_scene.ogg" fadein 1.5
```

---

## 10. デバッグのコツ（「今なにが鳴ってる？」）

BGMが「鳴らない」「切り替わらない」時は、まず**ファイルパス**と**拡張子**の確認が最優先です。
次に、意図通り `play/stop/queue` が呼ばれているかをログに出すと切り分けが楽です。

```renpy
$ renpy.log("BGM: play new_scene.ogg")
play music "audio/bgm/new_scene.ogg"
```

---

## 付録：おすすめの整理ルール（地味に効く）

* BGMの置き場所を固定：`game/audio/bgm/`
* ファイル名に用途を入れる：

  * `bgm_city_day.ogg`
  * `bgm_mystery_low.ogg`
  * `bgm_battle_loop.ogg`
* `intro` と `loop` を分けるなら命名で分かるように：

  * `bgm_title_intro.ogg`
  * `bgm_title_loop.ogg`

---

## renpy.music.set_volume() で下げた音量は、そのまま次のBGMにも引き継がれます。  

つまり、
```
$ renpy.music.set_volume(0.4, channel="music")
```
を一度実行すると、
その後に流す 別のBGM
```
play music "別の曲.ogg"
```
も 音量 0.4 のまま 再生されます。
