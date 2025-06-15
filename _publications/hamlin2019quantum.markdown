---
layout: publication
title: 'Quantum Security Of Hash Functions And Property-preservation Of Iterated Hashing'
authors: Ben Hamlin, Fang Song
conference: "Arxiv"
year: 2019
citations: 4
bibkey: hamlin2019quantum
additional_links:
  - {name: "Paper", url: 'https://arxiv.org/abs/1902.08709'}
tags: ['Hashing Fundamentals', 'Quantization and Compression', 'Hashing Methods']
---
This work contains two major parts: comprehensively studying the security
notions of cryptographic hash functions against quantum attacks and the
relationships between them; and revisiting whether Merkle-Damgard and related
iterated hash constructions preserve the security properties of the compression
function in the quantum setting. Specifically, we adapt the seven notions in
Rogaway and Shrimpton (FSE'04) to the quantum setting and prove that the
seemingly stronger attack model where an adversary accesses a challenger in
quantum superposition does not make a difference. We confirm the implications
and separations between the seven properties in the quantum setting, and in
addition we construct explicit examples separating an inherently quantum notion
called collapsing from several proposed properties. Finally, we pin down the
properties that are preserved under several iterated hash schemes. In
particular, we prove that the ROX construction in Andreeva et al.
(Asiacrypt'07) preserves the seven properties in the quantum random oracle
model.
