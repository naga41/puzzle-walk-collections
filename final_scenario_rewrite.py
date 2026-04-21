import json

def chat_msg(side, name, msg):
    return f'<div class="chat-item {side}"><div class="chat-name">{name}</div><div class="chat-bubble">{msg}</div></div>'

def chat_container(msgs):
    return f'<div class="chat-container">{"".join(msgs)}</div>'

with open("contents/tokyo-rediscovery/scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Metadata / Prologue
data["metadata"]["prologue"] = [
    "「……誰か、そこにいるのか？」",
    "「えっ、スマホから声が……？ 誰ですか、あなたは。」",
    "「私は葛城。1923年、この都市の『未来』を設計しようとした男だ。」",
    "「葛城……！ 名前だけは聞いたことがあります。震災の猛火の中で、幻の設計図を遺したという建築家……。」",
    "「いかにも。さあ、私のアーカイブを同期させよう。君の歩みとともに、この街の『真実の輪郭』を復元するんだ。」"
]

# Chapter 0 (Briefing)
data["chapters"][0]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "君が手にしているその端末……それが私の設計図と共鳴している。まずは私の設計思想を理解してほしい。"),
        chat_msg("right", "ハチ", "設計思想……『東洋のヴェニス』にしようとしていたって話、本当なんですね。"),
        chat_msg("left", "葛城", "ああ。大震災で街が焼けた時、私は絶望したが、同時に確信した。都市は石の檻ではない。水が流れ、記憶が重なる生き物なのだ。"),
        chat_msg("right", "ハチ", "だから、街の随所に未来の私たちが気づくような『楔（くさび）』を遺したと。"),
        chat_msg("left", "葛城", "その通り。私の記録は断片化されているが、特定の場所へ赴くことで復元できる。"),
        chat_msg("left", "葛城", "まずは、かつて『海』と『陸』の境界であった場所……<strong>『東京駅 八重洲中央口（地上）』</strong>へ向かってくれ。そこが旅の出発点だ。")
    ])
]
data["chapters"][0]["instruction"] = "東京駅 八重洲中央口（地上出口）へ向かい、旅の準備を整えよ。"

# Chapter 1 (Yaesu)
data["chapters"][1]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "着いたか。ここが八重洲だ。家康の時代、この辺りはすべて豊かな水を湛えた『海』だった。"),
        chat_msg("right", "ハチ", "信じられない。今は見渡す限りのビル街なのに。"),
        chat_msg("left", "葛城", "地名の由来となったヤン・ヨーステン……耶揚子という名をもらったオランダ人も、この海の広さに故郷を重ねたのだろう。"),
        chat_msg("left", "葛城", "彼は1600年、リーフデ号という一艘の船でこの国へ流れ着いた。だが、その船には出航当初、別の名が冠されていたのだ。"),
        chat_msg("right", "ハチ", "別の名……？ 船尾にその人物の像が飾られていたという、あの学者の名ですね。"),
        chat_msg("left", "葛城", "いかにも。八重洲通りの記念碑、あるいは地下街にある彼の像を観測してほしい。そこに刻まれた『人文学者の名』こそが、最初の解読鍵だ。")
    ])
]
data["chapters"][1]["instruction"] = "八重洲通りの記念碑、または地下街の像を調査し、リーフデ号の旧名（人文学者の名）を特定せよ。"

# Chapter 2 (Nihonbashi)
data["chapters"][2]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "日本橋……。お江戸のヘソであり、五街道の起点。ここはまさに都市の心臓だ。"),
        chat_msg("right", "ハチ", "この橋、何度見ても重厚で美しいですね。麒麟や獅子の像が誇らしげです。"),
        chat_msg("left", "葛城", "設計した妻木頼黄は、私の師匠筋にあたる男だ。彼は西洋のバロック様式に日本の伝統を融合させ、とてつもない芸術品を創り上げた。"),
        chat_msg("left", "葛城", "欄干の黒ずみを見てごらん。100年前の震災の業火を、この橋は耐え抜いたのだ。都市の不屈の意志がここにある。"),
        chat_msg("right", "ハチ", "麒麟の像が翼を広げてますね。日本の中心から世界へ羽ばたく象徴……。"),
        chat_msg("left", "葛城", "その麒麟が抱えている盾に注目してほしい。そこには、この街の誇りを示す<strong>『三文字の名前』</strong>が刻まれているはずだ。")
    ])
]
data["chapters"][2]["instruction"] = "麒麟像が抱える盾を詳細に観測し、そこに刻まれた『都市の名（三文字）』を特定せよ。"

