---
layout: publication
title: Region-aware Pretraining For Open-vocabulary Object Detection With Vision Transformers
authors: Dahun Kim, Anelia Angelova, Weicheng Kuo
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: kim2023region
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.07011'}]
tags: ["CVPR", "Few Shot & Zero Shot"]
short_authors: Dahun Kim, Anelia Angelova, Weicheng Kuo
---
We present Region-aware Open-vocabulary Vision Transformers (RO-ViT) - a
contrastive image-text pretraining recipe to bridge the gap between image-level
pretraining and open-vocabulary object detection. At the pretraining phase, we
propose to randomly crop and resize regions of positional embeddings instead of
using the whole image positional embeddings. This better matches the use of
positional embeddings at region-level in the detection finetuning phase. In
addition, we replace the common softmax cross entropy loss in contrastive
learning with focal loss to better learn the informative yet difficult
examples. Finally, we leverage recent advances in novel object proposals to
improve open-vocabulary detection finetuning. We evaluate our full model on the
LVIS and COCO open-vocabulary detection benchmarks and zero-shot transfer.
RO-ViT achieves a state-of-the-art 34.1 \\(AP_r\\) on LVIS, surpassing the best
existing approach by +7.8 points in addition to competitive zero-shot transfer
detection. Surprisingly, RO-ViT improves the image-level representation as well
and achieves the state of the art on 9 out of 12 metrics on COCO and Flickr
image-text retrieval benchmarks, outperforming competitive approaches with
larger models.