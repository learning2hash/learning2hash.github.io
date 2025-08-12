---
layout: publication
title: On The Texture Bias For Few-shot CNN Segmentation
authors: Reza Azad, Abdur R Fayjie, Claude Kauffman, Ismail Ben Ayed, Marco Pedersoli,
  Jose Dolz
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: azad2020texture
citations: 75
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2003.04052'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Azad et al.
---
Despite the initial belief that Convolutional Neural Networks (CNNs) are
driven by shapes to perform visual recognition tasks, recent evidence suggests
that texture bias in CNNs provides higher performing models when learning on
large labeled training datasets. This contrasts with the perceptual bias in the
human visual cortex, which has a stronger preference towards shape components.
Perceptual differences may explain why CNNs achieve human-level performance
when large labeled datasets are available, but their performance significantly
degrades in lowlabeled data scenarios, such as few-shot semantic segmentation.
To remove the texture bias in the context of few-shot learning, we propose a
novel architecture that integrates a set of Difference of Gaussians (DoG) to
attenuate high-frequency local components in the feature space. This produces a
set of modified feature maps, whose high-frequency components are diminished at
different standard deviation values of the Gaussian distribution in the spatial
domain. As this results in multiple feature maps for a single image, we employ
a bi-directional convolutional long-short-term-memory to efficiently merge the
multi scale-space representations. We perform extensive experiments on three
well-known few-shot segmentation benchmarks -- Pascal i5, COCO-20i and FSS-1000
-- and demonstrate that our method outperforms state-of-the-art approaches in
two datasets under the same conditions. The code is available at:
https://github.com/rezazad68/fewshot-segmentation