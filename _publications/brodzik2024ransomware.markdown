---
layout: publication
title: Ransomware Detection Using Machine Learning In The Linux Kernel
authors: "Adrian Brodzik, Tomasz Malec-Kruszy\u0144ski, Wojciech Niewolski, Miko\u0142\
  aj Tkaczyk, Krzysztof Bocianiak, Sok-Yen Loui"
conference: Arxiv
year: 2024
bibkey: brodzik2024ransomware
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2409.06452'}]
tags: []
short_authors: Brodzik et al.
---
Linux-based cloud environments have become lucrative targets for ransomware
attacks, employing various encryption schemes at unprecedented speeds.
Addressing the urgency for real-time ransomware protection, we propose
leveraging the extended Berkeley Packet Filter (eBPF) to collect system call
information regarding active processes and infer about the data directly at the
kernel level. In this study, we implement two Machine Learning (ML) models in
eBPF - a decision tree and a multilayer perceptron. Benchmarking latency and
accuracy against their user space counterparts, our findings underscore the
efficacy of this approach.