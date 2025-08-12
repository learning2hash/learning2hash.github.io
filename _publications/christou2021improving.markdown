---
layout: publication
title: Improving Distantly-supervised Relation Extraction Through Bert-based Label
  & Instance Embeddings
authors: Despina Christou, Grigorios Tsoumakas
conference: Arxiv
year: 2021
bibkey: christou2021improving
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2102.01156'}]
tags: ["Supervised"]
short_authors: Despina Christou, Grigorios Tsoumakas
---
Distantly-supervised relation extraction (RE) is an effective method to scale
RE to large corpora but suffers from noisy labels. Existing approaches try to
alleviate noise through multi-instance learning and by providing additional
information, but manage to recognize mainly the top frequent relations,
neglecting those in the long-tail. We propose REDSandT (Relation Extraction
with Distant Supervision and Transformers), a novel distantly-supervised
transformer-based RE method, that manages to capture a wider set of relations
through highly informative instance and label embeddings for RE, by exploiting
BERT's pre-trained model, and the relationship between labels and entities,
respectively. We guide REDSandT to focus solely on relational tokens by
fine-tuning BERT on a structured input, including the sub-tree connecting an
entity pair and the entities' types. Using the extracted informative vectors,
we shape label embeddings, which we also use as attention mechanism over
instances to further reduce noise. Finally, we represent sentences by
concatenating relation and instance embeddings. Experiments in the NYT-10
dataset show that REDSandT captures a broader set of relations with higher
confidence, achieving state-of-the-art AUC (0.424).