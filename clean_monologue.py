import json

with open("contents/tokyo-rediscovery/scenario.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Chapter 0
data["chapters"][0]["monologue"] = "「100年前の記憶を呼び覚まそう。私の設計した未来は、まだこの地下に、たしかに息づいている。」"

# Chapter 1
data["chapters"][1]["monologue"] = "「八重洲……。かつての水の境界線。この喧騒の下に眠る、一艘の漂流船の記憶を探ってほしい。」"

# Chapter 2
data["chapters"][2]["monologue"] = "「日本橋。ここは都市の意志が凝縮された場所だ。震災の業火さえも、この石と青銅の誇りを焼き払うことはできなかった。」"

# Chapter 3
data["chapters"][3]["monologue"] = "「人形町。この街の細い路地には、江戸から続く人々の熱気が堆積している。火を恐れず、火と共に生きた男たちの矜持を見せてやろう。」"

# Chapter 4
data["chapters"][4]["monologue"] = "「清洲橋。鋼鉄で描かれた優美な曲線は、私が東京に重ねた幻の影だ。水面に映るその残像を追ってほしい。」"

# Chapter 5
data["chapters"][5]["monologue"] = "「水天宮。安らぎと祈りの場所。海に始まり、祈りの水に還る……。この旅も、ようやく最深部へと辿り着いたようだ。」"

with open("contents/tokyo-rediscovery/scenario.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

