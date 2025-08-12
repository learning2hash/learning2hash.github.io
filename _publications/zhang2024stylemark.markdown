---
layout: publication
title: 'Stylemark: A Robust Watermarking Method For Art Style Images Against Black-box
  Arbitrary Style Transfer'
authors: Yunming Zhang, Dengpan Ye, Sipeng Shen, Jun Wang
conference: Arxiv
year: 2024
bibkey: zhang2024stylemark
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.07129'}]
tags: ["Robustness"]
short_authors: Zhang et al.
---
Arbitrary Style Transfer (AST) achieves the rendering of real natural images
into the painting styles of arbitrary art style images, promoting art
communication. However, misuse of unauthorized art style images for AST may
infringe on artists' copyrights. One countermeasure is robust watermarking,
which tracks image propagation by embedding copyright watermarks into carriers.
Unfortunately, AST-generated images lose the structural and semantic
information of the original style image, hindering end-to-end robust tracking
by watermarks. To fill this gap, we propose StyleMark, the first robust
watermarking method for black-box AST, which can be seamlessly applied to art
style images achieving precise attribution of artistic styles after AST.
Specifically, we propose a new style watermark network that adjusts the mean
activations of style features through multi-scale watermark embedding, thereby
planting watermark traces into the shared style feature space of style images.
Furthermore, we design a distribution squeeze loss, which constrain content
statistical feature distortion, forcing the reconstruction network to focus on
integrating style features with watermarks, thus optimizing the intrinsic
watermark distribution. Finally, based on solid end-to-end training, StyleMark
mitigates the optimization conflict between robustness and watermark
invisibility through decoder fine-tuning under random noise. Experimental
results demonstrate that StyleMark exhibits significant robustness against
black-box AST and common pixel-level distortions, while also securely defending
against malicious adaptive attacks.