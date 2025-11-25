---
layout: publication
title: Deep Convolutional Autoencoder-based Lossy Image Compression
authors: Zhengxue Cheng, Heming Sun, Masaru Takeuchi, Jiro Katto
conference: 2018 Picture Coding Symposium (PCS)
year: 2018
bibkey: cheng2018deep
citations: 224
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1804.09535'}]
tags: ["Efficiency", "Quantization"]
short_authors: Cheng et al.
---
Image compression has been investigated as a fundamental research topic for
many decades. Recently, deep learning has achieved great success in many
computer vision tasks, and is gradually being used in image compression. In
this paper, we present a lossy image compression architecture, which utilizes
the advantages of convolutional autoencoder (CAE) to achieve a high coding
efficiency. First, we design a novel CAE architecture to replace the
conventional transforms and train this CAE using a rate-distortion loss
function. Second, to generate a more energy-compact representation, we utilize
the principal components analysis (PCA) to rotate the feature maps produced by
the CAE, and then apply the quantization and entropy coder to generate the
codes. Experimental results demonstrate that our method outperforms traditional
image coding algorithms, by achieving a 13.7% BD-rate decrement on the Kodak
database images compared to JPEG2000. Besides, our method maintains a moderate
complexity similar to JPEG2000.