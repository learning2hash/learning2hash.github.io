---
layout: publication
title: 'Honeybee: A Scalable Modular Framework For Creating Multimodal Oncology Datasets
  With Foundational Embedding Models'
authors: Aakash Tripathi, Asim Waqas, Matthew B. Schabath, Yasin Yilmaz, Ghulam Rasool
conference: Arxiv
year: 2024
bibkey: tripathi2024honeybee
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.07460'}]
tags: [Tools & Libraries, Datasets, Scalability]
short_authors: Tripathi et al.
---
Developing accurate machine learning models for oncology requires
large-scale, high-quality multimodal datasets. However, creating such datasets
remains challenging due to the complexity and heterogeneity of medical data. To
address this challenge, we introduce HoneyBee, a scalable modular framework for
building multimodal oncology datasets that leverages foundation models to
generate representative embeddings. HoneyBee integrates various data
modalities, including clinical diagnostic and pathology imaging data, medical
notes, reports, records, and molecular data. It employs data preprocessing
techniques and foundation models to generate embeddings that capture the
essential features and relationships within the raw medical data. The generated
embeddings are stored in a structured format using Hugging Face datasets and
PyTorch dataloaders for accessibility. Vector databases enable efficient
querying and retrieval for machine learning applications. We demonstrate the
effectiveness of HoneyBee through experiments assessing the quality and
representativeness of these embeddings. The framework is designed to be
extensible to other medical domains and aims to accelerate oncology research by
providing high-quality, machine learning-ready datasets. HoneyBee is an ongoing
open-source effort, and the code, datasets, and models are available at the
project repository.