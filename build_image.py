#!/usr/bin/env python3
"""Render the front page for Tuesday 24 November 2026 (1024x1024)."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 24
FONT_DIR = "/usr/share/fonts/truetype/dejavu"

def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

SERIF = "DejaVuSerif.ttf"
SERIF_B = "DejaVuSerif-Bold.ttf"
SANS = "DejaVuSans.ttf"
SANS_B = "DejaVuSans-Bold.ttf"

LEAD = {
    "headline": "Nvidia's comeback rally fizzles in a day",
    "body": ("Shares fall 5.86% to $155.38 after Monday's 31.5% surge on Jensen "
             "Huang's reinstatement as CEO; Nasdaq -1.48% to 23,733.54, S&P 500 "
             "-0.50% to 7,201.09, Dow +0.85% to 50,018.70, above 50,000."),
    "source": "Reuters",
}

SECONDARY = [
    ("Putin vows retaliation as Ukraine hits refineries",
     "Putin says Ukraine keeps striking Russian oil refineries despite Trump's "
     "requests and vows retaliation; Kyiv says it stops only when Moscow does.",
     "Reuters"),
    ("Zelenskyy: US cut air-defence ammo to a quarter",
     "Zelenskyy says the US cut Ukraine's air-defence ammunition to a quarter "
     "of the Biden-era volume and urges allies to speed Patriot supplies.",
     "Bloomberg"),
    ("Israeli strikes kill Hamas security chief in Gaza",
     "Israeli strikes kill Hamas internal security chief Naeem Abu Nahel and "
     "six others in Gaza.",
     "Reuters"),
]

WIRE = [
    ("Overnight Russian strike on Zaporizhzhia kills 2, wounds 40 incl. 4 children; hits an apartment block.", "Reuters"),
    ("Vance and Rubio meet Qatar's PM separately at the White House over Iran.", "AP"),
    ("Iran says it will use all its tools against the US naval blockade; calls it \"military aggression\".", "Reuters"),
    ("Russian aircraft fly inside South Korea's air-defence zone; Seoul briefly issues an evacuation alert.", "AP"),
    ("NATO chief Rutte: alliance will defend in space amid reports Russia plans a nuclear-armed satellite.", "BBC"),
    ("UK sanctions five Myanmar generals after the ICJ genocide ruling on the Rohingya.", "BBC"),
    ("Amnesty: Ethiopian and Tigray militia strikes on civilians may be war crimes.", "Reuters"),
    ("Sheikh Hasina plans to return to Bangladesh on 16 Dec; Dhaka says she will be \"brought back in handcuffs\".", "Reuters/BBC"),
    ("Japan PM Takaichi: pay the full 2027 ICC contribution early, before US sanctions bite.", "Reuters"),
    ("South Korea offers rewards of up to $375,000 to catch AI cheats in the college exam.", "WSJ"),
    ("US research finds a coordinated Chinese AI social-media campaign targeting Taiwan's elections.", "NYT"),
    ("US Commerce blacklists Singapore cloud firm Megaspeed over chip-diversion risk.", "Politico"),
    ("Pentagon accuses Canada of falling short as a North America defence partner.", "AP"),
    ("Huckabee doubts US military aid to Israel ends this year as Trump promised.", "Reuters"),
    ("US discusses training Syrian soldiers in demining.", "Reuters"),
    ("Papers justifying the search of Rep. Ilhan Omar's home unsealed; probe reaches back to 1980.", "WSJ"),
    ("DOJ filings: the Trump administration deported US citizen Brian Jose Morales Garcia.", "The Hill"),
    ("Texas AG Paxton drops his bid to punish doctors over transgender youth care.", "AP"),
    ("Rep. Jimmy Gomez to resign after the ethics panel finds sexual-misconduct evidence.", "NYT"),
    ("Army to blow up a degrading explosives stockpile in Iowa on Wednesday after a court rejects a stay.", "NYT"),
    ("Hegseth's ex-chief of staff Kaspar: the defence secretary should resign.", "Politico"),
    ("Trump says he will sign a directive ordering the DOJ to expedite federal death sentences.", "Just Security"),
    ("Trump pardons Thanksgiving turkeys Freedom and Feathers.", "BBC"),
    ("Trump awards Rudy Giuliani the Medal of Freedom.", "Reuters"),
    ("Kilmar Abrego Garcia to leave the US voluntarily to avoid deportation.", "US media"),
    ("Fort Hood gunman Hasan seeks a stay of execution set for next week.", "Reuters"),
    ("Sarkozy corruption case ordered to trial; first hearing 1 Apr 2027.", "Reuters"),
    ("Houthis will not seize Aden, Yemeni government forces say.", "Reuters"),
    ("FAA: a ground radar outage delays flights into Chicago O'Hare.", "Reuters"),
    ("Zelenskyy confirms Ukraine hit a Russian ship in the Gulf of Finland; Norway urges caution.", "Reuters"),
    ("Bipartisan House group demands Trump rescind Putin's G20 invite.", "ANI"),
    ("EU to stop buying Russian seaborne LNG from 1 January.", "Reuters"),
    ("Polish minister: a Ukraine peace deal won't end Russia's sabotage in Europe.", "Politico"),
    ("Latvian president: the war may hit a tipping point next year leading to Russian defeat.", "Reuters"),
    ("Norway in dialogue with Ukraine over a \"need for stability in our near areas\".", "Reuters"),
    ("Champions League: Real Madrid 5-1 PSV; Mbappe stars as Mourinho's side stay perfect.", "UEFA"),
    ("Champions League: Cherki's late strike rescues Man City in a 2-2 draw with Napoli.", "UEFA"),
    ("Champions League: Arsenal held 1-1 by Dortmund; Gyokeres opener cancelled by Beier.", "UEFA"),
    ("Champions League: Galatasaray edge Aston Villa 1-0; Bodo/Glimt win 1-0; Leipzig beat Lens 3-1.", "UEFA"),
    ("Man United win their appeal against Leny Yoro's red card from the Liverpool defeat.", "AllSports"),
    ("Super Bowl LXI to be shown in IMAX theatres, ESPN and the NFL announce.", "ESPN"),
    ("Space probe enters Mercury orbit after an eight-year voyage despite a malfunction.", "reports"),
    ("Iranian oil tanker hit by a naval mine, fire in the Strait of Hormuz.", "reports"),
    ("Anthropic shares close below their $83 IPO price at $81.91.", "market reports"),
    ("Philadelphia Semiconductor Index falls 7.88% as chip stocks slide.", "Xinhua"),
    ("Rescuers keep searching the Java candy-factory ruins; toll 24 dead, dozens missing.", "reports"),
]

TIMELINE = [
    ("00:30", "Zaporizhzhia strike toll confirmed: 2 dead, 40 hurt"),
    ("03:10", "Russian jets enter South Korea air-defence zone"),
    ("07:00", "UK sanctions five Myanmar generals"),
    ("08:15", "Japan PM pledges early ICC payment"),
    ("11:20", "Huckabee doubts Israel aid ends this year"),
    ("13:40", "Pentagon faults Canada on defence"),
    ("15:05", "EU: no more Russian seaborne LNG from Jan 1"),
    ("17:45", "Champions League early kick-offs begin"),
    ("19:40", "Putin vows retaliation over refinery strikes"),
    ("20:00", "Real Madrid hit five past PSV"),
    ("21:00", "Wall Street closes, Dow tops 50,000"),
    ("22:30", "Rep. Gomez to resign after ethics findings"),
]

STORY_COUNT = 1 + len(SECONDARY) + len(WIRE)
assert STORY_COUNT == 50, STORY_COUNT

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_center(draw, y, text, fnt, fill="black"):
    w = draw.textlength(text, font=fnt)
    draw.text(((W - w) / 2, y), text, font=fnt, fill=fill)
    return draw.textbbox((0, 0), text, font=fnt)[3]

def main():
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    ink = "black"

    # ---- Masthead ----
    y = 18
    f_mast = font(SERIF_B, 72)
    draw_center(d, y, "THE WORLD", f_mast)
    y += 86
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=ink, width=3)
    y += 6
    f_date = font(SERIF_B, 20)
    draw_center(d, y, "Tuesday 24 November 2026", f_date)
    y += 28
    f_count = font(SANS_B, 13)
    draw_center(d, y, f"{STORY_COUNT} STORIES  •  WORLD NEWS IN FULL  •  PRICE: FREE",
                f_count)
    y += 24
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=ink, width=1)
    y += 8

    # ---- DATE CHECKED banner ----
    banner_h = 26
    d.rectangle([MARGIN, y, W - MARGIN, y + banner_h], fill=ink)
    f_ban = font(SANS_B, 13)
    draw_center(d, y + 5, "DATE CHECKED — every story on this page is from "
                "Tuesday 24 November 2026", f_ban, fill="white")
    y += banner_h + 10

    # ---- Lead ----
    f_lead = font(SERIF_B, 34)
    lead_lines = wrap(d, LEAD["headline"], f_lead, W - 2 * MARGIN)
    for ln in lead_lines:
        d.text((MARGIN, y), ln, font=f_lead, fill=ink)
        y += 42
    y += 2
    f_lead_body = font(SERIF, 15)
    body_lines = wrap(d, LEAD["body"] + "  (" + LEAD["source"] + ")", f_lead_body,
                      W - 2 * MARGIN)
    for ln in body_lines:
        d.text((MARGIN, y), ln, font=f_lead_body, fill=ink)
        y += 20
    y += 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=ink, width=2)
    y += 8

    # ---- Secondary: 3 columns ----
    col_w = (W - 2 * MARGIN - 2 * 14) // 3
    sec_top = y
    sec_bottom = sec_top
    for i, (head, body, src) in enumerate(SECONDARY):
        x = MARGIN + i * (col_w + 14)
        cy = sec_top
        f_sh = font(SERIF_B, 14)
        for ln in wrap(d, head, f_sh, col_w):
            d.text((x, cy), ln, font=f_sh, fill=ink)
            cy += 18
        cy += 2
        f_sb = font(SERIF, 11)
        for ln in wrap(d, body + "  (" + src + ")", f_sb, col_w):
            d.text((x, cy), ln, font=f_sb, fill=ink)
            cy += 14
        sec_bottom = max(sec_bottom, cy)
        if i < 2:
            d.line([(x + col_w + 7, sec_top), (x + col_w + 7, cy)],
                   fill="#999999", width=1)
    y = sec_bottom + 8
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=ink, width=1)
    y += 8

    # ---- UTC timeline strip ----
    f_tl_h = font(SANS_B, 13)
    d.text((MARGIN, y), "THE DAY IN UTC", font=f_tl_h, fill=ink)
    y += 20
    tl_col_w = (W - 2 * MARGIN - 3 * 10) // 4
    tl_rows = 3
    f_tt = font(SANS_B, 10)
    f_tx = font(SANS, 10)
    tl_bottom = y
    for idx, (t, ev) in enumerate(TIMELINE):
        col = idx // tl_rows
        row = idx % tl_rows
        x = MARGIN + col * (tl_col_w + 10)
        cy = y + row * 30
        d.text((x, cy), t, font=f_tt, fill=ink)
        tw = d.textlength(t, font=f_tt)
        for ln in wrap(d, ev, f_tx, tl_col_w - tw - 6):
            d.text((x + tw + 6, cy), ln, font=f_tx, fill=ink)
            cy += 12
        tl_bottom = max(tl_bottom, cy)
    y = tl_bottom + 6
    d.line([(MARGIN, y), (W - MARGIN, y)], fill=ink, width=1)
    y += 8

    # ---- The Wire ----
    f_w_h = font(SANS_B, 13)
    d.text((MARGIN, y), f"THE WIRE — {len(WIRE)} MORE STORIES",
           font=f_w_h, fill=ink)
    y += 20
    wire_top = y
    wire_bottom_limit = H - 26  # footer line

    # Adaptive font size so the wire fits.
    for size in (12, 11, 10, 9):
        f_w = font(SANS, size)
        f_wn = font(SANS_B, size)
        line_h = size + 4
        cols = [[], [], []]
        # Balance items across 3 columns by wrapped-line count.
        col_w = (W - 2 * MARGIN - 2 * 12) // 3
        wrapped = []
        for n, (txt, src) in enumerate(WIRE, 1):
            full = f"{n}. {txt} ({src})"
            wrapped.append(wrap(d, full, f_w, col_w))
        # Greedy balance by total lines.
        loads = [0, 0, 0]
        for lines in wrapped:
            c = loads.index(min(loads))
            cols[c].append(lines)
            loads[c] += len(lines)
        need = max(loads) * line_h + (max(len(c) for c in cols) - 1) * 4
        if wire_top + need <= wire_bottom_limit:
            break
    else:
        raise SystemExit("wire does not fit even at smallest size")

    for ci, col in enumerate(cols):
        x = MARGIN + ci * (col_w + 12)
        cy = wire_top
        for lines in col:
            for ln in lines:
                d.text((x, cy), ln, font=f_w, fill=ink)
                cy += line_h
            cy += 4
        if ci < 2:
            d.line([(x + col_w + 6, wire_top), (x + col_w + 6, cy)],
                   fill="#999999", width=1)

    # ---- Footer ----
    fy = H - 20
    d.line([(MARGIN, fy - 6), (W - MARGIN, fy - 6)], fill=ink, width=1)
    f_f = font(SANS, 10)
    draw_center(d, fy, "THE WORLD  •  Tuesday 24 November 2026  •  "
                f"{STORY_COUNT} stories, all dated 24 November 2026",
                f_f, fill="#333333")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out)
    print(f"saved {out}  size={img.size}  stories={STORY_COUNT}")

if __name__ == "__main__":
    main()
