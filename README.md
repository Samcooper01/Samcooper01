## Samuel Cooper

Physical design engineer at IBM (International Business Machines). I take
advanced-node chips from floorplan through sign-off: synthesis, place and route,
clock tree synthesis, timing closure, power delivery, and physical verification.

Outside work I build on the open flow, where every run is reproducible and every
number can be checked: OpenROAD on the ASAP7 (Arizona State University 7nm
predictive Process Design Kit) technology.

### Projects

**[learned-synth](https://github.com/Samcooper01/learned-synth)**
Open-source logic synthesis runs one hand-tuned recipe on every design, from a
tiny controller to a large processor. This project builds a recipe per design
with reinforcement learning and a graph neural network surrogate, and grades
every candidate on a finished chip layout instead of the usual gate-count
shortcut. On 6 of 9 designs the learned recipe beats the standard one, by as
much as 5.8% less area at the same clock speed, measured over 234 full layouts.
[Read the walkthrough.](https://samcooper01.github.io/learned-synth/)

**[128-bit Feistel cipher](https://github.com/Samcooper01/128bitFeistelCipher-ASIC)**
A streaming six-round block cipher carried from a C reference model through
register transfer level design, synthesis, static timing analysis, and power
analysis, in two design variants.

**[MazeRunner](https://github.com/Samcooper01/Pathfinder-FPGA-robot)**
A maze-solving robot on a field-programmable gate array: sensor interfaces, a
proportional-integral-derivative controller, and motor drivers, written in
SystemVerilog.

### Tools

Cadence (Genus, Innovus, Tempus, Voltus, Quantus, Cerebrus), Synopsys (Design
Compiler, Formality), Siemens Calibre, OpenROAD, KLayout, Yosys.

Tcl, Python, Verilog and SystemVerilog, C and C++.

### Education

M.S. and B.S., Electrical and Computer Engineering, University of
Wisconsin-Madison.
