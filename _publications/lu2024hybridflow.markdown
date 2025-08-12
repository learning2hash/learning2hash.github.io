---
layout: publication
title: 'Hybridflow: Infusing Continuity Into Masked Codebook For Extreme Low-bitrate
  Image Compression'
authors: Lei Lu, Yanyue Xie, Wei Jiang, Wei Wang, Xue Lin, Yanzhi Wang
conference: Arxiv
year: 2024
bibkey: lu2024hybridflow
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.13372'}]
tags: ["Quantization"]
short_authors: Lu et al.
---
This paper investigates the challenging problem of learned image compression
(LIC) with extreme low bitrates. Previous LIC methods based on transmitting
quantized continuous features often yield blurry and noisy reconstruction due
to the severe quantization loss. While previous LIC methods based on learned
codebooks that discretize visual space usually give poor-fidelity
reconstruction due to the insufficient representation power of limited
codewords in capturing faithful details. We propose a novel dual-stream
framework, HyrbidFlow, which combines the continuous-feature-based and
codebook-based streams to achieve both high perceptual quality and high
fidelity under extreme low bitrates. The codebook-based stream benefits from
the high-quality learned codebook priors to provide high quality and clarity in
reconstructed images. The continuous feature stream targets at maintaining
fidelity details. To achieve the ultra low bitrate, a masked token-based
transformer is further proposed, where we only transmit a masked portion of
codeword indices and recover the missing indices through token generation
guided by information from the continuous feature stream. We also develop a
bridging correction network to merge the two streams in pixel decoding for
final image reconstruction, where the continuous stream features rectify biases
of the codebook-based pixel decoder to impose reconstructed fidelity details.
Experimental results demonstrate superior performance across several datasets
under extremely low bitrates, compared with existing single-stream
codebook-based or continuous-feature-based LIC methods.