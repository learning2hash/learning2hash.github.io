---
layout: publication
title: 'Inter-bin: Interaction-based Cross-architecture Iot Binary Similarity Comparison'
authors: Qige Song, Yongzheng Zhang, Binglai Wang, Yige Chen
conference: IEEE Internet of Things Journal
year: 2022
bibkey: song2022inter
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2206.00219'}]
tags: ["Datasets", "Privacy & Security", "Scalability"]
short_authors: Song et al.
---
The big wave of Internet of Things (IoT) malware reflects the fragility of
the current IoT ecosystem. Research has found that IoT malware can spread
quickly on devices of different processer architectures, which leads our
attention to cross-architecture binary similarity comparison technology. The
goal of binary similarity comparison is to determine whether the semantics of
two binary snippets is similar. Existing learning-based approaches usually
learn the representations of binary code snippets individually and perform
similarity matching based on the distance metric, without considering
inter-binary semantic interactions. Moreover, they often rely on the
large-scale external code corpus for instruction embeddings pre-training, which
is heavyweight and easy to suffer the out-of-vocabulary (OOV) problem. In this
paper, we propose an interaction-based cross-architecture IoT binary similarity
comparison system, Inter-BIN. Our key insight is to introduce interaction
between instruction sequences by co-attention mechanism, which can flexibly
perform soft alignment of semantically related instructions from different
architectures. And we design a lightweight multi-feature fusion-based
instruction embedding method, which can avoid the heavy workload and the OOV
problem of previous approaches. Extensive experiments show that Inter-BIN can
significantly outperform state-of-the-art approaches on cross-architecture
binary similarity comparison tasks of different input granularities.
Furthermore, we present an IoT malware function matching dataset from real
network environments, CrossMal, containing 1,878,437 cross-architecture reuse
function pairs. Experimental results on CrossMal prove that Inter-BIN is
practical and scalable on real-world binary similarity comparison collections.