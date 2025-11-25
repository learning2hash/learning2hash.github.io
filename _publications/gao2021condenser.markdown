---
layout: publication
title: 'Condenser: A Pre-training Architecture For Dense Retrieval'
authors: Luyu Gao, Jamie Callan
conference: Arxiv
year: 2021
bibkey: gao2021condenser
citations: 8
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2104.08253'}]
tags: ["Text Retrieval"]
short_authors: Luyu Gao, Jamie Callan
---
Pre-trained Transformer language models (LM) have become go-to text
representation encoders. Prior research fine-tunes deep LMs to encode text
sequences such as sentences and passages into single dense vector
representations for efficient text comparison and retrieval. However, dense
encoders require a lot of data and sophisticated techniques to effectively
train and suffer in low data situations. This paper finds a key reason is that
standard LMs' internal attention structure is not ready-to-use for dense
encoders, which needs to aggregate text information into the dense
representation. We propose to pre-train towards dense encoder with a novel
Transformer architecture, Condenser, where LM prediction CONditions on DENSE
Representation. Our experiments show Condenser improves over standard LM by
large margins on various text retrieval and similarity tasks.