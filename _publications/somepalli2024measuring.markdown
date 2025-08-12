---
layout: publication
title: Measuring Style Similarity In Diffusion Models
authors: Gowthami Somepalli, Anubhav Gupta, Kamal Gupta, Shramay Palta, Micah Goldblum,
  Jonas Geiping, Abhinav Shrivastava, Tom Goldstein
conference: Arxiv
year: 2024
bibkey: somepalli2024measuring
citations: 0
additional_links: [{name: Code, url: 'https://github.com/learn2phoenix/CSD'}, {name: Paper,
    url: 'https://arxiv.org/abs/2404.01292'}]
tags: []
short_authors: Somepalli et al.
---
Generative models are now widely used by graphic designers and artists. Prior
works have shown that these models remember and often replicate content from
their training data during generation. Hence as their proliferation increases,
it has become important to perform a database search to determine whether the
properties of the image are attributable to specific training data, every time
before a generated image is used for professional purposes. Existing tools for
this purpose focus on retrieving images of similar semantic content. Meanwhile,
many artists are concerned with style replication in text-to-image models. We
present a framework for understanding and extracting style descriptors from
images. Our framework comprises a new dataset curated using the insight that
style is a subjective property of an image that captures complex yet meaningful
interactions of factors including but not limited to colors, textures, shapes,
etc. We also propose a method to extract style descriptors that can be used to
attribute style of a generated image to the images used in the training dataset
of a text-to-image model. We showcase promising results in various style
retrieval tasks. We also quantitatively and qualitatively analyze style
attribution and matching in the Stable Diffusion model. Code and artifacts are
available at https://github.com/learn2phoenix/CSD.