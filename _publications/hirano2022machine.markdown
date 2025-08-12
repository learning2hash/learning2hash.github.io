---
layout: publication
title: Machine Learning-based Ransomware Detection Using Low-level Memory Access Patterns
  Obtained From Live-forensic Hypervisor
authors: Manabu Hirano, Ryotaro Kobayashi
conference: 2022 IEEE International Conference on Cyber Security and Resilience (CSR)
year: 2022
bibkey: hirano2022machine
citations: 5
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2205.13765'}]
tags: []
short_authors: Manabu Hirano, Ryotaro Kobayashi
---
Since modern anti-virus software mainly depends on a signature-based static
analysis, they are not suitable for coping with the rapid increase in malware
variants. Moreover, even worse, many vulnerabilities of operating systems
enable attackers to evade such protection mechanisms. We, therefore, developed
a thin and lightweight live-forensic hypervisor to create an additional
protection layer under a conventional protection layer of operating systems
with supporting ransomware detection using dynamic behavioral features. The
developed live-forensic hypervisor collects low-level memory access patterns
instead of high-level information such as process IDs and API calls that modern
Virtual Machine Introspection techniques have employed. We then created the
low-level memory access patterns dataset of three ransomware samples, one wiper
malware sample, and four benign applications. We confirmed that our best
machine learning classifier using only low-level memory access patterns
achieved an \(F_1\) score of 0.95 in detecting ransomware and wiper malware.