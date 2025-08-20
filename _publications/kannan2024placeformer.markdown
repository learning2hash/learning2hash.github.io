---
layout: publication
title: 'Placeformer: Transformer-based Visual Place Recognition Using Multi-scale
  Patch Selection And Fusion'
authors: Shyam Sundar Kannan, Byung-Cheol Min
conference: IEEE Robotics and Automation Letters
year: 2024
bibkey: kannan2024placeformer
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.13082'}]
tags: [Efficiency, Image Retrieval, Evaluation, Datasets]
short_authors: Shyam Sundar Kannan, Byung-Cheol Min
---
Visual place recognition is a challenging task in the field of computer
vision, and autonomous robotics and vehicles, which aims to identify a location
or a place from visual inputs. Contemporary methods in visual place recognition
employ convolutional neural networks and utilize every region within the image
for the place recognition task. However, the presence of dynamic and
distracting elements in the image may impact the effectiveness of the place
recognition process. Therefore, it is meaningful to focus on task-relevant
regions of the image for improved recognition. In this paper, we present
PlaceFormer, a novel transformer-based approach for visual place recognition.
PlaceFormer employs patch tokens from the transformer to create global image
descriptors, which are then used for image retrieval. To re-rank the retrieved
images, PlaceFormer merges the patch tokens from the transformer to form
multi-scale patches. Utilizing the transformer's self-attention mechanism, it
selects patches that correspond to task-relevant areas in an image. These
selected patches undergo geometric verification, generating similarity scores
across different patch sizes. Subsequently, spatial scores from each patch size
are fused to produce a final similarity score. This score is then used to
re-rank the images initially retrieved using global image descriptors.
Extensive experiments on benchmark datasets demonstrate that PlaceFormer
outperforms several state-of-the-art methods in terms of accuracy and
computational efficiency, requiring less time and memory.