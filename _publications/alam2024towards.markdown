---
layout: publication
title: 'Towards Realistic Few-shot Relation Extraction: A New Meta Dataset And Evaluation'
authors: Fahmida Alam, Md Asiful Islam, Robert Vacareanu, Mihai Surdeanu
conference: Arxiv
year: 2024
bibkey: alam2024towards
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2404.04445'}]
tags: ["Datasets", "Evaluation", "Few Shot & Zero Shot"]
short_authors: Alam et al.
---
We introduce a meta dataset for few-shot relation extraction, which includes
two datasets derived from existing supervised relation extraction datasets
NYT29 (Takanobu et al., 2019; Nayak and Ng, 2020) and WIKIDATA (Sorokin and
Gurevych, 2017) as well as a few-shot form of the TACRED dataset (Sabo et al.,
2021). Importantly, all these few-shot datasets were generated under realistic
assumptions such as: the test relations are different from any relations a
model might have seen before, limited training data, and a preponderance of
candidate relation mentions that do not correspond to any of the relations of
interest. Using this large resource, we conduct a comprehensive evaluation of
six recent few-shot relation extraction methods, and observe that no method
comes out as a clear winner. Further, the overall performance on this task is
low, indicating substantial need for future research. We release all versions
of the data, i.e., both supervised and few-shot, for future research.