---
layout: publication
title: A Standalone Fpga-based Miner For Lyra2rev2 Cryptocurrencies
authors: "Jean-fran\xE7ois T\xEAtu, Louis-charles Trudeau, Michiel van Beirendonck,\
  \ Alexios Balatsoukas-stimming, Pascal Giard"
conference: 'IEEE Transactions on Circuits and Systems I: Regular Papers'
year: 2020
bibkey: "t\xEAtu2019standalone"
citations: 9
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1905.08792'}]
tags: []
short_authors: "T\xEAtu et al."
---
Lyra2REv2 is a hashing algorithm that consists of a chain of individual
hashing algorithms, and it is used as a proof-of-work function in several
cryptocurrencies. The most crucial and exotic hashing algorithm in the
Lyra2REv2 chain is a specific instance of the general Lyra2 algorithm. This
work presents the first hardware implementation of the specific instance of
Lyra2 that is used in Lyra2REv2. Several properties of the aforementioned
algorithm are exploited in order to optimize the design. In addition, an
FPGA-based hardware implementation of a standalone miner for Lyra2REv2 on a
Xilinx Multi-Processor System on Chip is presented. The proposed Lyra2REv2
miner is shown to be significantly more energy efficient than both a GPU and a
commercially available FPGA-based miner. Finally, we also explain how the
simplified Lyra2 and Lyra2REv2 architectures can be modified with minimal
effort to also support the recent Lyra2REv3 chained hashing algorithm.