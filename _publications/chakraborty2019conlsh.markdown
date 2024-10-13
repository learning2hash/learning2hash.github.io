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
<p>Single Molecule Real-Time (SMRT) sequencing is a recent advancement
of Next Gen technology developed by Pacific Bio (PacBio). It comes with
an explosion of long and noisy reads demanding cutting edge research to
get most out of it. To deal with the high error probability of SMRT
data, a novel contextual Locality Sensitive Hashing (conLSH) based
algorithm is proposed in this article, which can effectively align the
noisy SMRT reads to the reference genome. Here, sequences are hashed
together based not only on their closeness, but also on similarity of
context. The algorithm has <span
class="math inline">\(\mathcal{O}(n^{\rho+1})\)</span> space
requirement, where <span class="math inline">\(n\)</span> is the number
of sequences in the corpus and <span class="math inline">\(\rho\)</span>
is a constant. The indexing time and querying time are bounded by <span
class="math inline">\(\mathcal{O}(
\frac{n^{\rho+1} \cdot \ln n}{\ln \frac{1}{P_2}})\)</span> and <span
class="math inline">\(\mathcal{O}(n^\rho)\)</span> respectively, where
<span class="math inline">\(P_2 &gt; 0\)</span>, is a probability value.
This algorithm is particularly useful for retrieving similar sequences,
a widely used task in biology. The proposed conLSH based aligner is
compared with rHAT, popularly used for aligning SMRT reads, and is found
to comprehensively beat it in speed as well as in memory requirements.
In particular, it takes approximately <span
class="math inline">\(24.2\%\)</span> less processing time, while saving
about <span class="math inline">\(70.3\%\)</span> in peak memory
requirement for H.sapiens PacBio dataset.</p>
