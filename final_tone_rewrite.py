import json

def chat_msg(side, name, msg):
    return f'<div class="chat-item {side}"><div class="chat-name">{name}</div><div class="chat-bubble">{msg}</div></div>'

def chat_container(msgs):
    return f'<div class="chat-container">{"".join(msgs)}</div>'

with open("contents/tokyo-rediscovery/scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Restore Prologue Background (removal of image path)
data["metadata"]["prologueImage"] = ""

# Update Prologue Dialogue (Natural Tone)
data["metadata"]["prologue"] = [
    "「……そこにいるのは、未来の観測者か？」",
    "「はい。あなたの遺したアーカイブを辿っています。あなたは……葛城さんですね？」",
    "「そうだ。1923年、私はこの都市の再生に命を懸けた。震災で失われた夢を、君に託したい。」",
    "「『水の設計図』……今、私の目の前にある風景に、あなたの記憶が重層的に響いています。」",
    "「嬉しい回答だ。さあ、スマートフォンを構えて。私と共に、東京の深層へと降りていこう。」"
]

# Chapter 0 (Briefing)
data["chapters"][0]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "このポータルを通じて、100年前の記憶を同期させる。まずは私が何故、この街に『水の楔』を遺したのかを知ってほしい。"),
        chat_msg("right", "ハチ", "東洋のヴェニス……。教科書で見た理想的な都市計画ですね。"),
        chat_msg("left", "葛城", "震災後の猛火の中で、私は悟ったのだ。都市とは強固な石の防壁ではない。水のように流動し、人々の記憶が堆積する有機体であるべきだとね。"),
        chat_msg("right", "ハチ", "その設計図が、今の街の地下にまだ生きているんですね。"),
        chat_msg("left", "葛城", "いかにも。復元の第一歩として、かつて潮の香りが満ちていた境界……<strong>『東京駅 八重洲中央口』</strong>へ向かってほしい。")
    ])
]

# Chapter 1 (Yaesu) - Image: vintage_dutch_ship_edo_sketch_1776780212937.png
data["chapters"][1]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "八重洲へようこそ。ここはかつて江戸城の外堀が海へと繋がる、もっとも生命力に満ちた水際だった。"),
        chat_msg("right", "ハチ", "今は高層ビルに囲まれていますが、目を閉じると波音が聞こえてきそうです。"),
        chat_msg("left", "葛城", "1600年、この国に流れ着いたヤン・ヨーステンの数奇な運命を思い出すといい。彼が乗ってきた『リーフデ号』だが……。"),
        chat_msg("right", "ハチ", "出航時の名前が違うんですよね。人文学者の名前を冠していたとか。"),
        chat_msg("left", "葛城", "そうだ。船尾に飾られたその人物の像に注目してほしい。そこに、最初の解読鍵が隠されている。")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/vintage_dutch_ship_edo_sketch_1776780212937.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">葛城がアーカイブに遺した、17thオランダ船の意匠スケッチ</p></div>'
]

# Chapter 2 (Nihonbashi) - Image: nihonbashi_lion_crest_architectural_1776780237140.png
data["chapters"][2]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "日本橋。ここは五街道の起点であり、都市の心臓部だ。石と青銅が織りなす威厳を見てくれ。"),
        chat_msg("right", "ハチ", "この麒麟の像、いつ見ても圧倒されます。翼のデザインが本当に繊細ですね。"),
        chat_msg("left", "葛城", "設計者の妻木頼黄が込めた『日本の中心から世界へ羽ばたく』という意志。震災を耐え抜いたこの橋は、都市の不屈の象徴なのだ。"),
        chat_msg("right", "ハチ", "あ、麒麟が抱えている盾……。そこに文字が刻まれていますね。"),
        chat_msg("left", "葛城", "それがこの街の誇り高き名前だ。<strong>『三文字の名前』</strong>を正確に観測してほしい。")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/nihonbashi_lion_crest_architectural_1776780237140.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">妻木頼黄が考案した、獅子と市章の装飾的なディテール</p></div>'
]

# Chapter 3 (Ningyocho) - Image: edo_hikeshi_matoi_dramatic_1776780264280.png
data["chapters"][3]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "人形町……。ここは江戸の熱気が未だに地面の下で脈動している稀有な場所だ。"),
        chat_msg("right", "ハチ", "二つのからくり櫓が、街の時間を見守っていますね。"),
        chat_msg("left", "葛城", "私は設計図にこう記した。『人の祭りや熱気のリズムがなければ、街はただの抜け殻だ』。特に、火に立ち向かった者たちの誇りを忘れてはならない。"),
        chat_msg("right", "ハチ", "櫓の幕に書かれた名前……。彼らがこの街の不屈の魂の正体なんですね。"),
        chat_msg("left", "葛城", "その通りだ。伝統的な火消しの呼称を特定してほしい。")
    ]),
    f'<div style="margin: 20px -20px; text-align:center;"><img src="artifacts/edo_hikeshi_matoi_dramatic_1776780264280.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">不屈の精神を象徴する、江戸町火消の纒（まとい）のイメージ</p></div>'
]

# Chapter 4 (Kiyosu Bridge) - Image: contents/tokyo-rediscovery/assets/bridge.png
data["chapters"][4]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "隅田川。私の理想の結実の一つである清洲橋が見えてきた。"),
        chat_msg("right", "ハチ", "この曲線……鉄の重厚さと、水の優雅さが完璧に調和しています。"),
        chat_msg("left", "葛城", "私がドイツで惚れ込んだ吊り橋の形式……それをこの東京に再現したかった。モデルとなったのは、あの歴史あるドイツの都市だ。"),
        chat_msg("right", "ハチ", "『〇〇〇の眺め』として有名なあの場所……。あなたが東京に重ねた幻ですね。"),
        chat_msg("left", "葛城", "そうだ。その都市の名を観測することで、設計図は完成に近づく。")
    ]),
     f'<div style="margin: 20px -20px; text-align:center;"><img src="contents/tokyo-rediscovery/assets/bridge.png" style="width:100%; box-shadow: 0 4px 20px rgba(0,0,0,0.2);"><p style="font-size:0.8rem; color:var(--accent); margin-top:10px;">1928年に完成した、自碇式吊橋の美しいサイドビュー</p></div>'
]


with open("contents/tokyo-rediscovery/scenario.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Final Professional Tone Rewrite with New Visuals completed.")
