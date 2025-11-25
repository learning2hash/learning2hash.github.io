---
layout: publication
title: Generator-retriever-generator Approach For Open-domain Question Answering
authors: Abdelrahman Abdallah, Adam Jatowt
conference: Arxiv
year: 2023
bibkey: abdallah2023generator
citations: 5
additional_links: [{name: Code, url: 'https://github.com/abdoelsayed2016/GRG'}, {
    name: Paper, url: 'https://arxiv.org/abs/2307.11278'}]
tags: ["Datasets", "Evaluation", "Text Retrieval"]
short_authors: Abdelrahman Abdallah, Adam Jatowt
---
Open-domain question answering (QA) tasks usually require the retrieval of
relevant information from a large corpus to generate accurate answers. We
propose a novel approach called Generator-Retriever-Generator (GRG) that
combines document retrieval techniques with a large language model (LLM), by
first prompting the model to generate contextual documents based on a given
question. In parallel, a dual-encoder network retrieves documents that are
relevant to the question from an external corpus. The generated and retrieved
documents are then passed to the second LLM, which generates the final answer.
By combining document retrieval and LLM generation, our approach addresses the
challenges of open-domain QA, such as generating informative and contextually
relevant answers. GRG outperforms the state-of-the-art generate-then-read and
retrieve-then-read pipelines (GENREAD and RFiD) improving their performance by
at least by +5.2, +4.2, and +1.6 on TriviaQA, NQ, and WebQ datasets,
respectively. We provide code, datasets, and checkpoints at
https://github.com/abdoelsayed2016/GRG.