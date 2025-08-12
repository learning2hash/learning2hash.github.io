---
layout: publication
title: 'Hashpim: High-throughput SHA-3 Via Memristive Digital Processing-in-memory'
authors: Batel Oved, Orian Leitersdorf, Ronny Ronen, Shahar Kvatinsky
conference: 2022 11th International Conference on Modern Circuits and Systems Technologies
  (MOCAST)
year: 2022
bibkey: oved2022hashpim
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.13559'}]
tags: ["Efficiency", "Hashing Methods"]
short_authors: Oved et al.
---
Recent research has sought to accelerate cryptographic hash functions as they
are at the core of modern cryptography. Traditional designs, however, suffer
from the von Neumann bottleneck that originates from the separation of
processing and memory units. An emerging solution to overcome this bottleneck
is processing-in-memory (PIM): performing logic within the same devices
responsible for memory to eliminate data-transfer and simultaneously provide
massive computational parallelism. In this paper, we seek to vastly accelerate
the state-of-the-art SHA-3 cryptographic function using the memristive memory
processing unit (mMPU), a general-purpose memristive PIM architecture. To that
end, we propose a novel in-memory algorithm for variable rotation, and utilize
an efficient mapping of the SHA-3 state vector for memristive crossbar arrays
to efficiently exploit PIM parallelism. We demonstrate a massive energy
efficiency of 1,422 Gbps/W, improving a state-of-the-art memristive SHA-3
accelerator (SHINE-2) by 4.6x.