import json

with open("contents/tokyo-rediscovery/scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Metadata / Prologue
data["metadata"]["prologue"] = [
    "1923年。ひとりの建築家が遺した、一篇の手記がある。",
    "そこには、震災によって失われた『水都』の理想が、静かな言葉で綴られていた。",
    "あなたが今歩いているこの街の底には、その記憶が、今も形を変えて息づいている。",
    "——これは、都市の『失われた時間』を静かに辿る、思索の旅である。"
]

# Chapter 0: Briefing
ch0 = data["chapters"][0]
ch0["title"] = "建築家の遺録"
ch0["imageUrl"] = "contents/tokyo-rediscovery/assets/blueprint_final.png"
ch0["imageCaption"] = "葛城が遺した、1923年当時の都市計画の青写真"
ch0["content"] = [
    "<p>建築家・葛城は、関東大震災の直前まで、この東京を『水と人が共生する都市』へと再編する計画に没頭していました。しかし、その夢は火災と近代化の波に飲まれ、公の記録からは跡形もなく消え去りました。</p>",
    "<p style=\"margin: 25px 15px; font-size:0.9rem; color:#736050; line-height:1.8; border-left: 2px solid var(--border); padding-left:15px;\">『都市とは、ただの石やコンクリートの集積ではない。それは記憶の層が重なり、水の如く流動し続ける有機体であるべきだ。私はその理想を、街の細部に微かな影として投影しておくことにした。』</p>",
    "<p>彼の遺した言葉が、今も街の至る所に『静かな違和感』として残っています。私たちは、その断片をひとつずつ拾い集め、彼が守ろうとした都市の輪郭を確かめる必要があります。</p>"
]
ch0["successMessage"] = "手記の最初の頁が、静かに開かれた。"
ch0["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【次なる地点への導き】</strong>東京駅・八重洲口方面へ向かってください。まずは都市の玄関口、かつての水の境界線へと足を運びましょう。<br><a href=\"https://www.google.com/maps/search/?api=1&query=東京駅+八重洲中央口\" target=\"_blank\" style=\"color:#3e3124; text-decoration:underline;\">地図で確認する</a></div>"

# Chapter 1: Yaesu
ch1 = data["chapters"][1]
ch1["title"] = "境界の記録"
ch1["imageUrl"] = "contents/tokyo-rediscovery/assets/ship.png"
ch1["monologue"] = "「1600年、漂着した一艘の船がこの地に新たな時間を持ち込んだ。八重洲という名は、異国の航海士がこの地に根を下ろした証だ。かつてここは江戸城の外堀が流れ、波打ち際と陸地の境界であった。私は、この境界線こそが都市の成長の起点であると考え、ある名前を記録の中に伏せておいた。それは、彼が日本へ至るまでの苦難を共にした船の、真の名前だ。」"
ch1["content"] = [
    "<p>東京駅周辺の『八重洲』という地名。かつてここは、江戸城の外堀が豊かな水を湛えていた場所です。この名の由来となったヤン・ヨーステンが漂流の末に辿り着いた船『リーフデ号』。その船には、オランダを出航した際の<strong>『以前の名前』</strong>がありました。</p>",
    "<p>八重洲通りにある記念碑、あるいは八重洲地下街にある彼の像を訪ねてください。建築家・葛城が都市の起点として重視したその名前、人文学者の名に由来するその文字を特定してください。</p>"
]
ch1["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【史実アーカイブ】</strong>船の名前は『エラスムス号』。人文学者デジデリウス・エラスムスにちなんだものです。<br><hr style=\"border:none; border-top:1px dashed var(--border); margin:15px 0;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【次なる地点への導き】</strong>八重洲通りを東へ、日本橋方面へ進んでください。約10分、かつての運河の跡を感じながら、麒麟の像が立つ石造りの橋を目指します。<br><a href=\"https://www.google.com/maps/search/?api=1&query=日本橋+麒麟像\" target=\"_blank\" style=\"color:#3e3124; text-decoration:underline;\">地図で確認する</a></div>"

# Chapter 2: Nihonbashi
ch2 = data["chapters"][2]
ch2["title"] = "心室の守護"
ch2["imageUrl"] = "contents/tokyo-rediscovery/assets/kirin.png"
ch2["monologue"] = "「日本橋。五街道の起点。都市の心室。1923年の火災の際も、人々はこの橋の尊厳を守り抜いた。私は、この橋に施された装飾、とりわけ翼を持つ獣の力強さに魅せられた。それは単なる飾りではなく、再生を誓う都市の意志の現れだ。彼が抱える盾には、現在もこの地がどこへ属しているかを示す印が刻まれている。それを見落としてはならない。」"
ch2["content"] = [
    "<p>日本橋の中央、日本の道路の出発点である『日本国道路元標』の傍ら。そこに立つ『麒麟像』を仰ぎ見てください。建築家・葛城は、この像の放つ再生への意志に深く共感し、その細部に注目しました。</p>",
    "<p>麒麟がその手で固く押さえている盾。そこには、この地がいまどこに属しているかを示す『紋章（文字）』が含まれています。その盾に刻まれた印を特定してください。</p>"
]
ch2["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【史実アーカイブ】</strong>その紋章は『東京都（当時は東京市）』のものです。麒麟が東京の繁栄を守っている姿を現しています。<br><hr style=\"border:none; border-top:1px dashed var(--border); margin:15px 0;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【次なる地点への導き】</strong>橋を渡り、人形町方面へ向かってください。徒歩約15分。歴史ある街並みが残るエリアへ、かつてこの橋を渡ったであろう多くの旅人たちの足跡を辿るように進みます。<br><a href=\"https://www.google.com/maps/search/?api=1&query=人形町+からくり櫓\" target=\"_blank\" style=\"color:#3e3124; text-decoration:underline;\">地図で確認する</a></div>"

# Chapter 3: Ningyocho
ch3 = data["chapters"][3]
ch3["title"] = "営みの同期"
ch3["imageUrl"] = "contents/tokyo-rediscovery/assets/clocks_sketch.png"
ch3["monologue"] = "「人形町。ここには、近代的な変化に抗うような、古き良き江戸の営みのリズムが残っている。私はかつて、この街の至る所に火災への備えと、人々の熱気が同居していることに驚かされた。時計の櫓（やぐら）が刻んでいるのは、単なる時間ではない。この街を守り続けてきた者たちの誇り、その継続性だ。」"
ch3["content"] = [
    "<p>人形町通りに立つ、2つの『からくり櫓』。それぞれがこの街の歴史的な役割を象徴しています。建築家・葛城は、都市の機能美だけでなく、そこで暮らす人々の生活のリズムを保存しようと考えました。</p>",
    "<p>江戸の街を火災から守り続けてきた者たちを模した櫓の前に立ち、彼らを指すその『総称』を導き出してください。幕や案内板に、彼らの名前が刻まれているはずです。</p>"
]
ch3["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【史実アーカイブ】</strong>答えは『火消し』。江戸情緒をいまに伝えるシンボルです。<br><hr style=\"border:none; border-top:1px dashed var(--border); margin:15px 0;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【次なる地点への導き】</strong>甘酒横丁を抜け、隅田川の河畔を目指して東へ歩いてください。徒歩10分ほどで、川面に映える青い吊り橋が見えてきます。<br><a href=\"https://www.google.com/maps/search/?api=1&query=清洲橋\" target=\"_blank\" style=\"color:#3e3124; text-decoration:underline;\">地図で確認する</a></div>"

# Chapter 4: Kiyosu Bridge
ch4 = data["chapters"][4]
ch4["title"] = "水面の投影"
ch4["imageUrl"] = "contents/tokyo-rediscovery/assets/bridge.png"
ch4["monologue"] = "「1923年。瓦礫の山となった隅田川の岸辺で、私は誓った。再びこの川に、世界で最も美しいと讃えられる橋の姿を描き出すと。それはドイツの古都で見た、あの優美な吊り橋の記憶の投影だった。橋とは単なる移動の手段ではなく、向こう岸という『未来』への架け橋なのだ。」"
ch4["content"] = [
    "<p>隅田川のテラスに佇み、目の前の『清洲橋（きよすばし）』を見つめてください。建築家・葛城が、戦後復興の希望を込めて、当時の世界で最も美しいと言われたドイツの橋をモデルとして架けさせました。</p>",
    "<p>その設計のインスピレーションの元となった、ドイツの<strong>『ある都市の名前』</strong>を特定してください。その名を刻むことで、かつて葛城が見た風景が、あなたの目の前の景色と重なり合います。</p>"
]
ch4["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【史実アーカイブ】</strong>モデルとなったのは『ケルン』市にかつてあった大吊り橋です。<br><hr style=\"border:none; border-top:1px dashed var(--border); margin:15px 0;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【次なる地点への導き】</strong>清洲橋の青い姿を背に、最後は『水天宮』へと足を戻しましょう。この思索の旅の終着点は、命と水が交差する聖域です。<br><a href=\"https://www.google.com/maps/search/?api=1&query=水天宮\" target=\"_blank\" style=\"color:#3e3124; text-decoration:underline;\">地図で確認する</a></div>"

# Chapter 5: Final
ch5 = data["chapters"][5]
ch5["title"] = "源流の記憶"
ch5["imageUrl"] = "contents/tokyo-rediscovery/assets/suitengu_dog.png"
ch5["imageCaption"] = "建築家の旅の終点、命と水が重なり合う瞬間"
ch5["monologue"] = "「手記の最後を記す。すべての地点を繋ぎ終えたとき、あなたは何が見えているだろうか。私は最期の瞬間にまで、この都市の根底にある水の清らかさを信じていた。命の始まり、そして終わり。水天宮に刻まれた最後の一文字に、私の理想のすべてを込めることにする。」"
ch5["content"] = [
    "<p>今回の思索の旅の終着地点、水天宮。ここは人々の『安産』や『安全』を長きにわたり見守り続けてきた場所です。境内にある『子宝いぬ』の周囲にある円盤を、最後にもう一度、静かに観測してください。</p>",
    "<p>円盤の中心、母犬の足元に刻まれた<strong>『最後の一文字』</strong>は何でしょうか。それこそが、葛城が最も守り抜くべきと説いた、この都市の源流を象徴する言葉です。</p>"
]
ch5["postSolveHTML"] = "<div style=\"margin-top: 30px; font-size: 0.85rem; border: 1px solid var(--border); padding: 20px; border-radius: 4px; background: rgba(0,0,0,0.02); line-height:2;\"><strong style=\"color: var(--accent); display:block; margin-bottom:10px;\">【史実アーカイブ】</strong>答えは『水』。水天宮はその名の通り水と深く関わる歴史を持っています。</div>"

with open("contents/tokyo-rediscovery/scenario.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Professional Architect scenario rewrite completed.")
