---
layout: publication
title: Q-matrix Unaware Double JPEG Detection Using Dct-domain Deep Bilstm Network
authors: Vinay Verma, Deepak Singh, Nitin Khanna
conference: Arxiv
year: 2021
bibkey: verma2021q
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.04765'}]
tags: []
short_authors: Vinay Verma, Deepak Singh, Nitin Khanna
---
The double JPEG compression detection has received much attention in recent
years due to its applicability as a forensic tool for the most widely used JPEG
file format. Existing state-of-the-art CNN-based methods either use histograms
of all the frequencies or rely on heuristics to select histograms of specific
low frequencies to classify single and double compressed images. However, even
amidst lower frequencies of double compressed images/patches, histograms of all
the frequencies do not have distinguishable features to separate them from
single compressed images. This paper directly extracts the quantized DCT
coefficients from the JPEG images without decompressing them in the pixel
domain, obtains all AC frequencies' histograms, uses a module based on \(1\times
1\) depth-wise convolutions to learn the inherent relation between each
histogram and corresponding q-factor, and utilizes a tailor-made BiLSTM network
for selectively encoding these feature vector sequences. The proposed system
outperforms several baseline methods on a relatively large and diverse publicly
available dataset of single and double compressed patches. Another essential
aspect of any single vs. double JPEG compression detection system is handling
the scenario where test patches are compressed with entirely different
quantization matrices (Q-matrices) than those used while training; different
camera manufacturers and image processing software generally utilize their
customized quantization matrices. A set of extensive experiments shows that the
proposed system trained on a single dataset generalizes well on other datasets
compressed with completely unseen quantization matrices and outperforms the
state-of-the-art methods in both seen and unseen quantization matrices
scenarios.