---
layout: publication
title: "Using Text to Teach Image Retrieval"
authors: Dong Haoyu, Wang Ze, Qiu Qiang, Sapiro Guillermo
conference: "Arxiv"
year: 2020
bibkey: dong2020using
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2011.09928"}
tags: ['ARXIV', 'Graph', 'Image Retrieval']
---
Image retrieval relies heavily on the quality of the data modeling and the
distance measurement in the feature space. Building on the concept of image
manifold, we first propose to represent the feature space of images, learned via
neural networks, as a graph. Neighborhoods in the feature space are now defined
by the geodesic distance between images, represented as graph vertices or
manifold samples. When limited images are available, this manifold is sparsely
sampled, making the geodesic computation and the corresponding retrieval harder.
To address this, we augment the manifold samples with geometrically aligned
text, thereby using a plethora of sentences to teach us about images. In
addition to extensive results on standard datasets illustrating the power of
text to help in image retrieval, a new public dataset based on CLEVR is
introduced to quantify the semantic similarity between visual data and text
data. The experimental results show that the joint embedding manifold is a
robust representation, allowing it to be a better basis to perform image
retrieval given only an image and a textual instruction on the desired
modifications over the image
