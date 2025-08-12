---
layout: publication
title: Fast Universal Style Transfer For Artistic And Photorealistic Rendering
authors: Jie An, Haoyi Xiong, Jiebo Luo, Jun Huan, Jinwen Ma
conference: Arxiv
year: 2019
bibkey: an2019fast
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.03118'}]
tags: ["Efficiency"]
short_authors: An et al.
---
Universal style transfer is an image editing task that renders an input
content image using the visual style of arbitrary reference images, including
both artistic and photorealistic stylization. Given a pair of images as the
source of content and the reference of style, existing solutions usually first
train an auto-encoder (AE) to reconstruct the image using deep features and
then embeds pre-defined style transfer modules into the AE reconstruction
procedure to transfer the style of the reconstructed image through modifying
the deep features. While existing methods typically need multiple rounds of
time-consuming AE reconstruction for better stylization, our work intends to
design novel neural network architectures on top of AE for fast style transfer
with fewer artifacts and distortions all in one pass of end-to-end inference.
To this end, we propose two network architectures named ArtNet and PhotoNet to
improve artistic and photo-realistic stylization, respectively. Extensive
experiments demonstrate that ArtNet generates images with fewer artifacts and
distortions against the state-of-the-art artistic transfer algorithms, while
PhotoNet improves the photorealistic stylization results by creating sharp
images faithfully preserving rich details of the input content. Moreover,
ArtNet and PhotoNet can achieve 3X to 100X speed-up over the state-of-the-art
algorithms, which is a major advantage for large content images.