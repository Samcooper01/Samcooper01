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

I wanted to see if the default recipe for open-source logic synthesis could be
improved on. Usually it can: up to 5.8% less area at the same clock speed, on 6
of 9 designs. I searched for per-design recipes with reinforcement learning, a
graph neural network and a genetic algorithm, grading each one on a real layout.
[Write-up here.](https://samcooper01.github.io/learned-synth/)

[**GEMM_CORE**](https://github.com/Samcooper01/GEMM_CORE)
A 4-bit floating point matrix multiply engine, taken from Verilog to a finished
layout on SkyWater's open 130nm process. The processing element and vector unit
were hardened as separate macros and the top built from 64 of them, so timing
closed hierarchically: 1.63 mm² at 65% utilization, clean across three corners.
A five-person project for ECE 755, VLSI Design; my part was the physical
implementation and the floating-point arithmetic.

[**Multi-Layer-Perceptron**](https://github.com/Samcooper01/Multi-Layer-Perceptron)
An end-to-end full-custom design: a multi-layer perceptron built from hand-drawn
cells rather than a standard cell library. Every cell has a schematic, a
transistor-level layout, an extracted parasitic netlist and a post-layout
simulation, which is a good way to find out how much of a cell's delay is really
wire.

[**128bitFeistelCipher-ASIC**](https://github.com/Samcooper01/128bitFeistelCipher-ASIC)
A block cipher I took from a C golden model through synthesis, static timing and
power analysis, in two variants to see what reorganizing the key logic bought.
Done over a weekend.

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

[**ECE552-5-Stage-Pipelined-Processor**](https://github.com/Samcooper01/ECE552-5-Stage-Pipelined-Processor)
A five-stage pipelined processor in Verilog, with forwarding, branch prediction
and its own memory system: caches built twice, once direct-mapped and once
set-associative, so the two could be compared.
