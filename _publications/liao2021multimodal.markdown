---
layout: publication
title: Multimodal Representation Learning Via Maximization Of Local Mutual Information
authors: Ruizhi Liao, Daniel Moyer, Miriam Cha, Keegan Quigley, Seth Berkowitz, Steven
  Horng, Polina Golland, William M. Wells
conference: Lecture Notes in Computer Science
year: 2021
bibkey: liao2021multimodal
citations: 23
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.04537'}]
tags: ["Multimodal Retrieval", "Self-Supervised"]
short_authors: Liao et al.
---
We propose and demonstrate a representation learning approach by maximizing
the mutual information between local features of images and text. The goal of
this approach is to learn useful image representations by taking advantage of
the rich information contained in the free text that describes the findings in
the image. Our method trains image and text encoders by encouraging the
resulting representations to exhibit high local mutual information. We make use
of recent advances in mutual information estimation with neural network
discriminators. We argue that the sum of local mutual information is typically
a lower bound on the global mutual information. Our experimental results in the
downstream image classification tasks demonstrate the advantages of using local
features for image-text representation learning.