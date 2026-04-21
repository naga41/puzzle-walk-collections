import json

def chat_msg(side, name, msg):
    return f'<div class="chat-item {side}"><div class="chat-name">{name}</div><div class="chat-bubble">{msg}</div></div>'

def chat_container(msgs):
    return f'<div class="chat-container">{"".join(msgs)}</div>'

with open("contents/tokyo-rediscovery/scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Metadata / Prologue (Welcoming Intro)
data["metadata"]["prologue"] = [
    "「普段、何気なく歩いている東京の街……。」",
    "「でもその足元には、数え切れないほどの物語が地層のように重なっているんです。」",
    "「……おや、スマートフォンが何かを検知したようですね？」",
    "「これを開けば、100年前……都市を愛した建築家・葛城が遺した『記憶の層』へと繋がります。」",
    "「さあ、見慣れた景色の裏側に隠された、驚きの秘密を覗きに行きませんか？」"
]

# Chapter 0 (Briefing) - Gentle Intro
data["chapters"][0]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "こんにちは。1920年代の東京を愛した、建築家の葛城です。"),
        chat_msg("right", "ハチ", "あっ、ガイドの声……？ 初めまして！ 東京の歴史を探検できるって聞いてやってきました。"),
        chat_msg("left", "葛城", "ええ、面白いですよ。今のビル街の足元には、かつての運河や、震災の猛火を耐え抜いた人々の意志が今も眠っているんです。"),
        chat_msg("right", "ハチ", "ワクワクしますね！ 街歩きのポイントは、小さな違和感に気づくこと、でしょうか？"),
        chat_msg("left", "葛城", "その通り！ 実は東京駅の八重洲口……あそこはかつて、海と陸の境界線だったんです。"),
        chat_msg("left", "葛城", "まずは八重洲へ向かいましょう。なぜ地名が駅の反対側に移ってしまったのか……その謎から解き明かしていきましょう。")
    ])
]

# Chapter 1 (Yaesu) - Expanded Trivia
data["chapters"][1]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "さて、八重洲に着きましたね。今でこそオフィス街ですが、昔はここ、家康が名付けた『外堀』のすぐ外側だったんです。"),
        chat_msg("right", "ハチ", "へぇ〜！ じゃあ、ここを流れていたのはお堀の水だったんですね。"),
        chat_msg("left", "葛城", "そうなんです。実は『八重洲』という地名の元になったヨーステンさんの屋敷は、もともと駅の反対側（丸の内側）にあったんですよ。"),
        chat_msg("right", "ハチ", "えっ！？ じゃあ、どうして今こっち側が八重洲と呼ばれているんですか？"),
        chat_msg("left", "葛城", "明治時代に駅ができて、住所の整理が進むうちに、地名だけが駅を飛び越えてこっち側に定着しちゃったんです。不思議でしょう？"),
        chat_msg("left", "葛城", "では、一つ目の謎です。ヨーステンさんが乗ってきたリーフデ号。これ、出航した時はある学者の名で呼ばれていました。"),
        chat_msg("right", "ハチ", "船尾にその学者の像があったんですね。よし、記念碑を詳しく調べてみます！")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/vintage_dutch_ship_edo_sketch_1776780212937.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">（図：葛城のアーカイブより）出航当時の姿を描いた、人文学者の名を冠した船のスケッチ</p></div>'
]

# Chapter 2 (Nihonbashi) - 3x Expansion
data["chapters"][2]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "日本橋にやってきました。五街道の起点です。"),
        chat_msg("right", "ハチ", "歩道の脇に、不思議な形の街灯がありますね。あ、模様が『波』のデザインだ！"),
        chat_msg("left", "葛城", "おっ、よく気が付きましたね！ 実はこの辺りは江戸時代から水運の拠点でした。街灯の意匠一つにも、その歴史が刻まれているんです。"),
        chat_msg("left", "葛城", "そして、この橋そのもの。欄干を指で触ってみてください。少しザラついて、黒ずんでいる場所があるでしょう？"),
        chat_msg("right", "ハチ", "本当だ……これ、煤（すす）ですか？"),
        chat_msg("left", "葛城", "そう。1923年の関東大震災の猛火を、この橋が耐え抜いた証拠です。設計した妻木頼黄は、都市の不屈の意志をこの橋に込めたんです。"),
        chat_msg("right", "ハチ", "だから麒麟に『翼』があるんですね。日本の街が世界へ羽ばたくように……。"),
        chat_msg("left", "葛城", "ご名答！ では、その麒麟が抱えている盾を見てください。そこには、この街のアイデンティティを示す『三文字の名前』があるはずですよ。")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/nihonbashi_lion_crest_architectural_1776780237140.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">（資料）1923年の火災をも耐え抜いた、精緻な青銅の麒麟と盾の意匠</p></div>'
]

