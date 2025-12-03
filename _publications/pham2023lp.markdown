---
layout: publication
title: 'LP-OVOD: Open-vocabulary Object Detection By Linear Probing'
authors: Chau Pham, Truong Vu, Khoi Nguyen
conference: Arxiv
year: 2023
bibkey: pham2023lp
citations: 0
additional_links: [{name: Code, url: 'https://github.com/VinAIResearch/LP-OVOD'},
  {name: Paper, url: 'https://arxiv.org/abs/2310.17109'}]
tags: ["Datasets", "Evaluation"]
short_authors: Chau Pham, Truong Vu, Khoi Nguyen
---
This paper addresses the challenging problem of open-vocabulary object
detection (OVOD) where an object detector must identify both seen and unseen
classes in test images without labeled examples of the unseen classes in
training. A typical approach for OVOD is to use joint text-image embeddings of
CLIP to assign box proposals to their closest text label. However, this method
has a critical issue: many low-quality boxes, such as over- and
under-covered-object boxes, have the same similarity score as high-quality
boxes since CLIP is not trained on exact object location information. To
address this issue, we propose a novel method, LP-OVOD, that discards
low-quality boxes by training a sigmoid linear classifier on pseudo labels
retrieved from the top relevant region proposals to the novel text.
Experimental results on COCO affirm the superior performance of our approach
over the state of the art, achieving \(\textbf\{40.5\}\) in \(\text\{AP\}_\{novel\}\)
using ResNet50 as the backbone and without external datasets or knowing novel
classes during training. Our code will be available at
https://github.com/VinAIResearch/LP-OVOD.