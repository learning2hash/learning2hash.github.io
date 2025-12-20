---
layout: publication
title: Prototype-based Aleatoric Uncertainty Quantification For Cross-modal Retrieval
authors: Hao Li, Jingkuan Song, Lianli Gao, Xiaosu Zhu, Heng Tao Shen
conference: Arxiv
year: 2023
bibkey: li2023prototype
citations: 6
additional_links: [{name: Code, url: 'https://github.com/leolee99/PAU'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.17093'}]
tags: ["Datasets", "Evaluation", "Multimodal Retrieval", "Tools & Libraries"]
short_authors: Li et al.
---
Cross-modal Retrieval methods build similarity relations between vision and
language modalities by jointly learning a common representation space. However,
the predictions are often unreliable due to the Aleatoric uncertainty, which is
induced by low-quality data, e.g., corrupt images, fast-paced videos, and
non-detailed texts. In this paper, we propose a novel Prototype-based Aleatoric
Uncertainty Quantification (PAU) framework to provide trustworthy predictions
by quantifying the uncertainty arisen from the inherent data ambiguity.
Concretely, we first construct a set of various learnable prototypes for each
modality to represent the entire semantics subspace. Then Dempster-Shafer
Theory and Subjective Logic Theory are utilized to build an evidential
theoretical framework by associating evidence with Dirichlet Distribution
parameters. The PAU model induces accurate uncertainty and reliable predictions
for cross-modal retrieval. Extensive experiments are performed on four major
benchmark datasets of MSR-VTT, MSVD, DiDeMo, and MS-COCO, demonstrating the
effectiveness of our method. The code is accessible at
https://github.com/leolee99/PAU.