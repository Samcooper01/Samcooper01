## 👋 About me

Hey! I'm Sam, and I work as a physical design engineer at IBM. Most of what's
here is things I got curious about and explored on my own, plus some projects
from school. Lately that's mostly been machine learning applied to the chip
flow, using open-source tools like OpenROAD to experiment.

Always happy to talk chips, physical design, or open-source silicon. You can find me on [LinkedIn](https://www.linkedin.com/in/sam-cooper12).

---

## 🔬 Projects

### 🧱 Physical design

[**rl-macro-placer**](https://github.com/Samcooper01/rl-macro-placer)
A reimplementation of Google's reinforcement learning macro placer from the
2021 Nature paper: an agent places the hard macros one at a time, a
force-directed pass settles the standard cells around them, and a wirelength,
congestion and density proxy scores the result.

[**Open-SRAM-Compiler-ASAP7nmPDK**](https://github.com/Samcooper01/Open-SRAM-Compiler-ASAP7nmPDK)
An SRAM compiler for the ASAP7 7nm predictive process. Three parameters in, a
verified memory macro out: full-custom layout, an abstract for place and route,
a timing library and a behavioral model. The verification stack runs eleven
automated tests, from 97 transcribed design rules to switch-level simulation of
the extracted netlist.

[**learned-synth**](https://github.com/Samcooper01/learned-synth)

[![learned-synth project page: is the standard recipe for open-source logic synthesis good enough? A better recipe on 6 of 9 designs, with up to 5.8% less chip area at the same clock speed.](https://raw.githubusercontent.com/Samcooper01/learned-synth/main/docs/banner.png)](https://samcooper01.github.io/learned-synth/)

I wanted to see if the default recipe for open-source logic synthesis could be
improved on. Usually it can: up to 5.8% less area at the same clock speed, on 6
of 9 designs. I searched for per-design recipes with reinforcement learning, a
graph neural network and a genetic algorithm, grading each one on a real layout.
[Write-up here.](https://samcooper01.github.io/learned-synth/)

[**Std-Cell-Layout-Gen**](https://github.com/Samcooper01/Std-Cell-Layout-Gen)
A generator that turns a transistor netlist into a manufacturable standard cell
layout with nobody drawing anything by hand. Each cell gets a short recipe of
knobs while the process rules and library architecture stay shared, so you can
change a technology parameter, rerun, and get a whole co-legal library back.
319 of the 437 cells in the SKY130 high-density library build clean so far.

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

### 🔌 Programmable logic

[**ECE554-Capstone-Project**](https://github.com/Samcooper01/ECE554-Capstone-Project)
Real-time object detection and laser targeting on a Cyclone V board: a camera
feeding frame-differencing logic built in hardware, a servo-driven laser that
tracks whatever it finds, and a video overlay so you can watch it work. Five of
us built it, and it won best capstone in the class.

[**2D-Image-Processing-Module**](https://github.com/Samcooper01/2D-Image-Processing-Module)
Real-time image processing on a camera's pixel stream before it ever reaches
memory: Bayer to color, grayscale, then a 3x3 Sobel convolution for edge
detection, with shift-register line buffers holding the window and frames
buffered in memory on the way to the display.

[**Matrix-Multiplication-Module**](https://github.com/Samcooper01/Matrix-Multiplication-Module)
A matrix-vector multiply unit: eight multiply-accumulate lanes behind input
queues, pulling operands over an Avalon memory-mapped interface, constrained to
200 MHz and checked in the timing analyzer.

[**MAC-and-FIFO**](https://github.com/Samcooper01/MAC-and-FIFO)
A multiply-accumulate unit and the queue that feeds it, built twice: once from
the vendor's library blocks and once from scratch in SystemVerilog, then
compared on resource usage.

[**Pathfinder-FPGA-robot**](https://github.com/Samcooper01/Pathfinder-FPGA-robot)
A maze-solving robot. Infrared, hall-effect and gyro sensors in, motor drivers
out, and a proportional-integral-derivative controller keeping it off the walls.

### 🧮 Processors and toolchains

[**ECE552-5-Stage-Pipelined-Processor**](https://github.com/Samcooper01/ECE552-5-Stage-Pipelined-Processor)
A five-stage pipelined processor in Verilog, with forwarding, branch prediction
and its own memory system: caches built twice, once direct-mapped and once
set-associative, so the two could be compared.

[**SCC-16**](https://github.com/topics/scc-16)
A 16-bit instruction set I made up, then built everything around: the control
unit, arithmetic logic unit, register file and memory unit in SystemVerilog, an
instruction-set simulator in C to check them against, an assembler, and a
compiler that got about half finished.

### 💻 Programming

[**heap-alloc-dealloc**](https://github.com/Samcooper01/heap-alloc-dealloc)
A heap allocator in C: best-fit allocation, with free blocks coalesced
immediately rather than swept later.

[**simpleShell**](https://github.com/Samcooper01/simpleShell)
A Unix shell in C. Command parsing, process control, command history and saved
directories.

[**SysMonitor**](https://github.com/Samcooper01/SysMonitor)
A command-line system monitor for Linux, in C.

[**file_searcher**](https://github.com/Samcooper01/file_searcher)
Finds every instance of a string in a file, written in 32-bit x86 assembly.

[**game_ball**](https://github.com/Samcooper01/game_ball)
Pong, in x86 assembly.

[**MSP430Learning**](https://github.com/Samcooper01/MSP430Learning)
Bare-metal microcontroller exercises in C on an MSP430: blink, a simple timer
and a delay timer.
