---
layout: publication
title: A Method For Command Identification Using Modified Collision Free Hashing With Addition Rotation Iterative Hash Functions (part 1)
authors: Skraparlis Dimitrios
conference: "Arxiv"
year: 2000
bibkey: skraparlis2000method
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/cs/0005028"}
tags: ['ARXIV', 'Independent']
---
This paper proposes a method for identification of a user`s fixed string set (which can be a command/instruction set for a terminal or microprocessor). This method is fast and has very small memory requirements, compared to a traditional full string storage and compare method. The user feeds characters into a microcontroller via a keyboard or another microprocessor sends commands and the microcontroller hashes the input in order to identify valid commands, ensuring no collisions between hashed valid strings, while applying further criteria to narrow collision between random and valid strings. The method proposed narrows the possibility of the latter kind of collision, achieving small code and memory-size utilization and very fast execution. Hashing is achieved using additive &amp; rotating hash functions in an iterative form, which can be very easily implemented in simple microcontrollers and microprocessors. Such hash functions are presented and compared according to their efficiency for a given string/command set, using the program found in the appendix.
