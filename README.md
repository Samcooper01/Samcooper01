## Sam Cooper

Physical design engineer at IBM. I take
advanced-node chips from floorplan through sign-off: synthesis, place and route,
clock tree synthesis, timing closure, power delivery, and physical verification.

Outside work I do the same thing in the open, where the runs are reproducible
and the numbers can be checked: the OpenROAD flow on the ASAP7 (Arizona State
University 7nm predictive Process Design Kit) technology.

### learned-synth

**On 6 of 9 designs, a synthesis recipe chosen for that design beats the
standard hand-tuned one, by as much as 5.8% less area at the same clock speed,
measured on 234 finished chip layouts instead of on gate counts.**

Open-source logic synthesis hands a tiny controller and a large processor the
same fixed recipe. This project builds a better one per design, using
reinforcement learning, a graph neural network surrogate, and surrogate-guided
evolutionary search, and grades every candidate through place and route to
sign-off.

[Read the walkthrough](https://samcooper01.github.io/learned-synth/) ·
[Repository](https://github.com/Samcooper01/learned-synth)

### Earlier work

- [128-bit Feistel cipher](https://github.com/Samcooper01/128bitFeistelCipher-ASIC):
  a streaming six-round block cipher carried from a C golden model through
  RTL (register transfer level) design, synthesis, static timing analysis and
  power analysis.
- [MazeRunner](https://github.com/Samcooper01/Pathfinder-FPGA-robot): a
  maze-solving robot on an FPGA (field-programmable gate array), with sensor
  interfaces, a PID (proportional-integral-derivative) controller and motor
  drivers in SystemVerilog.
- [SCC-16](https://github.com/topics/scc-16): a 16-bit instruction set of my
  own, with its processor in SystemVerilog, a simulator in C, an assembler and
  a partial compiler.

### Tools

Cadence (Genus, Innovus, Tempus, Voltus, Quantus, Cerebrus), Synopsys (Design
Compiler, Formality), Siemens Calibre, OpenROAD, KLayout, Yosys.

Tcl, Python, Verilog and SystemVerilog, C and C++.

M.S. and B.S. in Electrical and Computer Engineering, University of
Wisconsin-Madison.
