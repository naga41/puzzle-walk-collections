# Architecture & Technical Specifications

本ドキュメントは、「謎解き街歩きコレクション」のエンジン設計およびファイル構成の技術仕様です。
機能追加やデバッグを行う際は、このドキュメントを方針としてください。

## 1. 概念モデルとファイル構成
アプリは「エンジン（View Logic）」と「コンテンツ（Data & Assets）」が完全に分離されています。

- `/index.html`: 全てのシナリオを束ねるポータル画面。ペーパーUIベースで静的に記述。
- `/app.html`: メインエンジンを起動するエントリーポイント。
- `/core/`: アプリを動かす全ロジック。
  - `js/engine.js`: Vanilla JSのクラス（`PuzzleWalkEngine`）。
  - `css/style.css`: Noto Serif JP をベースとした「ペーパーUI」の共通スタイル。
- `/contents/[scenario-id]/`: 各シナリオの保有データ。
  - `scenario.json`: 全シナリオデータ、画像パス、テーマCSS変数を保持。
  - `assets/`: 各シナリオに必要な画像（プロップ）を格納。

## 2. `scenario.json` のスキーマ定義
`scenario.json` はエンジンに読み込まれ、動的にDOMを生成します。

```json
{
  "metadata": {
    "title": "シナリオ名",
    "prologue": ["プロローグ行1", "プロローグ行2"] // 中央に1行ずつフェードインさせる配列
  },
  "theme": {
    "--bg-base": "#...",      // ベースの背景色
    "--bg-texture": "url(...)", // ペーパー感などを出すノイズやテクスチャ
    "--text-main": "#...",    // ベースの文字色
    "--accent": "#..."        // ワンポイントのカラー（見出しや補足）
  },
  "chapters": [
    {
      "id": "1",
      "type": "briefing | challenge | final", // briefing=入力なし、challenge=キーワード入力、final=最後
      "title": "チャプターのタイトル",
      "monologue": "「斜体で表示される雰囲気テキスト」",
      "imageUrl": "contents/[id]/assets/foo.png", // 挿絵（乗算ブレンドされる）
      "imageCaption": "——画像のキャプション",
      "content": ["<p>メインの</p>", "<p>HTMLコンテンツ</p>"], // 配列でHTMLを記述
      "answerKeyword": "正解キーワード",
      "successMessage": "正解時のインラインメッセージ",
      "failureMessage": "不正解時のインラインメッセージ",
      "hint": "隠しヒントテキスト",
      "nextChapterId": "2" // 成功後にアンロックするID
    }
  ]
}
```

## 3. PWAとキャッシュに関する注意 (Service Worker)
- `sw.js` による強力な **Cache-First** 戦略を採用しています。
- ローカルでスクリプトやCSS、JSONを更新した場合、`Shift + Cmd + R` のスーパーリロードを行うか、開発者ツールの `Application > Storage > Clear site data` を実行しない限り、古いキャッシュが優先して読み込まれるため、デバッグ時にエラーと勘違いしないように気をつけてください。

## 4. UI/UX のデザインルール (Paper UI)
- CSSは `.card::after` や `mix-blend-mode: multiply`、`filter: sepia()` などを駆使して、「紙と滲んだインク」の質感を実現しています。
- 追加コンポーネント（アラートやボタン等）を作る場合は、色をベタ塗りせず、余白（マージン/パディング）と極細い線、薄いシャドウを使用して、活版印刷や書籍のようなトーンを維持すること。
