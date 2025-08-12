---
layout: publication
title: High-resolution Image-based Malware Classification Using Multiple Instance
  Learning
authors: Tim Peters, Hikmat Farhat
conference: Arxiv
year: 2023
bibkey: peters2023high
citations: 0
additional_links: [{name: Code, url: 'https://github.com/timppeters/MIL-Malware-Images'},
  {name: Paper, url: 'https://arxiv.org/abs/2311.12760'}]
tags: ["Robustness"]
short_authors: Tim Peters, Hikmat Farhat
---
This paper proposes a novel method of classifying malware into families using
high-resolution greyscale images and multiple instance learning to overcome
adversarial binary enlargement. Current methods of visualisation-based malware
classification largely rely on lossy transformations of inputs such as resizing
to handle the large, variable-sized images. Through empirical analysis and
experimentation, it is shown that these approaches cause crucial information
loss that can be exploited. The proposed solution divides the images into
patches and uses embedding-based multiple instance learning with a
convolutional neural network and an attention aggregation function for
classification. The implementation is evaluated on the Microsoft Malware
Classification dataset and achieves accuracies of up to \(96.6%\) on
adversarially enlarged samples compared to the baseline of \(22.8%\). The Python
code is available online at https://github.com/timppeters/MIL-Malware-Images .