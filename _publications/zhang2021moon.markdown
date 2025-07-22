---
layout: publication
title: 'MOON: Multi-hash Codes Joint Learning For Cross-media Retrieval'
authors: Zhang Donglin, Wu Xiao-jun, Yin He-feng, Kittler Josef
conference: Pattern Recognition Letters
year: 2021
bibkey: zhang2021moon
citations: 10
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2109.00883'}]
tags: ["Hashing-Methods", "Efficiency", "Scalability", "Memory-Efficiency", "Tools-&-Libraries", "Compact-Codes", "Evaluation"]
short_authors: Zhang et al.
---
In recent years, cross-media hashing technique has attracted increasing
attention for its high computation efficiency and low storage cost. However,
the existing approaches still have some limitations, which need to be explored.
1) A fixed hash length (e.g., 16bits or 32bits) is predefined before learning
the binary codes. Therefore, these models need to be retrained when the hash
length changes, that consumes additional computation power, reducing the
scalability in practical applications. 2) Existing cross-modal approaches only
explore the information in the original multimedia data to perform the hash
learning, without exploiting the semantic information contained in the learned
hash codes. To this end, we develop a novel Multiple hash cOdes jOint learNing
method (MOON) for cross-media retrieval. Specifically, the developed MOON
synchronously learns the hash codes with multiple lengths in a unified
framework. Besides, to enhance the underlying discrimination, we combine the
clues from the multimodal data, semantic labels and learned hash codes for hash
learning. As far as we know, the proposed MOON is the first work to
simultaneously learn different length hash codes without retraining in
cross-media retrieval. Experiments on several databases show that our MOON can
achieve promising performance, outperforming some recent competitive shallow
and deep methods.