---
layout: publication
title: Query-guided Attention In Vision Transformers For Localizing Objects Using
  A Single Sketch
authors: Aditay Tripathi, Anand Mishra, Anirban Chakraborty
conference: Arxiv
year: 2023
bibkey: tripathi2023query
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.08784'}]
tags: []
short_authors: Aditay Tripathi, Anand Mishra, Anirban Chakraborty
---
In this work, we investigate the problem of sketch-based object localization
on natural images, where given a crude hand-drawn sketch of an object, the goal
is to localize all the instances of the same object on the target image. This
problem proves difficult due to the abstract nature of hand-drawn sketches,
variations in the style and quality of sketches, and the large domain gap
existing between the sketches and the natural images. To mitigate these
challenges, existing works proposed attention-based frameworks to incorporate
query information into the image features. However, in these works, the query
features are incorporated after the image features have already been
independently learned, leading to inadequate alignment. In contrast, we propose
a sketch-guided vision transformer encoder that uses cross-attention after each
block of the transformer-based image encoder to learn query-conditioned image
features leading to stronger alignment with the query sketch. Further, at the
output of the decoder, the object and the sketch features are refined to bring
the representation of relevant objects closer to the sketch query and thereby
improve the localization. The proposed model also generalizes to the object
categories not seen during training, as the target image features learned by
our method are query-aware. Our localization framework can also utilize
multiple sketch queries via a trainable novel sketch fusion strategy. The model
is evaluated on the images from the public object detection benchmark, namely
MS-COCO, using the sketch queries from QuickDraw! and Sketchy datasets.
Compared with existing localization methods, the proposed approach gives a
\(6.6%\) and \(8.0%\) improvement in mAP for seen objects using sketch queries
from QuickDraw! and Sketchy datasets, respectively, and a \(12.2%\) improvement
in AP@50 for large objects that are `unseen' during training.