---
layout: publication
title: 'FOR: Finetuning For Object Level Open Vocabulary Image Retrieval'
authors: Hila Levi, Guy Heller, Dan Levi
conference: Arxiv
year: 2024
bibkey: levi2024for
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.18806'}]
tags: [Evaluation, Supervised, Image Retrieval, Re-ranking, Efficiency, Datasets,
  Tools & Libraries]
short_authors: Hila Levi, Guy Heller, Dan Levi
---
As working with large datasets becomes standard, the task of accurately
retrieving images containing objects of interest by an open set textual query
gains practical importance. The current leading approach utilizes a pre-trained
CLIP model without any adaptation to the target domain, balancing accuracy and
efficiency through additional post-processing. In this work, we propose FOR:
Finetuning for Object-centric Open-vocabulary Image Retrieval, which allows
finetuning on a target dataset using closed-set labels while keeping the
visual-language association crucial for open vocabulary retrieval. FOR is based
on two design elements: a specialized decoder variant of the CLIP head
customized for the intended task, and its coupling within a multi-objective
training framework. Together, these design choices result in a significant
increase in accuracy, showcasing improvements of up to 8 mAP@50 points over
SoTA across three datasets. Additionally, we demonstrate that FOR is also
effective in a semi-supervised setting, achieving impressive results even when
only a small portion of the dataset is labeled.