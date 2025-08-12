---
layout: publication
title: De-identification Of Privacy-related Entities In Job Postings
authors: "Kristian N\xF8rgaard Jensen, Mike Zhang, Barbara Plank"
conference: Arxiv
year: 2021
bibkey: jensen2021de
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.11223'}]
tags: []
short_authors: "Kristian N\xF8rgaard Jensen, Mike Zhang, Barbara Plank"
---
De-identification is the task of detecting privacy-related entities in text,
such as person names, emails and contact data. It has been well-studied within
the medical domain. The need for de-identification technology is increasing, as
privacy-preserving data handling is in high demand in many domains. In this
paper, we focus on job postings. We present JobStack, a new corpus for
de-identification of personal data in job vacancies on Stackoverflow. We
introduce baselines, comparing Long-Short Term Memory (LSTM) and Transformer
models. To improve upon these baselines, we experiment with contextualized
embeddings and distantly related auxiliary data via multi-task learning. Our
results show that auxiliary data improves de-identification performance.
Surprisingly, vanilla BERT turned out to be more effective than a BERT model
trained on other portions of Stackoverflow.