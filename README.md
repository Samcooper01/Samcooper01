### About me

Hey! I'm Sam, and I work as a physical design engineer at IBM. Day to day, that
means taking advanced-node chips from floorplan through sign-off, at both the
macro and the chip-top level. My work covers place and route, timing closure,
clock tree synthesis, hierarchical timing, chip integration, power
distribution, and the sign-off checks.

Most of what's here is things I got curious about and explored on my own, plus
some projects from school. Lately I've been interested in what machine learning
can do for the back end of the chip flow, and in open tools like OpenROAD, where
I can take a design all the way through and measure what actually changed.

Always happy to talk chips, physical design, or machine learning. You can find me on [LinkedIn](https://www.linkedin.com/in/sam-cooper12).

### Physical design

[**learned-synth**](https://github.com/Samcooper01/learned-synth)
I wanted to know whether the default recipe that open-source logic synthesis
uses is actually any good. Turns out you can usually beat it by picking a recipe
for the specific design: on 6 of 9 designs I tried, up to about 5.8% less area at
the same clock speed. I used reinforcement learning and a graph neural network
to search for recipes, and checked every candidate on a real layout instead of
trusting gate counts.
[Write-up here.](https://samcooper01.github.io/learned-synth/)

[**GEMM_CORE**](https://github.com/Samcooper01/GEMM_CORE)
A matrix multiply engine for low-precision neural network inference, in 4-bit
floating point, taken from Verilog to a finished layout on SkyWater's open
130nm process. A five-person class project; my part was the physical
implementation and the floating-point arithmetic.

[**128bitFeistelCipher-ASIC**](https://github.com/Samcooper01/128bitFeistelCipher-ASIC)
A block cipher I took from a C model through synthesis, timing and power
analysis, in a couple of variants.

### Programmable logic

- [Matrix-Multiplication-Module](https://github.com/Samcooper01/Matrix-Multiplication-Module):
  matrix multiply hardware in SystemVerilog.
- [Pathfinder-FPGA-robot](https://github.com/Samcooper01/Pathfinder-FPGA-robot):
  a maze-solving robot with sensors and a proportional-integral-derivative
  controller.
- [ECE554-Capstone-Project](https://github.com/Samcooper01/ECE554-Capstone-Project):
  real-time object tracking, on an FPGA (field-programmable gate array). It won
  best capstone in the class.

### Processors and toolchains

- [SCC-16](https://github.com/topics/scc-16): a 16-bit instruction set I made
  up, with the processor, a simulator, an assembler and a half-finished
  compiler.

### Tools I use

Cadence (Genus, Innovus, Tempus, Voltus, Quantus, Cerebrus), Synopsys (Design
Compiler, Formality), Calibre, OpenROAD, Yosys, KLayout. Mostly Tcl and Python,
Verilog and SystemVerilog, some C and C++.

M.S. and B.S. from the University of Wisconsin-Madison.
