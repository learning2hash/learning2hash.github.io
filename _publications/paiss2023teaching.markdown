---
layout: publication
title: Teaching CLIP To Count To Ten
authors: Roni Paiss, Ariel Ephrat, Omer Tov, Shiran Zada, Inbar Mosseri, Michal Irani,
  Tali Dekel
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: paiss2023teaching
citations: 37
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2302.12066'}]
tags: ["Few Shot & Zero Shot", "ICCV", "Image Retrieval"]
short_authors: Paiss et al.
---
Large vision-language models (VLMs), such as CLIP, learn rich joint
image-text representations, facilitating advances in numerous downstream tasks,
including zero-shot classification and text-to-image generation. Nevertheless,
existing VLMs exhibit a prominent well-documented limitation - they fail to
encapsulate compositional concepts such as counting. We introduce a simple yet
effective method to improve the quantitative understanding of VLMs, while
maintaining their overall performance on common benchmarks. Specifically, we
propose a new counting-contrastive loss used to finetune a pre-trained VLM in
tandem with its original objective. Our counting loss is deployed over
automatically-created counterfactual examples, each consisting of an image and
a caption containing an incorrect object count. For example, an image depicting
three dogs is paired with the caption "Six dogs playing in the yard". Our loss
encourages discrimination between the correct caption and its counterfactual
variant which serves as a hard negative example. To the best of our knowledge,
this work is the first to extend CLIP's capabilities to object counting.
Furthermore, we introduce "CountBench" - a new image-text counting benchmark
for evaluating a model's understanding of object counting. We demonstrate a
significant improvement over state-of-the-art baseline models on this task.
Finally, we leverage our count-aware CLIP model for image retrieval and
text-conditioned image generation, demonstrating that our model can produce
specific counts of objects more reliably than existing ones.