---
layout: publication
title: Universal Model For Multi-domain Medical Image Retrieval
authors: Yang Feng, Yubao Liu, Jiebo Luo
conference: Arxiv
year: 2020
bibkey: feng2020universal
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2007.08628'}]
tags: ["Datasets", "Image Retrieval", "Multimodal Retrieval"]
short_authors: Yang Feng, Yubao Liu, Jiebo Luo
---
Medical Image Retrieval (MIR) helps doctors quickly find similar patients'
data, which can considerably aid the diagnosis process. MIR is becoming
increasingly helpful due to the wide use of digital imaging modalities and the
growth of the medical image repositories. However, the popularity of various
digital imaging modalities in hospitals also poses several challenges to MIR.
Usually, one image retrieval model is only trained to handle images from one
modality or one source. When there are needs to retrieve medical images from
several sources or domains, multiple retrieval models need to be maintained,
which is cost ineffective. In this paper, we study an important but unexplored
task: how to train one MIR model that is applicable to medical images from
multiple domains? Simply fusing the training data from multiple domains cannot
solve this problem because some domains become over-fit sooner when trained
together using existing methods. Therefore, we propose to distill the knowledge
in multiple specialist MIR models into a single multi-domain MIR model via
universal embedding to solve this problem. Using skin disease, x-ray, and
retina image datasets, we validate that our proposed universal model can
effectively accomplish multi-domain MIR.