---
layout: publication
title: Weakly Supervised Object Localization On Grocery Shelves Using Simple FCN And
  Synthetic Dataset
authors: Srikrishna Varadarajan, Muktabh Mayank Srivastava
conference: Proceedings of the 11th Indian Conference on Computer Vision, Graphics
  and Image Processing
year: 2018
bibkey: varadarajan2018weakly
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1803.06813'}]
tags: ["Supervised"]
short_authors: Srikrishna Varadarajan, Muktabh Mayank Srivastava
---
We propose a weakly supervised method using two algorithms to predict object
bounding boxes given only an image classification dataset. First algorithm is a
simple Fully Convolutional Network (FCN) trained to classify object instances.
We use the property of FCN to return a mask for images larger than training
images to get a primary output segmentation mask during test time by passing an
image pyramid to it. We enhance the FCN output mask into final output bounding
boxes by a Convolutional Encoder-Decoder (ConvAE) viz. the second algorithm.
ConvAE is trained to localize objects on an artificially generated dataset of
output segmentation masks. We demonstrate the effectiveness of this method in
localizing objects in grocery shelves where annotating data for object
detection is hard due to variety of objects. This method can be extended to any
problem domain where collecting images of objects is easy and annotating their
coordinates is hard.