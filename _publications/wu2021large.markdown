---
layout: publication
title: A Large-scale Benchmark For Food Image Segmentation
authors: Xiongwei Wu, Xin Fu, Ying Liu, Ee-Peng Lim, Steven C. H. Hoi, Qianru Sun
conference: Proceedings of the 29th ACM International Conference on Multimedia
year: 2021
bibkey: wu2021large
citations: 55
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.05409'}]
tags: ["Datasets", "Evaluation", "Scalability"]
short_authors: Wu et al.
---
Food image segmentation is a critical and indispensible task for developing
health-related applications such as estimating food calories and nutrients.
Existing food image segmentation models are underperforming due to two reasons:
(1) there is a lack of high quality food image datasets with fine-grained
ingredient labels and pixel-wise location masks -- the existing datasets either
carry coarse ingredient labels or are small in size; and (2) the complex
appearance of food makes it difficult to localize and recognize ingredients in
food images, e.g., the ingredients may overlap one another in the same image,
and the identical ingredient may appear distinctly in different food images. In
this work, we build a new food image dataset FoodSeg103 (and its extension
FoodSeg154) containing 9,490 images. We annotate these images with 154
ingredient classes and each image has an average of 6 ingredient labels and
pixel-wise masks. In addition, we propose a multi-modality pre-training
approach called ReLeM that explicitly equips a segmentation model with rich and
semantic food knowledge. In experiments, we use three popular semantic
segmentation methods (i.e., Dilated Convolution based, Feature Pyramid based,
and Vision Transformer based) as baselines, and evaluate them as well as ReLeM
on our new datasets. We believe that the FoodSeg103 (and its extension
FoodSeg154) and the pre-trained models using ReLeM can serve as a benchmark to
facilitate future works on fine-grained food image understanding. We make all
these datasets and methods public at
https://xiongweiwu.github.io/foodseg103.html.