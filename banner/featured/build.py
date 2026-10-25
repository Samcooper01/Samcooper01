#!/usr/bin/env python3
"""Write and render the poster cards, 1280 by 640 each, into this directory.

One card per project, all from card.css, for places that show an image as a small
thumbnail. Each gets the project's own artefact down the right at full saturation: the
finished accelerator, a multiplier layout, the datapath, rows of hand-drawn neurons, the
capstone's clock timing, and a dozen of the generated cells.

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


CARDS = {
    "sram": dict(
        kicker="sramforge &middot; ASAP7",
        title="SRAM<br>compiler",
        sub="Three parameters in, a verified memory macro out, on open tools",
        facts="<b>1.94</b> GHz <i>/</i> <b>114,454</b> transistors <i>/</i> <b>8</b> kB",
        art=picture("a_bank.png", ".art img { left: 0; top: -1500px; width: 548px; }"),
    ),
    "competition": dict(
        kicker="Chipbase &middot; Competition 01",
        title="Systolic array<br>AI accelerator",
        sub="Gemmini from RTL to a finished layout, on open tools only",
        facts="<b>200,000</b> cells <i>/</i> <b>9</b> metal layers <i>/</i> ASAP7",
        art=picture("a_harness.png", ".art img { left: -118px; top: -50px; width: 784px; }"),
    ),
    "capstone": dict(
        kicker="ECE 554 &middot; Capstone",
        title="Object tracking<br>on an FPGA",
        sub="A camera, frame differencing in hardware, and a laser that follows what it finds",
        facts="<b>Best capstone</b> in the class <i>/</i> Cyclone V",
        art=stack("a_wave.png", 3, ".art img { left: -560px; width: 2246px; }\n"
                  + "".join(f".art img:nth-child({i+1}) {{ top: {i*216 - 4}px; }}\n" for i in range(3))),
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
        art=picture("a_cells.png", ".art img { left: -22px; top: 50%; transform: translateY(-50%); width: 592px; }"),
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
