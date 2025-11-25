---
layout: publication
title: Learning Soft-attention Models For Tempo-invariant Audio-sheet Music Retrieval
authors: Stefan Balke, Matthias Dorfer, Luis Carvalho, Andreas Arzt, Gerhard Widmer
conference: Arxiv
year: 2019
bibkey: balke2019learning
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1906.10996'}]
tags: ["Multimodal Retrieval", "Robustness"]
short_authors: Balke et al.
---
Connecting large libraries of digitized audio recordings to their
corresponding sheet music images has long been a motivation for researchers to
develop new cross-modal retrieval systems. In recent years, retrieval systems
based on embedding space learning with deep neural networks got a step closer
to fulfilling this vision. However, global and local tempo deviations in the
music recordings still require careful tuning of the amount of temporal context
given to the system. In this paper, we address this problem by introducing an
additional soft-attention mechanism on the audio input. Quantitative and
qualitative results on synthesized piano data indicate that this attention
increases the robustness of the retrieval system by focusing on different parts
of the input representation based on the tempo of the audio. Encouraged by
these results, we argue for the potential of attention models as a very general
tool for many MIR tasks.