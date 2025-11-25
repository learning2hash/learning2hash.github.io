---
layout: publication
title: 'GPU-FV: Realtime Fisher Vector And Its Applications In Video Monitoring'
authors: Wenying Ma, Liangliang Cao, Lei Yu, Guoping Long, Yucheng Li
conference: Arxiv
year: 2016
bibkey: ma2016gpu
citations: 2
additional_links: [{name: Code, url: 'https://bitbucket.org/mawenjing/gpu-fv'}, {
    name: Paper, url: 'https://arxiv.org/abs/1604.03498'}]
tags: ["Efficiency", "Video Retrieval"]
short_authors: Ma et al.
---
Fisher vector has been widely used in many multimedia retrieval and visual
recognition applications with good performance. However, the computation
complexity prevents its usage in real-time video monitoring. In this work, we
proposed and implemented GPU-FV, a fast Fisher vector extraction method with
the help of modern GPUs. The challenge of implementing Fisher vector on GPUs
lies in the data dependency in feature extraction and expensive memory access
in Fisher vector computing. To handle these challenges, we carefully designed
GPU-FV in a way that utilizes the computing power of GPU as much as possible,
and applied optimizations such as loop tiling to boost the performance. GPU-FV
is about 12 times faster than the CPU version, and 50% faster than a
non-optimized GPU implementation. For standard video input (320*240), GPU-FV
can process each frame within 34ms on a model GPU. Our experiments show that
GPU-FV obtains a similar recognition accuracy as traditional FV on VOC 2007 and
Caltech 256 image sets. We also applied GPU-FV for realtime video monitoring
tasks and found that GPU-FV outperforms a number of previous works. Especially,
when the number of training examples are small, GPU-FV outperforms the recent
popular deep CNN features borrowed from ImageNet. The code can be downloaded
from the following link https://bitbucket.org/mawenjing/gpu-fv.