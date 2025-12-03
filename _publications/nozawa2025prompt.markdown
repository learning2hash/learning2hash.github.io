---
layout: publication
title: Prompt-guided Attention Head Selection For Focus-oriented Image Retrieval
authors: Yuji Nozawa, Yu-Chieh Lin, Kazumoto Nakamura, Youyang Ng
conference: 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2025
bibkey: nozawa2025prompt
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.01348'}]
tags: ["CVPR", "Datasets", "Evaluation", "Image Retrieval"]
short_authors: Nozawa et al.
---
The goal of this paper is to enhance pretrained Vision Transformer (ViT)
models for focus-oriented image retrieval with visual prompting. In real-world
image retrieval scenarios, both query and database images often exhibit
complexity, with multiple objects and intricate backgrounds. Users often want
to retrieve images with specific object, which we define as the Focus-Oriented
Image Retrieval (FOIR) task. While a standard image encoder can be employed to
extract image features for similarity matching, it may not perform optimally in
the multi-object-based FOIR task. This is because each image is represented by
a single global feature vector. To overcome this, a prompt-based image
retrieval solution is required. We propose an approach called Prompt-guided
attention Head Selection (PHS) to leverage the head-wise potential of the
multi-head attention mechanism in ViT in a promptable manner. PHS selects
specific attention heads by matching their attention maps with user's visual
prompts, such as a point, box, or segmentation. This empowers the model to
focus on specific object of interest while preserving the surrounding visual
context. Notably, PHS does not necessitate model re-training and avoids any
image alteration. Experimental results show that PHS substantially improves
performance on multiple datasets, offering a practical and training-free
solution to enhance model performance in the FOIR task.