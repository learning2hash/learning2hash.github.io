---
layout: publication
title: Adaptive Fine-grained Sketch-based Image Retrieval
authors: Bhunia Ayan Kumar, Sain Aneeshan, Shah Parth, Gupta Animesh, Chowdhury Pinaki
  Nath, Xiang Tao, Song Yi-zhe
conference: Lecture Notes in Computer Science
year: 2022
bibkey: bhunia2022adaptive
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.01723'}]
tags: ["Datasets", "Distance Metric Learning", "Few-shot & Zero-shot", "Image Retrieval"]
short_authors: Bhunia et al.
---
The recent focus on Fine-Grained Sketch-Based Image Retrieval (FG-SBIR) has
shifted towards generalising a model to new categories without any training
data from them. In real-world applications, however, a trained FG-SBIR model is
often applied to both new categories and different human sketchers, i.e.,
different drawing styles. Although this complicates the generalisation problem,
fortunately, a handful of examples are typically available, enabling the model
to adapt to the new category/style. In this paper, we offer a novel perspective
-- instead of asking for a model that generalises, we advocate for one that
quickly adapts, with just very few samples during testing (in a few-shot
manner). To solve this new problem, we introduce a novel model-agnostic
meta-learning (MAML) based framework with several key modifications: (1) As a
retrieval task with a margin-based contrastive loss, we simplify the MAML
training in the inner loop to make it more stable and tractable. (2) The margin
in our contrastive loss is also meta-learned with the rest of the model. (3)
Three additional regularisation losses are introduced in the outer loop, to
make the meta-learned FG-SBIR model more effective for category/style
adaptation. Extensive experiments on public datasets suggest a large gain over
generalisation and zero-shot based approaches, and a few strong few-shot
baselines.