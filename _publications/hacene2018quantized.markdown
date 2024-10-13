---
layout: publication
title: Quantized Guided Pruning For Efficient Hardware Implementations Of Convolutional Neural Networks
authors: Hacene Ghouthi Boukli Elec, Gripon Vincent Elec, Arzel Matthieu Elec, Farrugia Nicolas Elec, Bengio Yoshua Diro
conference: "Arxiv"
year: 2018
bibkey: hacene2018quantized
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1812.11337"}
tags: ['ARXIV', 'CNN', 'Quantisation', 'Supervised']
---
Convolutional Neural Networks (CNNs) are state-of-the-art in numerous
computer vision tasks such as object classification and detection. However, the
large amount of parameters they contain leads to a high computational
complexity and strongly limits their usability in budget-constrained devices
such as embedded devices. In this paper, we propose a combination of a new
pruning technique and a quantization scheme that effectively reduce the
complexity and memory usage of convolutional layers of CNNs, and replace the
complex convolutional operation by a low-cost multiplexer. We perform
experiments on the CIFAR10, CIFAR100 and SVHN and show that the proposed method
achieves almost state-of-the-art accuracy, while drastically reducing the
computational and memory footprints. We also propose an efficient hardware
architecture to accelerate CNN operations. The proposed hardware architecture
is a pipeline and accommodates multiple layers working at the same time to
speed up the inference process.
