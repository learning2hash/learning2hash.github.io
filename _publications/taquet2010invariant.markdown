---
layout: publication
title: "Invariant Spectral Hashing of Image Saliency Graph"
authors: Taquet Maxime, Jacques Laurent, De Vleeschouwer Christophe, Macq Benoit
conference: Arxiv
year: 2010
bibkey: taquet2010invariant
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1009.3029"}
tags: ['ARXIV', 'Graph']
---
Image hashing is the process of associating a short vector of bits to an image.
The resulting summaries are useful in many applications including image
indexing, image authentication and pattern recognition. These hashes need to be
invariant under transformations of the image that result in similar visual
content, but should drastically differ for conceptually distinct contents. This
paper proposes an image hashing method that is invariant under rotation, scaling
and translation of the image. The gist of our approach relies on the geometric
characterization of salient point distribution in the image. This is achieved by
the definition of a "saliency graph" connecting these points jointly with an
image intensity function on the graph nodes. An invariant hash is then obtained
by considering the spectrum of this function in the eigenvector basis of the
Laplacian graph, that is, its graph Fourier transform. Interestingly, this
spectrum is invariant under any relabeling of the graph nodes. The graph reveals
geometric information of the image, making the hash robust to image
transformation, yet distinct for different visual content. The efficiency of the
proposed method is assessed on a set of MRI 2-D slices and on a database of
faces.
