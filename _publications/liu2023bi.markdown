---
layout: publication
title: Bi-directional Training for Composed Image Retrieval via Text Prompt Learning
authors: Liu et al.
conference: 2024 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
year: 2024
bibkey: liu2023bi
citations: 13
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2303.16604'}]
tags: ["Image-Retrieval"]
---
Composed image retrieval searches for a target image based on a multi-modal
user query comprised of a reference image and modification text describing the
desired changes. Existing approaches to solving this challenging task learn a
mapping from the (reference image, modification text)-pair to an image
embedding that is then matched against a large image corpus. One area that has
not yet been explored is the reverse direction, which asks the question, what
reference image when modified as described by the text would produce the given
target image? In this work we propose a bi-directional training scheme that
leverages such reversed queries and can be applied to existing composed image
retrieval architectures with minimum changes, which improves the performance of
the model. To encode the bi-directional query we prepend a learnable token to
the modification text that designates the direction of the query and then
finetune the parameters of the text embedding module. We make no other changes
to the network architecture. Experiments on two standard datasets show that our
novel approach achieves improved performance over a baseline BLIP-based model
that itself already achieves competitive performance. Our code is released at
https://github.com/Cuberick-Orion/Bi-Blip4CIR.