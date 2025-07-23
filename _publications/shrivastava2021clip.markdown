---
layout: publication
title: 'Clip-lite: Information Efficient Visual Representation Learning With Language
  Supervision'
authors: Shrivastava Aman, Selvaraju Ramprasaath R., Naik Nikhil, Ordonez Vicente
conference: Arxiv
year: 2021
bibkey: shrivastava2021clip
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2112.07133'}]
tags: ["Datasets", "Efficiency", "Evaluation", "Few-shot & Zero-shot", "Self-Supervised"]
short_authors: Shrivastava et al.
---
We propose CLIP-Lite, an information efficient method for visual
representation learning by feature alignment with textual annotations. Compared
to the previously proposed CLIP model, CLIP-Lite requires only one negative
image-text sample pair for every positive image-text sample during the
optimization of its contrastive learning objective. We accomplish this by
taking advantage of an information efficient lower-bound to maximize the mutual
information between the two input modalities. This allows CLIP-Lite to be
trained with significantly reduced amounts of data and batch sizes while
obtaining better performance than CLIP at the same scale. We evaluate CLIP-Lite
by pretraining on the COCO-Captions dataset and testing transfer learning to
other datasets. CLIP-Lite obtains a +14.0% mAP absolute gain in performance on
Pascal VOC classification, and a +22.1% top-1 accuracy gain on ImageNet, while
being comparable or superior to other, more complex, text-supervised models.
CLIP-Lite is also superior to CLIP on image and text retrieval, zero-shot
classification, and visual grounding. Finally, we show that CLIP-Lite can
leverage language semantics to encourage bias-free visual representations that
can be used in downstream tasks. Implementation:
https://github.com/4m4n5/CLIP-Lite