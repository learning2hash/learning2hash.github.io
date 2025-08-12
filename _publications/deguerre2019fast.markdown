---
layout: publication
title: Fast Object Detection In Compressed JPEG Images
authors: "Benjamin Deguerre, Cl\xE9ment Chatelain, Gilles Gasso"
conference: 2019 IEEE Intelligent Transportation Systems Conference (ITSC)
year: 2019
bibkey: deguerre2019fast
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1904.08408'}]
tags: []
short_authors: "Benjamin Deguerre, Cl\xE9ment Chatelain, Gilles Gasso"
---
Object detection in still images has drawn a lot of attention over past few
years, and with the advent of Deep Learning impressive performances have been
achieved with numerous industrial applications. Most of these deep learning
models rely on RGB images to localize and identify objects in the image.
However in some application scenarii, images are compressed either for storage
savings or fast transmission. Therefore a time consuming image decompression
step is compulsory in order to apply the aforementioned deep models. To
alleviate this drawback, we propose a fast deep architecture for object
detection in JPEG images, one of the most widespread compression format. We
train a neural network to detect objects based on the blockwise DCT (discrete
cosine transform) coefficients \{issued from\} the JPEG compression algorithm. We
modify the well-known Single Shot multibox Detector (SSD) by replacing its
first layers with one convolutional layer dedicated to process the DCT inputs.
Experimental evaluations on PASCAL VOC and industrial dataset comprising images
of road traffic surveillance show that the model is about \(2\times\) faster than
regular SSD with promising detection performances. To the best of our
knowledge, this paper is the first to address detection in compressed JPEG
images.