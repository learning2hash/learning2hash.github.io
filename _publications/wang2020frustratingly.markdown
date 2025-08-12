---
layout: publication
title: Frustratingly Simple Few-shot Object Detection
authors: Xin Wang, Thomas E. Huang, Trevor Darrell, Joseph E. Gonzalez, Fisher Yu
conference: Arxiv
year: 2020
bibkey: wang2020frustratingly
citations: 310
additional_links: [{name: Code, url: 'https://github.com/ucbdrive/few-shot-object-detection'},
  {name: Paper, url: 'https://arxiv.org/abs/2003.06957'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Wang et al.
---
Detecting rare objects from a few examples is an emerging problem. Prior
works show meta-learning is a promising approach. But, fine-tuning techniques
have drawn scant attention. We find that fine-tuning only the last layer of
existing detectors on rare classes is crucial to the few-shot object detection
task. Such a simple approach outperforms the meta-learning methods by roughly
2~20 points on current benchmarks and sometimes even doubles the accuracy of
the prior methods. However, the high variance in the few samples often leads to
the unreliability of existing benchmarks. We revise the evaluation protocols by
sampling multiple groups of training examples to obtain stable comparisons and
build new benchmarks based on three datasets: PASCAL VOC, COCO and LVIS. Again,
our fine-tuning approach establishes a new state of the art on the revised
benchmarks. The code as well as the pretrained models are available at
https://github.com/ucbdrive/few-shot-object-detection.