---
layout: publication
title: Sketch-based Medical Image Retrieval
authors: Kobayashi et al.
conference: Arxiv
year: 2023
bibkey: kobayashi2023sketch
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.03633'}]
tags: [Image Retrieval]
---
The amount of medical images stored in hospitals is increasing faster than
ever; however, utilizing the accumulated medical images has been limited. This
is because existing content-based medical image retrieval (CBMIR) systems
usually require example images to construct query vectors; nevertheless,
example images cannot always be prepared. Besides, there can be images with
rare characteristics that make it difficult to find similar example images,
which we call isolated samples. Here, we introduce a novel sketch-based medical
image retrieval (SBMIR) system that enables users to find images of interest
without example images. The key idea lies in feature decomposition of medical
images, whereby the entire feature of a medical image can be decomposed into
and reconstructed from normal and abnormal features. By extending this idea,
our SBMIR system provides an easy-to-use two-step graphical user interface:
users first select a template image to specify a normal feature and then draw a
semantic sketch of the disease on the template image to represent an abnormal
feature. Subsequently, it integrates the two kinds of input to construct a
query vector and retrieves reference images with the closest reference vectors.
Using two datasets, ten healthcare professionals with various clinical
backgrounds participated in the user test for evaluation. As a result, our
SBMIR system enabled users to overcome previous challenges, including image
retrieval based on fine-grained image characteristics, image retrieval without
example images, and image retrieval for isolated samples. Our SBMIR system
achieves flexible medical image retrieval on demand, thereby expanding the
utility of medical image databases.