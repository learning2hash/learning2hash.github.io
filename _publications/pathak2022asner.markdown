---
layout: publication
title: Asner -- Annotated Dataset And Baseline For Assamese Named Entity Recognition
authors: Dhrubajyoti Pathak, Sukumar Nandi, Priyankoo Sarmah
conference: Proceedings of the Language Resources and Evaluation Conference June 2022
  Marseille France European Language Resources Association 6571-6577
year: 2022
bibkey: pathak2022asner
citations: 4
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2207.03422'}]
tags: ["Datasets", "Evaluation", "LREC"]
short_authors: Dhrubajyoti Pathak, Sukumar Nandi, Priyankoo Sarmah
---
We present the AsNER, a named entity annotation dataset for low resource
Assamese language with a baseline Assamese NER model. The dataset contains
about 99k tokens comprised of text from the speech of the Prime Minister of
India and Assamese play. It also contains person names, location names and
addresses. The proposed NER dataset is likely to be a significant resource for
deep neural based Assamese language processing. We benchmark the dataset by
training NER models and evaluating using state-of-the-art architectures for
supervised named entity recognition (NER) such as Fasttext, BERT, XLM-R, FLAIR,
MuRIL etc. We implement several baseline approaches with state-of-the-art
sequence tagging Bi-LSTM-CRF architecture. The highest F1-score among all
baselines achieves an accuracy of 80.69% when using MuRIL as a word embedding
method. The annotated dataset and the top performing model are made publicly
available.