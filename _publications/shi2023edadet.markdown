---
layout: publication
title: 'Edadet: Open-vocabulary Object Detection Using Early Dense Alignment'
authors: Cheng Shi, Sibei Yang
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: shi2023edadet
citations: 20
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2309.01151'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "ICCV"]
short_authors: Cheng Shi, Sibei Yang
---
Vision-language models such as CLIP have boosted the performance of
open-vocabulary object detection, where the detector is trained on base
categories but required to detect novel categories. Existing methods leverage
CLIP's strong zero-shot recognition ability to align object-level embeddings
with textual embeddings of categories. However, we observe that using CLIP for
object-level alignment results in overfitting to base categories, i.e., novel
categories most similar to base categories have particularly poor performance
as they are recognized as similar base categories. In this paper, we first
identify that the loss of critical fine-grained local image semantics hinders
existing methods from attaining strong base-to-novel generalization. Then, we
propose Early Dense Alignment (EDA) to bridge the gap between generalizable
local semantics and object-level prediction. In EDA, we use object-level
supervision to learn the dense-level rather than object-level alignment to
maintain the local fine-grained semantics. Extensive experiments demonstrate
our superior performance to competing approaches under the same strict setting
and without using external training resources, i.e., improving the +8.4% novel
box AP50 on COCO and +3.9% rare mask AP on LVIS.