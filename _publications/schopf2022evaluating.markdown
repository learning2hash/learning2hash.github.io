---
layout: publication
title: 'Evaluating Unsupervised Text Classification: Zero-shot And Similarity-based
  Approaches'
authors: Tim Schopf, Daniel Braun, Florian Matthes
conference: Proceedings of the 2022 6th International Conference on Natural Language
  Processing and Information Retrieval
year: 2022
bibkey: schopf2022evaluating
citations: 30
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.16285'}]
tags: ["Evaluation", "Few Shot & Zero Shot", "Unsupervised"]
short_authors: Tim Schopf, Daniel Braun, Florian Matthes
---
Text classification of unseen classes is a challenging Natural Language
Processing task and is mainly attempted using two different types of
approaches. Similarity-based approaches attempt to classify instances based on
similarities between text document representations and class description
representations. Zero-shot text classification approaches aim to generalize
knowledge gained from a training task by assigning appropriate labels of
unknown classes to text documents. Although existing studies have already
investigated individual approaches to these categories, the experiments in
literature do not provide a consistent comparison. This paper addresses this
gap by conducting a systematic evaluation of different similarity-based and
zero-shot approaches for text classification of unseen classes. Different
state-of-the-art approaches are benchmarked on four text classification
datasets, including a new dataset from the medical domain. Additionally, novel
SimCSE and SBERT-based baselines are proposed, as other baselines used in
existing work yield weak classification results and are easily outperformed.
Finally, the novel similarity-based Lbl2TransformerVec approach is presented,
which outperforms previous state-of-the-art approaches in unsupervised text
classification. Our experiments show that similarity-based approaches
significantly outperform zero-shot approaches in most cases. Additionally,
using SimCSE or SBERT embeddings instead of simpler text representations
increases similarity-based classification results even further.