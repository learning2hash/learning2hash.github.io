---
layout: publication
title: Sketch-based Image Retrieval From Millions Of Images Under Rotation, Translation
  And Scale Variations
authors: Sarthak Parui, Anurag Mittal
conference: Arxiv
year: 2015
citations: 3
bibkey: parui2015sketch
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1511.00099'}]
tags: [Applications, Indexing, Tools and Libraries]
---
Proliferation of touch-based devices has made sketch-based image retrieval
practical. While many methods exist for sketch-based object detection/image
retrieval on small datasets, relatively less work has been done on large
(web)-scale image retrieval. In this paper, we present an efficient approach
for image retrieval from millions of images based on user-drawn sketches.
Unlike existing methods for this problem which are sensitive to even
translation or scale variations, our method handles rotation, translation,
scale (i.e. a similarity transformation) and small deformations. The object
boundaries are represented as chains of connected segments and the database
images are pre-processed to obtain such chains that have a high chance of
containing the object. This is accomplished using two approaches in this work:
a) extracting long chains in contour segment networks and b) extracting
boundaries of segmented object proposals. These chains are then represented by
similarity-invariant variable length descriptors. Descriptor similarities are
computed by a fast Dynamic Programming-based partial matching algorithm. This
matching mechanism is used to generate a hierarchical k-medoids based indexing
structure for the extracted chains of all database images in an offline process
which is used to efficiently retrieve a small set of possible matched images
for query chains. Finally, a geometric verification step is employed to test
geometric consistency of multiple chain matches to improve results. Qualitative
and quantitative results clearly demonstrate superiority of the approach over
existing methods.