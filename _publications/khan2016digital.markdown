---
layout: publication
title: Digital Makeup From Internet Images
authors: Asad Khan, Muhammad Ahmad, Yudong Guo, Ligang Liu
conference: Optik
year: 2017
bibkey: khan2016digital
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1610.04861'}]
tags: ["Image Retrieval"]
short_authors: Khan et al.
---
We present a novel approach of color transfer between images by exploring
their high-level semantic information. First, we set up a database which
consists of the collection of downloaded images from the internet, which are
segmented automatically by using matting techniques. We then, extract image
foregrounds from both source and multiple target images. Then by using image
matting algorithms, the system extracts the semantic information such as faces,
lips, teeth, eyes, eyebrows, etc., from the extracted foregrounds of the source
image. And, then the color is transferred between corresponding parts with the
same semantic information. Next we get the color transferred result by
seamlessly compositing different parts together using alpha blending. In the
final step, we present an efficient method of color consistency to optimize the
color of a collection of images showing the common scene. The main advantage of
our method over existing techniques is that it does not need face matching, as
one could use more than one target images. It is not restricted to head shot
images as we can also change the color style in the wild. Moreover, our
algorithm does not require to choose the same color style, same pose and image
size between source and target images. Our algorithm is not restricted to
one-to-one image color transfer and can make use of more than one target images
to transfer the color in different parts in the source image. Comparing with
other approaches, our algorithm is much better in color blending in the input
data.