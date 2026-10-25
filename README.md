### 👋 About me

Hey! I'm Sam, and I work as a physical design engineer at IBM. Day to day, that
means taking advanced-node chips from floorplan through sign-off, at both the
macro and the chip-top level. My work covers place and route, timing closure,
clock tree synthesis, hierarchical timing, chip integration, power
distribution, and the sign-off checks.

Most of what's here is things I got curious about and explored on my own, plus
some projects from school. Lately I've been interested in what machine learning
can do for the back end of the chip flow, and in open tools like OpenROAD, where
I can take a design all the way through and measure what actually changed.

Always happy to talk chips, physical design, or open-source silicon. You can find me on [LinkedIn](https://www.linkedin.com/in/sam-cooper12).

---

### 🔬 Projects

#### 🧱 Physical design

[**learned-synth**](https://github.com/Samcooper01/learned-synth)

[![learned-synth project page: is the standard recipe for open-source logic synthesis good enough? A better recipe on 6 of 9 designs, with up to 5.8% less chip area at the same clock speed.](https://raw.githubusercontent.com/Samcooper01/learned-synth/main/docs/banner.png)](https://samcooper01.github.io/learned-synth/)

I wanted to see whether the default recipe that open-source logic synthesis uses
could be improved on. It usually can, if you pick a recipe for the specific
design: on 6 of 9 designs I tried, up to about 5.8% less area
at the same clock speed. I used reinforcement learning and a graph neural
network to search for recipes, then a genetic algorithm to search further, and
checked every candidate on a real layout instead of trusting gate counts. That
came out to 234 full layouts through OpenROAD on the ASAP7 predictive process.
[Write-up here.](https://samcooper01.github.io/learned-synth/)

[**GEMM_CORE**](https://github.com/Samcooper01/GEMM_CORE)
A matrix multiply engine for low-precision neural network inference, in 4-bit
floating point, taken from Verilog to a finished layout on SkyWater's open
130nm process. The processing element and the vector unit were hardened as
separate macros and the top level built out of 64 of them, so it closed timing
hierarchically rather than flat: 1.63 mm² of die at about 65% utilization,
signed off across three corners with no setup or hold violations. A five-person
class project; my part was the physical implementation and the floating-point
arithmetic.

[**128bitFeistelCipher-ASIC**](https://github.com/Samcooper01/128bitFeistelCipher-ASIC)
A block cipher I took from a C golden model through synthesis, static timing and
power analysis, in two variants to see what reorganizing the key logic bought.
Done over a weekend.

[**Multi-Layer-Perceptron**](https://github.com/Samcooper01/Multi-Layer-Perceptron)
A multi-layer perceptron built out of full-custom cells rather than standard
ones. Every cell has a schematic, a transistor-level layout, an extracted
parasitic netlist and a post-layout simulation, which is a good way to find out
how much of a cell's delay is really wire.

#### 🔌 Programmable logic

[**ECE554-Capstone-Project**](https://github.com/Samcooper01/ECE554-Capstone-Project)
Real-time object detection and laser targeting on a Cyclone V board: a camera
feeding frame-differencing logic built in hardware, a servo-driven laser that
tracks whatever it finds, and a video overlay so you can watch it work. Five of
us built it, and it won best capstone in the class.

[**Matrix-Multiplication-Module**](https://github.com/Samcooper01/Matrix-Multiplication-Module)
A matrix-vector multiply unit: eight multiply-accumulate lanes behind input
queues, pulling operands over an Avalon memory-mapped interface, constrained to
200 MHz and checked in the timing analyzer.

[**Pathfinder-FPGA-robot**](https://github.com/Samcooper01/Pathfinder-FPGA-robot)
A maze-solving robot. Infrared, hall-effect and gyro sensors in, motor drivers
out, and a proportional-integral-derivative controller keeping it off the walls.

#### 🧮 Processors and toolchains

[**SCC-16**](https://github.com/topics/scc-16)
A 16-bit instruction set I made up, then built everything around: the control
unit, arithmetic logic unit, register file and memory unit in SystemVerilog, an
instruction-set simulator in C to check them against, an assembler, and a
compiler that got about half finished.

---

### 🛠 Tools I use

Cadence (Genus, Innovus, Tempus, Voltus, Quantus, Cerebrus), Synopsys (Design
Compiler, Formality), Calibre, OpenROAD, Yosys, KLayout. Mostly Tcl and Python,
Verilog and SystemVerilog, some C and C++.

M.S. and B.S. from the University of Wisconsin-Madison.
