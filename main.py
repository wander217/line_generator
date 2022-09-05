import json
import math
import os
import random
import lmdb
import tqdm
from PIL import Image, ImageDraw, ImageFont

alpha = open(r'F:\project\python\line_generator\material\alphabet', 'r', encoding='utf-8').read()


def has_glyph(glyph):
    return glyph in alpha


font_root = r'F:\project\python\line_generator\material\font'
bg_root = r'F:\project\python\line_generator\material\bg'
dict_path = r'F:\project\python\line_generator\material\train.json'
save_path = r"F:\project\data\lines\train"
count = 0

env = lmdb.open(save_path, map_size=int(1099511627776 // 1024 * 2 ** 4))

with open(dict_path, 'r', encoding='utf-8') as f:
    lines = json.loads(f.read())
bgs = [Image.open(os.path.join(bg_root, bg_path)) for bg_path in os.listdir(bg_root)]
fonts = [ImageFont.truetype(os.path.join(font_root, font_path), 16, encoding="utf-8")
         for font_path in os.listdir(font_root)]
with env.begin(write=True) as txn:
    for line in tqdm.tqdm(lines):
        line = "".join([c if has_glyph(c) else "" for c in line])
        line_tmps = [line, line.lower(), line.upper()]
        for font in fonts:
            for bg in bgs:
                line_tmp = random.choice(line_tmps)
                x1, y1, x2, y2 = font.getbbox(line_tmp)
                w, h = x2 - x1 + 10, y2 - y1 + 10
                bw, bh = bg.size
                text_image = Image.new("RGBA", (w, h))
                text_image_draw = ImageDraw.Draw(text_image)
                text_image_draw.text((5, 0), line_tmp, font=font, fill=(0, 0, 0))
                x, y = random.randint(0, bw - w - 10), random.randint(0, bh - h - 10)
                text_bg = bg.crop((x, y, x + w, y + h))
                text_bg.paste(text_image, (0, 0), mask=text_image)
                # text_bg.show()
                tw, th = text_bg.size
                text_bg = text_bg.resize((math.ceil(32 / th * tw), 32))
                new_image = Image.new("RGB", (1024, 32), (255, 255, 255))
                new_image.paste(text_bg, (0, 0))
                new_image.save(os.path.join(save_path, "test.jpg"))
                with open(os.path.join(save_path, "test.jpg"), 'rb') as f:
                    imageBin = f.read()
                txn.put("img{}".format(count + 1).encode("utf-8"), imageBin)
                txn.put("label{}".format(count + 1).encode("utf-8"), line_tmp.encode("utf-8"))
                count = count + 1
    txn.put("num-samples".encode("utf-8"), str(count).encode("utf-8"))
