---
layout: publication
title: Lifelong Person Search
authors: Jae-won Yang, Seungbin Hong, Jae-young Sim
conference: IEEE Access
year: 2025
bibkey: yang2024lifelong
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2407.21252'}]
tags: []
short_authors: Jae-won Yang, Seungbin Hong, Jae-young Sim
---
Person search is the task to localize a query person in gallery datasets of scene images. Existing methods have been mainly developed to handle a single target dataset only, however diverse datasets are continuously given in practical applications of person search. In such cases, they suffer from the catastrophic knowledge forgetting in the old datasets when trained on new datasets. In this paper, we first introduce a novel problem of lifelong person search (LPS) where the model is incrementally trained on the new datasets while preserving the knowledge learned in the old datasets. We propose an end-to-end LPS framework that facilitates the knowledge distillation to enforce the consistency learning between the old and new models by utilizing the prototype features of the foreground persons as well as the hard background proposals in the old domains. Moreover, we also devise the rehearsal-based instance matching to further improve the discrimination ability in the old domains by using the unlabeled person instances additionally. Experimental results demonstrate that the proposed method achieves significantly superior performance of both the detection and re-identification to preserve the knowledge learned in the old domains compared with the existing methods.