---
layout: publication
title: Random Binary Mappings For Kernel Learning And Efficient SVM
authors: Roig Gemma, Boix Xavier, Van Gool Luc
conference: "Arxiv"
year: 2013
bibkey: roig2013random
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1307.5161"}
tags: ['ARXIV', 'Quantisation', 'Supervised']
---
Support Vector Machines (SVMs) are powerful learners that have led to
state-of-the-art results in various computer vision problems. SVMs suffer from
various drawbacks in terms of selecting the right kernel, which depends on the
image descriptors, as well as computational and memory efficiency. This paper
introduces a novel kernel, which serves such issues well. The kernel is learned
by exploiting a large amount of low-complex, randomized binary mappings of the
input feature. This leads to an efficient SVM, while also alleviating the task
of kernel selection. We demonstrate the capabilities of our kernel on 6
standard vision benchmarks, in which we combine several common image
descriptors, namely histograms (Flowers17 and Daimler), attribute-like
descriptors (UCI, OSR, and a-VOC08), and Sparse Quantization (ImageNet).
Results show that our kernel learning adapts well to the different descriptors
types, achieving the performance of the kernels specifically tuned for each
image descriptor, and with similar evaluation cost as efficient SVM methods.
