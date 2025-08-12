---
layout: publication
title: Using Deep Object Features For Image Descriptions
authors: Ashutosh Mishra, Marcus Liwicki
conference: Arxiv
year: 2019
bibkey: mishra2019using
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1902.09969'}]
tags: ["Evaluation"]
short_authors: Ashutosh Mishra, Marcus Liwicki
---
Inspired by recent advances in leveraging multiple modalities in machine
translation, we introduce an encoder-decoder pipeline that uses (1) specific
objects within an image and their object labels, (2) a language model for
decoding joint embedding of object features and the object labels. Our pipeline
merges prior detected objects from the image and their object labels and then
learns the sequences of captions describing the particular image. The decoder
model learns to extract descriptions for the image from scratch by decoding the
joint representation of the object visual features and their object classes
conditioned by the encoder component. The idea of the model is to concentrate
only on the specific objects of the image and their labels for generating
descriptions of the image rather than visual feature of the entire image. The
model needs to be calibrated more by adjusting the parameters and settings to
result in better accuracy and performance.