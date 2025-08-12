---
layout: publication
title: Foreground-aware Semantic Representations For Image Harmonization
authors: Konstantin Sofiiuk, Polina Popenova, Anton Konushin
conference: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2021
bibkey: sofiiuk2020foreground
citations: 57
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2006.00809'}]
tags: ["Evaluation"]
short_authors: Konstantin Sofiiuk, Polina Popenova, Anton Konushin
---
Image harmonization is an important step in photo editing to achieve visual
consistency in composite images by adjusting the appearances of foreground to
make it compatible with background. Previous approaches to harmonize composites
are based on training of encoder-decoder networks from scratch, which makes it
challenging for a neural network to learn a high-level representation of
objects. We propose a novel architecture to utilize the space of high-level
features learned by a pre-trained classification network. We create our models
as a combination of existing encoder-decoder architectures and a pre-trained
foreground-aware deep high-resolution network. We extensively evaluate the
proposed method on existing image harmonization benchmark and set up a new
state-of-the-art in terms of MSE and PSNR metrics. The code and trained models
are available at https://github.com/saic-vul/image_harmonization.