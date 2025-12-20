---
layout: publication
title: Object Discovery Via Contrastive Learning For Weakly Supervised Object Detection
authors: Jinhwan Seo, Wonho Bae, Danica J. Sutherland, Junhyug Noh, Daijin Kim
conference: Lecture Notes in Computer Science
year: 2022
bibkey: seo2022object
citations: 33
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2208.07576'}]
tags: ["Distance Metric Learning", "Self-Supervised", "Supervised"]
short_authors: Seo et al.
---
Weakly Supervised Object Detection (WSOD) is a task that detects objects in
an image using a model trained only on image-level annotations. Current
state-of-the-art models benefit from self-supervised instance-level
supervision, but since weak supervision does not include count or location
information, the most common ``argmax'' labeling method often ignores many
instances of objects. To alleviate this issue, we propose a novel multiple
instance labeling method called object discovery. We further introduce a new
contrastive loss under weak supervision where no instance-level information is
available for sampling, called weakly supervised contrastive loss (WSCL). WSCL
aims to construct a credible similarity threshold for object discovery by
leveraging consistent features for embedding vectors in the same class. As a
result, we achieve new state-of-the-art results on MS-COCO 2014 and 2017 as
well as PASCAL VOC 2012, and competitive results on PASCAL VOC 2007.