---
layout: publication
title: 'Transreid: Transformer-based Object Re-identification'
authors: Shuting He, Hao Luo, Pichao Wang, Fan Wang, Hao Li, Wei Jiang
conference: 2021 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2021
bibkey: he2021transreid
citations: 698
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.04378'}]
tags: ["ICCV"]
short_authors: He et al.
---
Extracting robust feature representation is one of the key challenges in
object re-identification (ReID). Although convolution neural network
(CNN)-based methods have achieved great success, they only process one local
neighborhood at a time and suffer from information loss on details caused by
convolution and downsampling operators (e.g. pooling and strided convolution).
To overcome these limitations, we propose a pure transformer-based object ReID
framework named TransReID. Specifically, we first encode an image as a sequence
of patches and build a transformer-based strong baseline with a few critical
improvements, which achieves competitive results on several ReID benchmarks
with CNN-based methods. To further enhance the robust feature learning in the
context of transformers, two novel modules are carefully designed. (i) The
jigsaw patch module (JPM) is proposed to rearrange the patch embeddings via
shift and patch shuffle operations which generates robust features with
improved discrimination ability and more diversified coverage. (ii) The side
information embeddings (SIE) is introduced to mitigate feature bias towards
camera/view variations by plugging in learnable embeddings to incorporate these
non-visual clues. To the best of our knowledge, this is the first work to adopt
a pure transformer for ReID research. Experimental results of TransReID are
superior promising, which achieve state-of-the-art performance on both person
and vehicle ReID benchmarks.