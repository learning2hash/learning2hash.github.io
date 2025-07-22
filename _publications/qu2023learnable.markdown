---
layout: publication
title: Learnable Pillar-based Re-ranking For Image-text Retrieval
authors: Qu Leigang, Liu Meng, Wang Wenjie, Zheng Zhedong, Nie Liqiang, Chua Tat-seng
conference: Proceedings of the 46th International ACM SIGIR Conference on Research
  and Development in Information Retrieval
year: 2023
bibkey: qu2023learnable
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2304.12570'}]
tags: ["Text-Retrieval", "SIGIR", "Datasets", "Re-Ranking", "Hybrid-Ann-Methods", "Evaluation"]
short_authors: Qu et al.
---
Image-text retrieval aims to bridge the modality gap and retrieve cross-modal
content based on semantic similarities. Prior work usually focuses on the
pairwise relations (i.e., whether a data sample matches another) but ignores
the higher-order neighbor relations (i.e., a matching structure among multiple
data samples). Re-ranking, a popular post-processing practice, has revealed the
superiority of capturing neighbor relations in single-modality retrieval tasks.
However, it is ineffective to directly extend existing re-ranking algorithms to
image-text retrieval. In this paper, we analyze the reason from four
perspectives, i.e., generalization, flexibility, sparsity, and asymmetry, and
propose a novel learnable pillar-based re-ranking paradigm. Concretely, we
first select top-ranked intra- and inter-modal neighbors as pillars, and then
reconstruct data samples with the neighbor relations between them and the
pillars. In this way, each sample can be mapped into a multimodal pillar space
only using similarities, ensuring generalization. After that, we design a
neighbor-aware graph reasoning module to flexibly exploit the relations and
excavate the sparse positive items within a neighborhood. We also present a
structure alignment constraint to promote cross-modal collaboration and align
the asymmetric modalities. On top of various base backbones, we carry out
extensive experiments on two benchmark datasets, i.e., Flickr30K and MS-COCO,
demonstrating the effectiveness, superiority, generalization, and
transferability of our proposed re-ranking paradigm.