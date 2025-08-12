---
layout: publication
title: 'Retail-786k: A Large-scale Dataset For Visual Entity Matching'
authors: Bianca Lamm, Janis Keuper
conference: Arxiv
year: 2023
bibkey: lamm2023retail
citations: 0
additional_links: [{name: Code, url: 'https://www.retail-786k.org/'}, {name: Paper,
    url: 'https://arxiv.org/abs/2309.17164'}]
tags: ["Datasets"]
short_authors: Bianca Lamm, Janis Keuper
---
Entity Matching (EM) defines the task of learning to group objects by
transferring semantic concepts from example groups (=entities) to unseen data.
Despite the general availability of image data in the context of many
EM-problems, most currently available EM-algorithms solely rely on (textual)
meta data. In this paper, we introduce the first publicly available large-scale
dataset for "visual entity matching", based on a production level use case in
the retail domain. Using scanned advertisement leaflets, collected over several
years from different European retailers, we provide a total of ~786k manually
annotated, high resolution product images containing ~18k different individual
retail products which are grouped into ~3k entities. The annotation of these
product entities is based on a price comparison task, where each entity forms
an equivalence class of comparable products. Following on a first baseline
evaluation, we show that the proposed "visual entity matching" constitutes a
novel learning problem which can not sufficiently be solved using standard
image based classification and retrieval algorithms. Instead, novel approaches
which allow to transfer example based visual equivalent classes to new data are
needed to address the proposed problem. The aim of this paper is to provide a
benchmark for such algorithms.
  Information about the dataset, evaluation code and download instructions are
provided under https://www.retail-786k.org/.