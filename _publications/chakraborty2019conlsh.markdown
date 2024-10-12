---
layout: publication
title: Conlsh Context Based Locality Sensitive Hashing For Mapping Of Noisy SMRT Reads
authors: Chakraborty Angana, Bandyopadhyay Sanghamitra
conference: "Arxiv"
year: 2019
bibkey: chakraborty2019conlsh
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1903.04925"}
tags: ['ARXIV', 'Independent']
---
Single Molecule Real-Time (SMRT) sequencing is a recent advancement of Next Gen technology developed by Pacific Bio (PacBio). It comes with an explosion of long and noisy reads demanding cutting edge research to get most out of it. To deal with the high error probability of SMRT data, a novel contextual Locality Sensitive Hashing (conLSH) based algorithm is proposed in this article, which can effectively align the noisy SMRT reads to the reference genome. Here, sequences are hashed together based not only on their closeness, but also on similarity of context. The algorithm has \(\mathcal\&amp;\#123;O\&amp;\#125;(n^\&amp;\#123;\rho+1\&amp;\#125;)\) space requirement, where \(n\) is the number of sequences in the corpus and \(\rho\) is a constant. The indexing time and querying time are bounded by $\mathcal&amp;\#123;O&amp;\#125;( \frac&amp;\#123;n^&amp;\#123;\rho+1&amp;\#125; \cdot \ln n&amp;\#125;&amp;\#123;\ln \frac&amp;\#123;1&amp;\#125;&amp;\#123;P\_2&amp;\#125;&amp;\#125;)\( and \)\mathcal&amp;\#123;O&amp;\#125;(n^\rho)$ respectively, where \(P\_2 > 0\), is a probability value. This algorithm is particularly useful for retrieving similar sequences, a widely used task in biology. The proposed conLSH based aligner is compared with rHAT, popularly used for aligning SMRT reads, and is found to comprehensively beat it in speed as well as in memory requirements. In particular, it takes approximately \(24.2\&#37;\) less processing time, while saving about \(70.3\&#37;\) in peak memory requirement for H.sapiens PacBio dataset.
