---
layout: publication
title: Texture Memory-augmented Deep Patch-based Image Inpainting
authors: Rui Xu, Minghao Guo, Jiaqi Wang, Xiaoxiao Li, Bolei Zhou, Chen Change Loy
conference: IEEE Transactions on Image Processing
year: 2020
bibkey: xu2020texture
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2009.13240'}]
tags: ["Datasets", "Evaluation"]
short_authors: Xu et al.
---
Patch-based methods and deep networks have been employed to tackle image
inpainting problem, with their own strengths and weaknesses. Patch-based
methods are capable of restoring a missing region with high-quality texture
through searching nearest neighbor patches from the unmasked regions. However,
these methods bring problematic contents when recovering large missing regions.
Deep networks, on the other hand, show promising results in completing large
regions. Nonetheless, the results often lack faithful and sharp details that
resemble the surrounding area. By bringing together the best of both paradigms,
we propose a new deep inpainting framework where texture generation is guided
by a texture memory of patch samples extracted from unmasked regions. The
framework has a novel design that allows texture memory retrieval to be trained
end-to-end with the deep inpainting network. In addition, we introduce a patch
distribution loss to encourage high-quality patch synthesis. The proposed
method shows superior performance both qualitatively and quantitatively on
three challenging image benchmarks, i.e., Places, CelebA-HQ, and Paris
Street-View datasets.