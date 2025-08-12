---
layout: publication
title: Mining Cryptonight-haven On The Varium C1100 Blockchain Accelerator Card
authors: Lucas Bex, Furkan Turan, Michiel van Beirendonck, Ingrid Verbauwhede
conference: 2022 32nd International Conference on Field-Programmable Logic and Applications
  (FPL)
year: 2022
bibkey: bex2022mining
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2212.05033'}]
tags: ["Efficiency"]
short_authors: Bex et al.
---
Cryptocurrency mining is an energy-intensive process that presents a prime
candidate for hardware acceleration. This work-in-progress presents the first
coprocessor design for the ASIC-resistant CryptoNight-Haven Proof of Work (PoW)
algorithm. We construct our hardware accelerator as a Xilinx Run Time (XRT) RTL
kernel targeting the Xilinx Varium C1100 Blockchain Accelerator Card. The
design employs deeply pipelined computation and High Bandwidth Memory (HBM) for
the underlying scratchpad data. We aim to compare our accelerator to existing
CPU and GPU miners to show increased throughput and energy efficiency of its
hash computations