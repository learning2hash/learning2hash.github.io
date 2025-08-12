---
layout: publication
title: 'A Byte Sequence Is Worth An Image: CNN For File Fragment Classification Using
  Bit Shift And N-gram Embeddings'
authors: Wenyang Liu, Yi Wang, Kejun Wu, Kim-Hui Yap, Lap-Pui Chau
conference: 2023 IEEE 5th International Conference on Artificial Intelligence Circuits
  and Systems (AICAS)
year: 2023
bibkey: liu2023byte
citations: 5
additional_links: [{name: Code, url: 'https://github.com/wenyang001/Byte2Image'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.06983'}]
tags: []
short_authors: Liu et al.
---
File fragment classification (FFC) on small chunks of memory is essential in
memory forensics and Internet security. Existing methods mainly treat file
fragments as 1d byte signals and utilize the captured inter-byte features for
classification, while the bit information within bytes, i.e., intra-byte
information, is seldom considered. This is inherently inapt for classifying
variable-length coding files whose symbols are represented as the variable
number of bits. Conversely, we propose Byte2Image, a novel data augmentation
technique, to introduce the neglected intra-byte information into file
fragments and re-treat them as 2d gray-scale images, which allows us to capture
both inter-byte and intra-byte correlations simultaneously through powerful
convolutional neural networks (CNNs). Specifically, to convert file fragments
to 2d images, we employ a sliding byte window to expose the neglected
intra-byte information and stack their n-gram features row by row. We further
propose a byte sequence \& image fusion network as a classifier, which can
jointly model the raw 1d byte sequence and the converted 2d image to perform
FFC. Experiments on FFT-75 dataset validate that our proposed method can
achieve notable accuracy improvements over state-of-the-art methods in nearly
all scenarios. The code will be released at
https://github.com/wenyang001/Byte2Image.