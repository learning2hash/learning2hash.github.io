---
layout: publication
title: 'Liteembed: Adapting CLIP To Rare Classes'
authors: Aishwarya Agarwal, Srikrishna Karanam, Vineet Gandhi
conference: Arxiv
year: 2026
bibkey: agarwal2026liteembed
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2601.09661'}]
tags: ["Few Shot & Zero Shot", "Scalability", "Tools & Libraries"]
short_authors: Aishwarya Agarwal, Srikrishna Karanam, Vineet Gandhi
---
Large-scale vision-language models such as CLIP achieve strong zero-shot recognition but struggle with classes that are rarely seen during pretraining, including newly emerging entities and culturally specific categories. We introduce LiteEmbed, a lightweight framework for few-shot personalization of CLIP that enables new classes to be added without retraining its encoders. LiteEmbed performs subspace-guided optimization of text embeddings within CLIP's vocabulary, leveraging a PCA-based decomposition that disentangles coarse semantic directions from fine-grained variations. Two complementary objectives, coarse alignment and fine separation, jointly preserve global semantic consistency while enhancing discriminability among visually similar classes. Once optimized, the embeddings are plug-and-play, seamlessly substituting CLIP's original text features across classification, retrieval, segmentation, and detection tasks. Extensive experiments demonstrate substantial gains over prior methods, establishing LiteEmbed as an effective approach for adapting CLIP to underrepresented, rare, or unseen classes.