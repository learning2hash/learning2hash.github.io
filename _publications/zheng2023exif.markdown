---
layout: publication
title: 'EXIF As Language: Learning Cross-modal Associations Between Images And Camera
  Metadata'
authors: Chenhao Zheng, Ayush Shrivastava, Andrew Owens
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: zheng2023exif
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2301.04647'}]
tags: ["CVPR"]
short_authors: Chenhao Zheng, Ayush Shrivastava, Andrew Owens
---
We learn a visual representation that captures information about the camera
that recorded a given photo. To do this, we train a multimodal embedding
between image patches and the EXIF metadata that cameras automatically insert
into image files. Our model represents this metadata by simply converting it to
text and then processing it with a transformer. The features that we learn
significantly outperform other self-supervised and supervised features on
downstream image forensics and calibration tasks. In particular, we
successfully localize spliced image regions "zero shot" by clustering the
visual embeddings for all of the patches within an image.