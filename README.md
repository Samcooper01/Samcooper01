## Sam Cooper

Hey!, I'm Sam, a physical design engineer at IBM. Most of what's here is me working on the
same problems with open tools on my own time, usually using OpenROAD on the ASAP7
process, plus some older school projects.

### learned-synth

I wanted to know whether the default recipe that open-source logic synthesis
uses is actually any good. Turns out you can usually beat it by picking a recipe
for the specific design: on 6 of 9 designs I tried, up to about 5.8% less area at
the same clock speed. I used reinforcement learning and a graph neural network
to search for recipes, and checked every candidate on a real layout instead of
trusting gate counts.
[Write-up here.](https://samcooper01.github.io/learned-synth/)

### Older projects

- [128bitFeistelCipher-ASIC](https://github.com/Samcooper01/128bitFeistelCipher-ASIC):
  a block cipher I took from a C model through synthesis, timing and power, in a
  couple of variants.
- [Matrix-Multiplication-Module](https://github.com/Samcooper01/Matrix-Multiplication-Module)
  and [Pathfinder-FPGA-robot](https://github.com/Samcooper01/Pathfinder-FPGA-robot):
  matrix multiply hardware, and a maze-solving robot with sensors and a
  proportional-integral-derivative controller. Both on an FPGA
  (field-programmable gate array), in SystemVerilog.
- [ECE554-Capstone-Project](https://github.com/Samcooper01/ECE554-Capstone-Project):
  real-time object tracking on an FPGA (field-programmable gate array). It won
  best capstone in the class.
- [SCC-16](https://github.com/topics/scc-16): a 16-bit instruction set I made
  up, with the processor, a simulator, an assembler and a half-finished
  compiler.

### Tools I use

Cadence (Genus, Innovus, Tempus, Voltus, Quantus, Cerebrus), Synopsys (Design
Compiler, Formality), Calibre, OpenROAD, Yosys, KLayout. Mostly Tcl and Python,
Verilog and SystemVerilog, some C and C++.

M.S. and B.S. from the University of Wisconsin-Madison.
