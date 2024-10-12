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
Single Molecule Real-Time (SMRT) sequencing is a recent advancement of Next Gen technology developed by Pacific Bio (PacBio). It comes with an explosion of long and noisy reads demanding cutting edge research to get most out of it. To deal with the high error probability of SMRT data, a novel contextual Locality Sensitive Hashing (conLSH) based algorithm is proposed in this article, which can effectively align the noisy SMRT reads to the reference genome. Here, sequences are hashed together based not only on their closeness, but also on similarity of context. The algorithm has \\(\mathcal&#123;O&#125;(n^&#123;\rho+1&#125;)\\) space requirement, where \\(n\\) is the number of sequences in the corpus and \\(\rho\\) is a constant. The indexing time and querying time are bounded by $\mathcal{O}( \frac{n^{\rho+1} \cdot \ln n}{\ln \frac{1}{P\_2}})\\( and \\)\mathcal{O}(n^\rho)$ respectively, where \\(P_2 > 0\\), is a probability value. This algorithm is particularly useful for retrieving similar sequences, a widely used task in biology. The proposed conLSH based aligner is compared with rHAT, popularly used for aligning SMRT reads, and is found to comprehensively beat it in speed as well as in memory requirements. In particular, it takes approximately \\(24.2\%\\) less processing time, while saving about \\(70.3\%\\) in peak memory requirement for H.sapiens PacBio dataset.
