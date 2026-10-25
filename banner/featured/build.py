#!/usr/bin/env python3
"""Write and render the poster cards, 1280 by 640 each, into this directory.

One card per project, all from card.css, for places that show an image as a small
thumbnail. Each gets the project's own artefact down the right at full saturation; the
two without a usable one (the capstone, the cell generator) get a drawing instead.

    python3 build.py <path to headless chromium>     (or set CHROME)
"""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="card.css">
<style>{style}</style>
</head>
<body>
{art}
  <div class="wrap">
    <div class="kicker">{kicker}</div>
    <h1>{title}<small>{sub}</small></h1>
    <div class="facts">{facts}</div>
  </div>
</body>
</html>
"""


def picture(src, style):
    return f'  <div class="art"><img src="img/{src}" alt=""></div>\n  <div class="fade"></div>', style


def stack(src, count, style):
    """A wide, short artefact repeated down the column, which is how the real design is
    built anyway: rows of the same cell."""
    imgs = "".join(f'<img src="img/{src}" alt="">' for _ in range(count))
    return f'  <div class="art">{imgs}</div>\n  <div class="fade"></div>', style


def sheet(src, style):
    return f'  <div class="art sheet"><img src="img/{src}" alt=""></div>\n  <div class="fade"></div>', style


def dots(built, total):
    """One square per cell in the library, the ones that build clean picked out."""
    body = "".join(f'<i class="{"on" if i < built else ""}"></i>' for i in range(total))
    return f'  <div class="dots">{body}</div>', ""


def crosshair():
    """No photograph of the build survives, so the card draws what it did instead:
    a frame locked onto a moving target."""
    return ('''  <div class="art">
    <svg viewBox="0 0 548 640" width="548" height="640">
      <defs><pattern id="g" width="34" height="34" patternUnits="userSpaceOnUse">
        <path d="M34 0H0v34" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>
      </pattern></defs>
      <rect width="548" height="640" fill="url(#g)"/>
      <g fill="none" stroke="#f0bb52" stroke-width="4">
        <path d="M150 196h-44v-44M398 196h44v-44M150 444h-44v44M398 444h44v44"/>
      </g>
      <rect x="106" y="152" width="336" height="336" fill="rgba(240,187,82,0.07)"/>
      <circle cx="274" cy="320" r="86" fill="none" stroke="rgba(240,187,82,0.5)" stroke-width="3"/>
      <circle cx="274" cy="320" r="13" fill="#e8402a"/>
      <g stroke="rgba(240,187,82,0.5)" stroke-width="3">
        <path d="M274 196v62M274 382v62M150 320h62M336 320h62"/>
      </g>
    </svg>
  </div>''', "")


CARDS = {
    "competition": dict(
        kicker="Chipbase &middot; Competition 01",
        title="Systolic array<br>AI accelerator",
        sub="Gemmini from RTL to a finished layout, on open tools",
        facts="<b>200,000</b> cells <i>/</i> <b>35,000</b> registers <i>/</i> <b>9</b> metal layers",
        art=picture("a_harness.png", ".art img { left: -118px; top: -50px; width: 784px; }"),
    ),
    "capstone": dict(
        kicker="ECE 554 &middot; Capstone",
        title="Object tracking<br>on an FPGA",
        sub="A camera, frame differencing in hardware, and a laser that follows what it finds",
        facts="<b>Best capstone</b> in the class <i>/</i> Cyclone V",
        art=crosshair(),
    ),
    "processor": dict(
        kicker="ECE 552",
        title="Five-stage<br>pipelined processor",
        sub="Forwarding, branch prediction, and a memory system of its own",
        facts="<b>5</b> stages <i>/</i> <b>2</b> cache designs, compared",
        art=sheet("a_ece552.png", ".art.sheet img { left: -126px; top: 32px; width: 726px; }"),
    ),
    "gemm": dict(
        kicker="ECE 755 &middot; VLSI Design",
        title="FP4 matrix<br>multiply engine",
        sub="Verilog to a finished layout on SkyWater's open 130nm process",
        facts="<b>1.63</b> mm&sup2; <i>/</i> <b>65%</b> utilization <i>/</i> <b>3</b> corners clean",
        art=picture("a_gemm.png", ".art img { left: -44px; top: -44px; width: 740px; }"),
    ),
    "perceptron": dict(
        kicker="ECE 555 &middot; Full custom",
        title="A perceptron,<br>drawn by hand",
        sub="Every cell has a schematic, a transistor-level layout, and a post-layout simulation",
        facts="<b>transistor level</b> <i>/</i> extracted parasitics",
        art=stack("a_mlp.png", 3, ".art img { left: -92px; width: 760px; }\n"
                  ".art img:nth-child(1) { top: -24px; }\n"
                  ".art img:nth-child(2) { top: 194px; }\n"
                  ".art img:nth-child(3) { top: 412px; }"),
    ),
    "stdcell": dict(
        kicker="SKY130 &middot; Cell generator",
        title="Standard cells,<br>generated",
        sub="A transistor netlist in, a manufacturable layout out, with nothing drawn by hand",
        facts="<b>319</b> of <b>437</b> cells build clean",
        art=dots(319, 437),
    ),
}


def main():
    chrome = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CHROME")
    if not chrome:
        sys.exit("usage: build.py <path to headless chromium>  (or set CHROME)")

    for name, card in CARDS.items():
        art, style = card["art"]
        page = PAGE.format(style=style, art=art, kicker=card["kicker"],
                           title=card["title"], sub=card["sub"], facts=card["facts"])
        source = HERE / f"{name}.html"
        source.write_text(page)
        out = HERE / f"{name}.png"
        subprocess.run([chrome, "--headless", "--no-sandbox", "--hide-scrollbars",
                        "--window-size=1280,640", "--force-device-scale-factor=1",
                        "--virtual-time-budget=6000", f"--screenshot={out}",
                        source.as_uri()], check=True, capture_output=True)
        print(f"{out.name:18s} {out.stat().st_size // 1024:4d} KB")


if __name__ == "__main__":
    main()
