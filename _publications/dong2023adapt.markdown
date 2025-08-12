---
layout: publication
title: Adapt And Align To Improve Zero-shot Sketch-based Image Retrieval
authors: Shiyin Dong, Mingrui Zhu, Nannan Wang, Xinbo Gao
conference: Arxiv
year: 2023
bibkey: dong2023adapt
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.05144'}]
tags: ["Few Shot & Zero Shot", "Image Retrieval"]
short_authors: Dong et al.
---
Zero-shot sketch-based image retrieval (ZS-SBIR) is challenging due to the
cross-domain nature of sketches and photos, as well as the semantic gap between
seen and unseen image distributions. Previous methods fine-tune pre-trained
models with various side information and learning strategies to learn a compact
feature space that is shared between the sketch and photo domains and bridges
seen and unseen classes. However, these efforts are inadequate in adapting
domains and transferring knowledge from seen to unseen classes. In this paper,
we present an effective ``Adapt and Align'' approach to address the key
challenges. Specifically, we insert simple and lightweight domain adapters to
learn new abstract concepts of the sketch domain and improve cross-domain
representation capabilities. Inspired by recent advances in image-text
foundation models (e.g., CLIP) on zero-shot scenarios, we explicitly align the
learned image embedding with a more semantic text embedding to achieve the
desired knowledge transfer from seen to unseen classes. Extensive experiments
on three benchmark datasets and two popular backbones demonstrate the
superiority of our method in terms of retrieval accuracy and flexibility.