# Chapter 3 (Ningyocho) - Trivia Deep Dive
data["chapters"][3]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "人形町です。いい雰囲気でしょう？ でも実はここ、江戸の初期は広大な『湿地帯』だったんですよ。"),
        chat_msg("right", "ハチ", "えっ！ 今じゃこんなに賑やかな商店街なのに？"),
        chat_msg("left", "葛城", "そう。そこを埋め立てて、芝居小屋や遊郭が作られました。だから昔は火事がとても怖かったんです。"),
        chat_msg("right", "ハチ", "あ、だからからくり時計の櫓が『火消し』のデザインになっているんですね！"),
        chat_msg("left", "葛城", "その通り。この櫓に描かれている勇猛な男たちは、街の人々の憧れでした。"),
        chat_msg("left", "葛城", "実は、人形町の地名も、人形で生業を立てていた人たちが集まっていたことに由来しています。櫓に隠された『英雄の名』を探してみましょう。")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/edo_hikeshi_matoi_dramatic_1776780264280.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">（図）江戸の街を守り抜いた、勇敢な火消したちの誇り高き『纒』</p></div>'
]

# Chapter 4 (Kiyosu Bridge) - Architectural Secrets
data["chapters"][4]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "隅田川が見えてきました。そして、私の自信作……清洲橋です。"),
        chat_msg("right", "ハチ", "わぁ、本当に綺麗！ 西洋の吊り橋みたいですね。"),
        chat_msg("left", "葛城", "よく分かりましたね！ 実はこのデザイン、ドイツのケルンにあった橋がモデルになっているんです。"),
        chat_msg("right", "ハチ", "ケルンですか！ なぜわざわざドイツの橋を？"),
        chat_msg("left", "葛城", "隅田川の広い水面を美しく見せるためには、無骨な鉄骨よりも、優雅な曲線が必要だと思ったんです。当時の最先端の意匠ですよ。"),
        chat_msg("left", "葛城", "橋の袂に、この橋のモデルとなった美しい『ドイツの都市名』が刻まれています。歩いて探してみましょう！")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="contents/tokyo-rediscovery/assets/bridge.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">（図）隅田川の水面に映えるよう計算し尽くされた、清洲橋のシルエット</p></div>'
]

# Chapter 5 (Suitengu) - End with Trivia
data["chapters"][5]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "終着点、水天宮です。実はここ、江戸時代はお殿様（有馬家）の屋敷の中にあったんですよ。"),
        chat_msg("right", "ハチ", "えっ！ じゃあ一般の人は入れなかったんですか？"),
        chat_msg("left", "葛城", "ふふふ。毎月5日にだけお屋敷を開放したそうです。そこから『情け有馬の水天宮』という言葉が生まれたんですよ。"),
        chat_msg("right", "ハチ", "へぇ〜！ 人情味のある、素敵な歴史があるんですね。"),
        chat_msg("left", "葛城", "都市がどれだけ開発されても、こうした『命への慈しみ』は変わらない。最後は命を祝う場所で、葛城のアーカイブを結びましょう。"),
        chat_msg("left", "葛城", "境内の干支の円盤の中央。都市の源を象徴する最後の一文字、分かりますか？")
    ])
]

# Reward Expansion
reward = data["chapters"][5]["finalReward"]
reward["content"] = [
    chat_container([
        chat_msg("left", "葛城", "お疲れ様でした。君が今日歩いたその道、実はすべて『海』だったことが分かりましたか？"),
        chat_msg("right", "ハチ", "ええ……ヤン・ヨーステンの海、日本橋の運河……すべてが繋がった気がします。"),
        chat_msg("left", "葛城", "そう。100年前の幻の設計図は、今も君の足元で、静かに、でも力強く生き続けているんです。"),
        chat_msg("right", "ハチ", "明日からいつもの通勤路が、ちょっと違って見えそうです。"),
        chat_msg("left", "葛城", "それでいいんです。また、どこか街の角でお会いしましょう。さようなら！")
    ])
]

with open("contents/tokyo-rediscovery/scenario.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

