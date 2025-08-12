---
layout: publication
title: Diagram Image Retrieval Using Sketch-based Deep Learning And Transfer Learning
authors: Manish Bhattarai, Diane Oyen, Juan Castorena, Liping Yang, Brendt Wohlberg
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: bhattarai2020diagram
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2004.10780'}]
tags: ["CVPR", "Image Retrieval"]
short_authors: Bhattarai et al.
---
Resolution of the complex problem of image retrieval for diagram images has
yet to be reached. Deep learning methods continue to excel in the fields of
object detection and image classification applied to natural imagery. However,
the application of such methodologies applied to binary imagery remains limited
due to lack of crucial features such as textures,color and intensity
information. This paper presents a deep learning based method for image-based
search for binary patent images by taking advantage of existing large natural
image repositories for image search and sketch-based methods (Sketches are not
identical to diagrams, but they do share some characteristics; for example,
both imagery types are gray scale (binary), composed of contours, and are
lacking in texture).
  We begin by using deep learning to generate sketches from natural images for
image retrieval and then train a second deep learning model on the sketches. We
then use our small set of manually labeled patent diagram images via transfer
learning to adapt the image search from sketches of natural images to diagrams.
Our experiment results show the effectiveness of deep learning with transfer
learning for detecting near-identical copies in patent images and querying
similar images based on content.