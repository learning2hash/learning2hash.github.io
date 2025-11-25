---
layout: publication
title: Hyperbolic Image-text Representations
authors: Karan Desai, Maximilian Nickel, Tanmay Rajpurohit, Justin Johnson, Ramakrishna
  Vedantam
conference: Arxiv
year: 2023
bibkey: desai2023hyperbolic
citations: 2
additional_links: [{name: Code, url: 'https://www.github.com/facebookresearch/meru'},
  {name: Paper, url: 'https://arxiv.org/abs/2304.09172'}]
tags: ["Image Retrieval", "Multimodal Retrieval", "Scalability", "Self-Supervised"]
short_authors: Desai et al.
---
Visual and linguistic concepts naturally organize themselves in a hierarchy,
where a textual concept "dog" entails all images that contain dogs. Despite
being intuitive, current large-scale vision and language models such as CLIP do
not explicitly capture such hierarchy. We propose MERU, a contrastive model
that yields hyperbolic representations of images and text. Hyperbolic spaces
have suitable geometric properties to embed tree-like data, so MERU can better
capture the underlying hierarchy in image-text datasets. Our results show that
MERU learns a highly interpretable and structured representation space while
being competitive with CLIP's performance on standard multi-modal tasks like
image classification and image-text retrieval. Our code and models are
available at https://www.github.com/facebookresearch/meru