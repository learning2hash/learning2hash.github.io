---
layout: publication
title: Progressive Neural Image Compression With Nested Quantization And Latent Ordering
authors: Yadong Lu, Yinhao Zhu, Yang Yang, Amir Said, Taco S Cohen
conference: 2021 IEEE International Conference on Image Processing (ICIP)
year: 2021
bibkey: lu2021progressive
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.02913'}]
tags: ["Quantization"]
short_authors: Lu et al.
---
We present PLONQ, a progressive neural image compression scheme which pushes
the boundary of variable bitrate compression by allowing quality scalable
coding with a single bitstream. In contrast to existing learned variable
bitrate solutions which produce separate bitstreams for each quality, it
enables easier rate-control and requires less storage. Leveraging the latent
scaling based variable bitrate solution, we introduce nested quantization, a
method that defines multiple quantization levels with nested quantization
grids, and progressively refines all latents from the coarsest to the finest
quantization level. To achieve finer progressiveness in between any two
quantization levels, latent elements are incrementally refined with an
importance ordering defined in the rate-distortion sense. To the best of our
knowledge, PLONQ is the first learning-based progressive image coding scheme
and it outperforms SPIHT, a well-known wavelet-based progressive image codec.