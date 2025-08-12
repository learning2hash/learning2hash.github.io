---
layout: publication
title: Semantic Perceptual Image Compression Using Deep Convolution Networks
authors: Aaditya Prakash, Nick Moran, Solomon Garber, Antonella Dilillo, James Storer
conference: 2017 Data Compression Conference (DCC)
year: 2017
bibkey: prakash2016semantic
citations: 77
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1612.08712'}]
tags: []
short_authors: Prakash et al.
---
It has long been considered a significant problem to improve the visual
quality of lossy image and video compression. Recent advances in computing
power together with the availability of large training data sets has increased
interest in the application of deep learning cnns to address image recognition
and image processing tasks. Here, we present a powerful cnn tailored to the
specific task of semantic image understanding to achieve higher visual quality
in lossy compression. A modest increase in complexity is incorporated to the
encoder which allows a standard, off-the-shelf jpeg decoder to be used. While
jpeg encoding may be optimized for generic images, the process is ultimately
unaware of the specific content of the image to be compressed. Our technique
makes jpeg content-aware by designing and training a model to identify multiple
semantic regions in a given image. Unlike object detection techniques, our
model does not require labeling of object positions and is able to identify
objects in a single pass. We present a new cnn architecture directed
specifically to image compression, which generates a map that highlights
semantically-salient regions so that they can be encoded at higher quality as
compared to background regions. By adding a complete set of features for every
class, and then taking a threshold over the sum of all feature activations, we
generate a map that highlights semantically-salient regions so that they can be
encoded at a better quality compared to background regions. Experiments are
presented on the Kodak PhotoCD dataset and the MIT Saliency Benchmark dataset,
in which our algorithm achieves higher visual quality for the same compressed
size.