# Chapter 3 (Ningyocho)
data["chapters"][3]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "人形町。江戸の情緒が服を着て歩いているような街だ。吉原の熱気と芝居小屋の賑わいが、今もこの空気には混ざっている。"),
        chat_msg("right", "ハチ", "からくり時計の櫓（やぐら）が見えます！ 二つ並んで立っているんですね。"),
        chat_msg("left", "葛城", "私は設計図にこう記した。『ただ綺麗なハコを作っても街は死ぬ。住む人の祭りと熱気、そのリズムを同期させろ』と。"),
        chat_msg("left", "葛城", "特に、江戸の暮らしを守り続けた男たちの誇りを忘れてはならない。大正の震災時、この街の人々は手を取り合って延焼を防いだのだ。"),
        chat_msg("right", "ハチ", "あ、このチャットに出ている『職業』の連中のことですね。櫓の幕にもはっきりと名前が……！"),
        chat_msg("left", "葛城", "いかにも。彼らの精神こそが、この街を何度でも蘇らせる。その職業の名を特定できるか。")
    ])
]
data["chapters"][3]["instruction"] = "人形町通りの『からくり櫓』を調査し、江戸の街を火から守った勇猛な職業の名を特定せよ。"

# Chapter 4 (Kiyosu Bridge)
data["chapters"][4]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "隅田川……。かつて『震災復興の華』と呼ばれた橋が見えてきた。清洲橋だ。"),
        chat_msg("right", "ハチ", "なんて優美な曲線なんだ……。鉄の橋なのに、どこか柔らかさを感じます。"),
        chat_msg("left", "葛城", "私がドイツで見た夢を、ここに具現化したのだよ。当時、世界一美しいと言われたケルン川の吊り橋をモデルにした。"),
        chat_msg("left", "葛城", "単に渡るための道具ではない。水辺の景観を祝福し、都市に品格を与えるための祈念碑なのだ、これは。"),
        chat_msg("right", "ハチ", "『〇〇〇の眺め』として知られるその都市……。葛城さんが東京に重ねた幻の影ですね。"),
        chat_msg("left", "葛城", "その通りだ。私の魂を震わせたそのドイツの都市名を、君の観測で確定させてほしい。")
    ])
]
data["chapters"][4]["instruction"] = "清洲橋のたもと、または案内板を調査し、そのモデルとなったドイツの都市名を特定せよ。"

# Chapter 5 (Suitengu)
data["chapters"][5]["content"] = [
    chat_container([
        chat_msg("left", "葛城", "ついに終着地点、水天宮だ。私の旅も、君の観測も、最後はここに戻り着く。"),
        chat_msg("right", "ハチ", "有馬家が江戸の人々に開放したという『情け有馬』の水天宮。慈悲の心に満ちた場所ですね。"),
        chat_msg("left", "葛城", "どんなに巨大な都市を作ろうと、最後は『命への祈り』がなければ空虚な石積みだ。"),
        chat_msg("left", "葛城", "この街の底流には、常に水の力が流れている。海から始まり、祈りの水へと還る。"),
        chat_msg("right", "ハチ", "あ、境内の『子宝いぬ』の周りに、干支を記した円盤があります。"),
        chat_msg("left", "葛城", "その円盤のど真ん中を、心で見てごらん。都市の源であり、葛城が死ぬまで守ろうとした『幻の水都』を象徴する、最後の一文字があるはずだ。")
    ])
]
data["chapters"][5]["instruction"] = "水天宮境内の『子宝いぬ』の台座を詳細に観測し、中央に刻まれた『最後の一文字』を特定せよ。"

# Reward (Dialogue Expansion)
reward = data["chapters"][5]["finalReward"]
reward["content"] = [
    chat_container([
        chat_msg("left", "葛城", "……見事だ。君のおかげで、私の『水の設計図』は100年の時を超え、現代の君の眼差しの中に復元された。"),
        chat_msg("right", "ハチ", "葛城さん、あなたの歩いた軌跡を地図に重ねてみました。……嘘だろ、道が一本もない！"),
        chat_msg("left", "葛城", "ははは。全部『海』だよ。今、君が立っているその場所も、かつては波が揺れていたのだ。"),
        chat_msg("right", "ハチ", "僕たちは、100年前の海の上を歩いていたのか……。"),
        chat_msg("left", "葛城", "この街は今も、海の上に浮かぶ一時の幻。だがその幻を愛おしむ君のような観測者がいる限り、東京は何度でも水の都として輝き続ける。……さらばだ、若き友よ。")
    ])
]

with open("contents/tokyo-rediscovery/scenario.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Katsuragi-Personified 3x Expanded Dialogue Rewrite logic completed.")
