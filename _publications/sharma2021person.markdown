---
layout: publication
title: Person Re-identification With A Locally Aware Transformer
authors: Charu Sharma, Siddhant R. Kapil, David Chapman
conference: Arxiv
year: 2021
bibkey: sharma2021person
citations: 32
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.03720'}]
tags: ["Datasets"]
short_authors: Charu Sharma, Siddhant R. Kapil, David Chapman
---
Person Re-Identification is an important problem in computer vision-based
surveillance applications, in which the same person is attempted to be
identified from surveillance photographs in a variety of nearby zones. At
present, the majority of Person re-ID techniques are based on Convolutional
Neural Networks (CNNs), but Vision Transformers are beginning to displace pure
CNNs for a variety of object recognition tasks. The primary output of a vision
transformer is a global classification token, but vision transformers also
yield local tokens which contain additional information about local regions of
the image. Techniques to make use of these local tokens to improve
classification accuracy are an active area of research. We propose a novel
Locally Aware Transformer (LA-Transformer) that employs a Parts-based
Convolution Baseline (PCB)-inspired strategy for aggregating globally enhanced
local classification tokens into an ensemble of \(\sqrt\{N\}\) classifiers, where
\(N\) is the number of patches. An additional novelty is that we incorporate
blockwise fine-tuning which further improves re-ID accuracy. LA-Transformer
with blockwise fine-tuning achieves rank-1 accuracy of \(98.27 %\) with standard
deviation of \(0.13\) on the Market-1501 and \(98.7%\) with standard deviation of
\(0.2\) on the CUHK03 dataset respectively, outperforming all other
state-of-the-art published methods at the time of writing.