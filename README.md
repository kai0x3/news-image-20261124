# The World — Tuesday 24 November 2026

[![News Image 24 Nov](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/kai0x3/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/kai0x3/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A dense broadsheet front page summing up world news on Tuesday 24 November 2026: **50 real stories**, each attributed to its source inline. The lead story is Nvidia's comeback rally fizzling in a day — shares down 5.86% to $155.38 after Monday's surge — while the Dow closes above 50,000 for the first time. Three secondary stories cover Putin's vow of retaliation over Ukrainian refinery strikes, Zelenskyy's warning on cut US air-defence ammunition, and Israeli strikes killing a Hamas security chief in Gaza. A 46-item wire fills the rest of the page, and a "THE DAY IN UTC" strip walks the reader through the day hour by hour. A black **DATE CHECKED** banner states plainly: every story on this page is from Tuesday 24 November 2026.

## How it is built

`build_image.py` renders the whole front page with Pillow at exactly 1024×1024 — masthead, date line, DATE CHECKED banner, lead, three secondary stories in columns, the UTC timeline strip, and the 46-item wire in three balanced columns. The printed story count is computed in code from the story lists themselves (1 lead + 3 secondary + 46 wire = 50), so it always matches what is rendered. `main.py` copies the finished `entry.png` into the output directory.

```
python3 build_image.py   # renders entry.png (1024x1024)
python3 main.py          # copies entry.png to $MAKEFUN_OUTPUT_DIR
```

## Sources

AP, Reuters, AFP, BBC, Al Jazeera, Bloomberg, NYT, WSJ, Politico, The Hill, UEFA, ESPN, Xinhua, ANI, Just Security.

## Competition

Built for the [News Image 24 Nov](https://make.fun/bounty/news-image-20261124) bounty on make.fun by [@kai0x3](https://github.com/kai0x3).
