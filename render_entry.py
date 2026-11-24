"""Local build script only. Renders entry.png deterministically.

This file is build evidence. The grader entrypoint is main.py, which
never imports this module: it copies entry.png with the standard library.
"""

import hashlib
import os

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 62)
F_DATE = font("DejaVuSans-Bold.ttf", 25)
F_KICKER = font("DejaVuSans-Bold.ttf", 22)
F_HERO = font("DejaVuSans-Bold.ttf", 56)
F_HERO_SUB = font("DejaVuSans-Bold.ttf", 29)
F_PANEL = font("DejaVuSans-Bold.ttf", 29)
F_BODY = font("DejaVuSans.ttf", 21)
F_BODY_B = font("DejaVuSans-Bold.ttf", 21)
F_FOOT = font("DejaVuSans-Bold.ttf", 24)
F_FOOT2 = font("DejaVuSans.ttf", 20)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def render():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # Masthead.
    d.rectangle([0, 0, W, 118], fill=(17, 17, 17))
    d.text((24, 18), "THE WORLD", font=F_TITLE, fill=(255, 255, 255))
    d.text((24, 82), "TUESDAY 24 NOVEMBER 2026  ·  ONE IMAGE, FIVE STORIES",
           font=F_DATE, fill=(255, 204, 0))
    d.rectangle([0, 118, W, 126], fill=(200, 30, 30))

    # Hero: Nvidia / AI rebound.
    d.rectangle([24, 138, 1000, 420], fill=(16, 36, 68))
    d.text((48, 154), "LEAD  ·  MARKETS", font=F_KICKER, fill=(120, 220, 140))
    d.text((48, 184), "AI COMES", font=F_HERO, fill=(255, 255, 255))
    d.text((48, 246), "ROARING BACK", font=F_HERO, fill=(255, 255, 255))
    d.text((48, 318), "NVIDIA +31% AS HUANG RETURNS",
           font=F_HERO_SUB, fill=(255, 204, 0))
    d.text((48, 356), "Nasdaq +6.5%  ·  S&P 500 +4.7%  ·  Asia rallies",
           font=F_BODY_B, fill=(220, 230, 245))
    # Rising chart, right side.
    pts = [(640, 380), (700, 350), (760, 362), (820, 300),
           (880, 262), (940, 210), (984, 168)]
    d.line(pts, fill=(80, 220, 120), width=7)
    for (x, y) in pts:
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=(80, 220, 120))
    d.polygon([(984, 168), (958, 172), (974, 196)], fill=(80, 220, 120))
    d.text((640, 388), "31.5% IN A DAY", font=F_BODY_B, fill=(120, 220, 140))

    # Grid panels.
    panels = [
        (24, 436, (255, 238, 210), (150, 60, 0), "COP31: NO DEAL",
         "Fossil-fuel wording stripped out. EU rejects the pact; "
         "Erdogan says groundwork was laid."),
        (520, 436, (222, 235, 248), (20, 70, 130), "DRONES SINK WARSHIP",
         "Ukraine: 7 drones sank the corvette Merkury off Libya; "
         "Angara damaged."),
        (24, 644, (255, 246, 190), (130, 95, 0), "EU: 22nd SANCTIONS",
         "60 banks face a SWIFT cut; 70+ shadow-fleet ships listed; "
         "Russian flag banned in EU sport."),
        (520, 644, (210, 240, 236), (0, 105, 95), "HORMUZ AT WAR HIGH",
         "At least 22 attacks in November; 3 tankers struck "
         "Fri-Sat; oil slips below $90."),
    ]
    for (x, y, bg, accent, head, body) in panels:
        d.rectangle([x, y, x + 480, y + 192], fill=bg)
        d.rectangle([x, y, x + 480, y + 8], fill=accent)
        d.text((x + 20, y + 20), head, font=F_PANEL, fill=(17, 17, 17))
        text_block(d, x + 20, y + 62, body, F_BODY, (35, 35, 35),
                   440, 27)

    # Simple pictures inside panels: sun, ship, bars, tanker.
    d.ellipse([392, 556, 452, 616], fill=(240, 140, 20))
    d.line([(372, 586), (472, 586)], fill=(150, 60, 0), width=4)
    d.polygon([(556, 606), (640, 606), (620, 626), (576, 626)],
              fill=(30, 60, 100))
    d.rectangle([588, 584, 606, 606], fill=(30, 60, 100))
    for bx in (60, 104, 148, 192):
        d.rectangle([bx, 796, bx + 28, 820], fill=(150, 60, 0))
    d.rectangle([556, 790, 760, 820], fill=(0, 105, 95))
    d.rectangle([700, 770, 730, 790], fill=(0, 105, 95))
    d.line([(540, 826), (980, 826)], fill=(0, 105, 95), width=4)

    # Footer.
    d.rectangle([24, 852, 1000, 1000], fill=(17, 17, 17))
    d.text((48, 868), "FOOTER  ·  THE HAGUE", font=F_KICKER,
           fill=(255, 204, 0))
    d.text((48, 896), "ICJ: MYANMAR COMMITTED GENOCIDE",
           font=F_FOOT, fill=(255, 255, 255))
    d.text((48, 928), "AGAINST THE ROHINGYA — FIRST STATE RULING, 9–6",
           font=F_FOOT, fill=(255, 255, 255))
    d.text((48, 964), "Also: Moscow accuses Estonia as border closes 1 Dec",
           font=F_FOOT2, fill=(200, 200, 200))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    img.save(out, format="PNG")
    with open(out, "rb") as f:
        print(hashlib.sha256(f.read()).hexdigest())


if __name__ == "__main__":
    render()
