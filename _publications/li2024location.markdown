---
layout: publication
title: Location Aware Modular Biencoder For Tourism Question Answering
authors: Haonan Li, Martin Tomko, Timothy Baldwin
conference: Arxiv
year: 2024
bibkey: li2024location
citations: 0
additional_links: [{name: Code, url: 'https://github.com/haonan-li/LAMB.'}, {name: Paper,
    url: 'https://arxiv.org/abs/2401.02187'}]
tags: [Evaluation, Datasets]
short_authors: Haonan Li, Martin Tomko, Timothy Baldwin
---
Answering real-world tourism questions that seek Point-of-Interest (POI)
recommendations is challenging, as it requires both spatial and non-spatial
reasoning, over a large candidate pool. The traditional method of encoding each
pair of question and POI becomes inefficient when the number of candidates
increases, making it infeasible for real-world applications. To overcome this,
we propose treating the QA task as a dense vector retrieval problem, where we
encode questions and POIs separately and retrieve the most relevant POIs for a
question by utilizing embedding space similarity. We use pretrained language
models (PLMs) to encode textual information, and train a location encoder to
capture spatial information of POIs. Experiments on a real-world tourism QA
dataset demonstrate that our approach is effective, efficient, and outperforms
previous methods across all metrics. Enabled by the dense retrieval
architecture, we further build a global evaluation baseline, expanding the
search space by 20 times compared to previous work. We also explore several
factors that impact on the model's performance through follow-up experiments.
Our code and model are publicly available at https://github.com/haonan-li/LAMB.