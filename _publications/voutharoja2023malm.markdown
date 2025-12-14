---
layout: publication
title: 'MALM: Mask Augmentation Based Local Matching For Food-recipe Retrieval'
authors: Bhanu Prakash Voutharoja, Peng Wang, Lei Wang, Vivienne Guan
conference: Arxiv
year: 2023
bibkey: voutharoja2023malm
citations: 2
additional_links: [{name: Code, url: 'https://github.com/MyFoodChoice/MALM_Mask_Augmentation_based_Local_Matching-_for-_Food_Recipe_Retrieval'},
  {name: Paper, url: 'https://arxiv.org/abs/2305.11327'}]
tags: [Supervised, Datasets]
short_authors: Voutharoja et al.
---
Image-to-recipe retrieval is a challenging vision-to-language task of
significant practical value. The main challenge of the task lies in the
ultra-high redundancy in the long recipe and the large variation reflected in
both food item combination and food item appearance. A de-facto idea to address
this task is to learn a shared feature embedding space in which a food image is
aligned better to its paired recipe than other recipes. However, such
supervised global matching is prone to supervision collapse, i.e., only partial
information that is necessary for distinguishing training pairs can be
identified, while other information that is potentially useful in
generalization could be lost. To mitigate such a problem, we propose a
mask-augmentation-based local matching network (MALM), where an image-text
matching module and a masked self-distillation module benefit each other
mutually to learn generalizable cross-modality representations. On one hand, we
perform local matching between the tokenized representations of image and text
to locate fine-grained cross-modality correspondence explicitly. We involve
representations of masked image patches in this process to alleviate
overfitting resulting from local matching especially when some food items are
underrepresented. On the other hand, predicting the hidden representations of
the masked patches through self-distillation helps to learn general-purpose
image representations that are expected to generalize better. And the
multi-task nature of the model enables the representations of masked patches to
be text-aware and thus facilitates the lost information reconstruction.
Experimental results on Recipe1M dataset show our method can clearly outperform
state-of-the-art (SOTA) methods. Our code will be available at
https://github.com/MyFoodChoice/MALM_Mask_Augmentation_based_Local_Matching-_for-_Food_Recipe_Retrieval