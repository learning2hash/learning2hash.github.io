---
layout: publication
title: Decomposing Normal And Abnormal Features Of Medical Images Into Discrete Latent
  Codes For Content-based Image Retrieval
authors: Kazuma Kobayashi, Ryuichiro Hataya, Yusuke Kurose, Mototaka Miyake, Masamichi
  Takahashi, Akiko Nakagawa, Tatsuya Harada, Ryuji Hamamoto
conference: Arxiv
year: 2021
bibkey: kobayashi2021decomposing
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2103.12328'}]
tags: [Image Retrieval, Similarity Search, Datasets, Quantization, Hashing Methods]
short_authors: Kobayashi et al.
---
In medical imaging, the characteristics purely derived from a disease should
reflect the extent to which abnormal findings deviate from the normal features.
Indeed, physicians often need corresponding images without abnormal findings of
interest or, conversely, images that contain similar abnormal findings
regardless of normal anatomical context. This is called comparative diagnostic
reading of medical images, which is essential for a correct diagnosis. To
support comparative diagnostic reading, content-based image retrieval (CBIR),
which can selectively utilize normal and abnormal features in medical images as
two separable semantic components, will be useful. Therefore, we propose a
neural network architecture to decompose the semantic components of medical
images into two latent codes: normal anatomy code and abnormal anatomy code.
The normal anatomy code represents normal anatomies that should have existed if
the sample is healthy, whereas the abnormal anatomy code attributes to abnormal
changes that reflect deviation from the normal baseline. These latent codes are
discretized through vector quantization to enable binary hashing, which can
reduce the computational burden at the time of similarity search. By
calculating the similarity based on either normal or abnormal anatomy codes or
the combination of the two codes, our algorithm can retrieve images according
to the selected semantic component from a dataset consisting of brain magnetic
resonance images of gliomas. Our CBIR system qualitatively and quantitatively
achieves remarkable results.