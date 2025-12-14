---
layout: publication
title: Coarse-to-fine Alignment Makes Better Speech-image Retrieval
authors: Lifeng Zhou, Yuke Li
conference: Arxiv
year: 2024
bibkey: zhou2024coarse
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.13119'}]
tags: [Evaluation, Image Retrieval, Few-shot & Zero-shot, Datasets, Tools & Libraries]
short_authors: Lifeng Zhou, Yuke Li
---
In this paper, we propose a novel framework for speech-image retrieval. We
utilize speech-image contrastive (SIC) learning tasks to align speech and image
representations at a coarse level and speech-image matching (SIM) learning
tasks to further refine the fine-grained cross-modal alignment. SIC and SIM
learning tasks are jointly trained in a unified manner. To optimize the
learning process, we utilize an embedding queue that facilitates efficient
sampling of high-quality and diverse negative representations during SIC
learning. Additionally, it enhances the learning of SIM tasks by effectively
mining hard negatives based on contrastive similarities calculated in SIC
tasks. To further optimize learning under noisy supervision, we incorporate
momentum distillation into the training process. Experimental results show that
our framework outperforms the state-of-the-art method by more than 4% in R@1 on
two benchmark datasets for the speech-image retrieval tasks. Moreover, as
observed in zero-shot experiments, our framework demonstrates excellent
generalization capabilities.