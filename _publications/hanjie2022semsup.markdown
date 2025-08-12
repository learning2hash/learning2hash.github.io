---
layout: publication
title: 'Semsup: Semantic Supervision For Simple And Scalable Zero-shot Generalization'
authors: Austin W. Hanjie, Ameet Deshpande, Karthik Narasimhan
conference: Arxiv
year: 2022
bibkey: hanjie2022semsup
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2202.13100'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Austin W. Hanjie, Ameet Deshpande, Karthik Narasimhan
---
Zero-shot learning is the problem of predicting instances over classes not
seen during training. One approach to zero-shot learning is providing auxiliary
class information to the model. Prior work along this vein have largely used
expensive per-instance annotation or singular class-level descriptions, but
per-instance descriptions are hard to scale and single class descriptions may
not be rich enough. Furthermore, these works have used natural-language
descriptions exclusively, simple bi-encoders models, and modality or
task-specific methods. These approaches have several limitations: text
supervision may not always be available or optimal and bi-encoders may only
learn coarse relations between inputs and class descriptions. In this work, we
present SemSup, a novel approach that uses (1) a scalable multiple description
sampling method which improves performance over single descriptions, (2)
alternative description formats such as JSON that are easy to generate and
outperform text on certain settings, and (3) hybrid lexical-semantic similarity
to leverage fine-grained information in class descriptions. We demonstrate the
effectiveness of SemSup across four datasets, two modalities, and three
generalization settings. For example, across text and image datasets, SemSup
increases unseen class generalization accuracy by 15 points on average compared
to the closest baseline.