---
layout: publication
title: 'No Fear Of The Dark: Image Retrieval Under Varying Illumination Conditions'
authors: "Tomas Jenicek, Ond\u0159ej Chum"
conference: 2019 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2019
bibkey: jenicek2019no
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1908.08999'}]
tags: ["Datasets", "Evaluation", "ICCV", "Image Retrieval"]
short_authors: "Tomas Jenicek, Ond\u0159ej Chum"
---
Image retrieval under varying illumination conditions, such as day and night
images, is addressed by image preprocessing, both hand-crafted and learned.
Prior to extracting image descriptors by a convolutional neural network, images
are photometrically normalised in order to reduce the descriptor sensitivity to
illumination changes. We propose a learnable normalisation based on the U-Net
architecture, which is trained on a combination of single-camera multi-exposure
images and a newly constructed collection of similar views of landmarks during
day and night. We experimentally show that both hand-crafted normalisation
based on local histogram equalisation and the learnable normalisation
outperform standard approaches in varying illumination conditions, while
staying on par with the state-of-the-art methods on daylight illumination
benchmarks, such as Oxford or Paris datasets.