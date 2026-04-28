## MP4の動画をwebmに変換

FFmpegとは？
世界標準レベルの動画変換ツール
Ren’Py界隈・ゲーム開発者・動画制作者が全員使ってる定番
完全無料・広告なし・安全

🔹 手順（Windows想定・最短ルート）
① FFmpegをダウンロード

公式サイト：
👉 https://ffmpeg.org/download.html

Windowsなら
「Windows builds」→「gyan.dev」→「release full」

zipを展開（例：C:\ffmpeg\bin）

※ パス設定はあとでやってもOKです
（最初は動画フォルダに ffmpeg.exe を置いても動きます）

② MP4 → WebM に変換（Ren’Py向け・推奨）

コマンドプロンプトで以下を実行：
```
ffmpeg -i input.mp4 -c:v libvpx-vp9 -crf 32 -b:v 0 -pix_fmt yuv420p output.webm
```
🔸 各項目の意味（安心用）

libvpx-vp9：WebM用の高品質コーデック

-crf 32：画質と容量のバランス（28〜35で調整可）

yuv420p：Ren’Py互換性◎

👉 Ren’Py 8.x で非常に安定します

🔹 音声も入れたい場合（推奨）
```
ffmpeg -i input.mp4 -c:v libvpx-vp9 -crf 32 -b:v 0 -c:a libopus output.webm
```

# （超やさしい）FFmpegの使い方

## ゴール

👉 **MP4ファイルを WebM に変換できるようになる**

---

## ステップ①：ダウンロードしたFFmpegを確認する

まず、ダウンロードしたZIPを **右クリック → 解凍** してください。

解凍後、だいたいこんな構成になっています：

```
ffmpeg-xxxx/
 ├ bin/
 │   ├ ffmpeg.exe   ← ← ← これが主役です
 │   ├ ffplay.exe
 │   └ ffprobe.exe
 ├ doc/
 └ presets/
```

### ✅ 確認ポイント

* `bin` フォルダの中に
  **`ffmpeg.exe` があること**

これさえあればOKです。

---

## ステップ②：変換したい動画と ffmpeg.exe を同じ場所に置く

最初は **環境変数や難しい設定を一切やりません**。

1. 変換したい MP4 ファイル
   例：

   ```
   opening.mp4
   ```
2. `bin` フォルダにある

   ```
   ffmpeg.exe
   ```

この **2つを同じフォルダ** にコピーしてください。

フォルダの中身はこうなります：

```
video_conversion/
 ├ ffmpeg.exe
 └ opening.mp4
```

👉 これが **いちばん失敗しない構成**です。

---

## ステップ③：コマンドプロンプトを開く（ここ少しだけ頑張る）

1. さきほどの「動画変換」フォルダを開く
2. **ウインドウのアドレスバーをクリック**（上の方の💻こんな絵があるところの右隣）
3. そこに直接`cmd` と入力して **Enter**
すると、例の黒い画面（コマンドプロンプト）が開きます。

表示例：

```
C:\Users\あなたの名前\Desktop\video_conversion>
```

--- 

## ステップ④：いよいよ変換（コピペでOK）

以下を **そのままコピー＆ペースト** してください：

```
ffmpeg -i input.mp4 -c:v libvpx-vp9 -crf 32 -b:v 0 -c:a libopus output.webm
ffmpeg -i input.mov -c:v libvpx-vp9 -crf 32 -b:v 0 -c:a libopus output.webm
```

こちらは音を削除
```
ffmpeg -i input.mp4 -an -c:v libvpx-vp9 -crf 32 -b:v 0 -pix_fmt yuv420p output.webm
```
音を削除
-an
再生互換性
-pix_fmt yuv420p 

### 実行すると…

* 文字がバーッと流れます（正常です）
* 数秒〜数十秒待ちます
* フォルダに
  **`output.webm`** ができていたら成功 🎉

---

## ステップ⑤：できたか確認する

### ✔ 確認方法

* ダブルクリックで再生できるか
* 音が出るか

（Windows標準プレイヤーで再生できなくても
Ren’Pyでは問題なく再生できることがあります）

---

## よくあるつまずきポイント（安心してください）

### Q. `'ffmpeg' は内部コマンドではありません`

👉 **ffmpeg.exe と動画が同じフォルダにありません**

もう一度同じフォルダにあるか確認してください。

---

### Q. 変換が異常に遅い

👉 正常です。VP9は重いですが **安定度は最強**です。

---

### Q. 容量が大きい

👉 `-crf 36` にすると軽くなります（画質↓）

---

## Ren’Pyで使うときの置き場所（参考）

```
game/
 └ movies/
     └ opening.webm
```

再生例：

```renpy
$ renpy.movie_cutscene("movies/opening.webm")
```

---

## 結論から

> **はい、MOV → WEBM は FFmpeg で問題なく変換できます。**

しかも

* 品質も保てる
* 音ズレもしにくい
* 世界中で使われている方法

なので、胸を張ってOKです。

---

## ✅ まずは一番シンプルで安全な変換コマンド

### VP9 + Opus（おすすめ）

```bash
ffmpeg -i input.mov -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus output.webm
```

```bash
ffmpeg -i Timeline.mov -c:v libvpx-vp9 -crf 30 -b:v 0 -c:a libopus output.webm
```

### 日本語で意味を説明しますね

```text
-i input.mov        入力ファイル（今回のMOV）
-c:v libvpx-vp9     WEBM用の映像コーデック（高品質）
-crf 30             画質と容量のバランス（数値↓＝高画質）
-b:v 0              可変ビットレートにする指定
-c:a libopus         音声をOpus形式にする
output.webm         出力ファイル名
```

👉 **まずはこのままコピペでOK** です。

---

## 🎯 画質を少し変えたい場合（任意）

| 用途  | crf の目安 |
| --- | ------- |
| 高画質 | 24      |
| 標準  | 28〜30   |
| 軽量  | 33〜36   |

例（少し高画質）：

```bash
ffmpeg -i input.mov -c:v libvpx-vp9 -crf 24 -b:v 0 -c:a libopus output.webm
```

---

## 🔊 音声が不要な場合（さらに軽量）

```bash
ffmpeg -i input.mov -c:v libvpx-vp9 -crf 30 -b:v 0 -an output.webm
```

※ `-an` = audio none（音声なし）

---

## 🧠 もしトラブルが出たら（念のため）

* 変換が遅い → VP9は仕様です（正常）
* 音が出ない → プレイヤー側がWEBM非対応なだけのことあり
* サイズが大きい → `crf` を上げる（30→33）



