---
layout: publication
title: Multi-task Bidirectional Transformer Representations For Irony Detection
authors: Chiyu Zhang, Muhammad Abdul-Mageed
conference: Arxiv
year: 2019
bibkey: zhang2019multi
citations: 12
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1909.03526'}]
tags: ["Supervised"]
short_authors: Chiyu Zhang, Muhammad Abdul-Mageed
---
Supervised deep learning requires large amounts of training data. In the
context of the FIRE2019 Arabic irony detection shared task (IDAT@FIRE2019), we
show how we mitigate this need by fine-tuning the pre-trained bidirectional
encoders from transformers (BERT) on gold data in a multi-task setting. We
further improve our models by by further pre-training BERT on `in-domain' data,
thus alleviating an issue of dialect mismatch in the Google-released BERT
model. Our best model acquires 82.4 macro F1 score, and has the unique
advantage of being feature-engineering free (i.e., based exclusively on deep
learning).