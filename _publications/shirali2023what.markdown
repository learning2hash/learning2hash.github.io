---
layout: publication
title: What Makes Imagenet Look Unlike LAION
authors: Ali Shirali, Moritz Hardt
conference: Arxiv
year: 2023
bibkey: shirali2023what
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2306.15769'}]
tags: ["Datasets", "Image Retrieval"]
short_authors: Ali Shirali, Moritz Hardt
---
ImageNet was famously created from Flickr image search results. What if we
recreated ImageNet instead by searching the massive LAION dataset based on
image captions alone? In this work, we carry out this counterfactual
investigation. We find that the resulting ImageNet recreation, which we call
LAIONet, looks distinctly unlike the original. Specifically, the intra-class
similarity of images in the original ImageNet is dramatically higher than it is
for LAIONet. Consequently, models trained on ImageNet perform significantly
worse on LAIONet. We propose a rigorous explanation for the discrepancy in
terms of a subtle, yet important, difference in two plausible causal
data-generating processes for the respective datasets, that we support with
systematic experimentation. In a nutshell, searching based on an image caption
alone creates an information bottleneck that mitigates the selection bias
otherwise present in image-based filtering. Our explanation formalizes a
long-held intuition in the community that ImageNet images are stereotypical,
unnatural, and overly simple representations of the class category. At the same
time, it provides a simple and actionable takeaway for future dataset creation
efforts.