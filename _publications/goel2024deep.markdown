---
layout: publication
title: Deep Learning Based Named Entity Recognition Models For Recipes
authors: Mansi Goel, Ayush Agarwal, Shubham Agrawal, Janak Kapuriya, Akhil Vamshi
  Konam, Rishabh Gupta, Shrey Rastogi, Niharika, Ganesh Bagler
conference: Arxiv
year: 2024
bibkey: goel2024deep
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.17447'}]
tags: ["Datasets", "Evaluation"]
short_authors: Goel et al.
---
Food touches our lives through various endeavors, including flavor,
nourishment, health, and sustainability. Recipes are cultural capsules
transmitted across generations via unstructured text. Automated protocols for
recognizing named entities, the building blocks of recipe text, are of immense
value for various applications ranging from information extraction to novel
recipe generation. Named entity recognition is a technique for extracting
information from unstructured or semi-structured data with known labels.
Starting with manually-annotated data of 6,611 ingredient phrases, we created
an augmented dataset of 26,445 phrases cumulatively. Simultaneously, we
systematically cleaned and analyzed ingredient phrases from RecipeDB, the
gold-standard recipe data repository, and annotated them using the Stanford
NER. Based on the analysis, we sampled a subset of 88,526 phrases using a
clustering-based approach while preserving the diversity to create the
machine-annotated dataset. A thorough investigation of NER approaches on these
three datasets involving statistical, fine-tuning of deep learning-based
language models and few-shot prompting on large language models (LLMs) provides
deep insights. We conclude that few-shot prompting on LLMs has abysmal
performance, whereas the fine-tuned spaCy-transformer emerges as the best model
with macro-F1 scores of 95.9%, 96.04%, and 95.71% for the manually-annotated,
augmented, and machine-annotated datasets, respectively.