---
layout: publication
title: Generative Retrieval With Few-shot Indexing
authors: Arian Askari, Chuan Meng, Mohammad Aliannejadi, Zhaochun Ren, Evangelos Kanoulas,
  Suzan Verberne
conference: Arxiv
year: 2024
bibkey: askari2024generative
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.02152'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Askari et al.
---
Existing generative retrieval (GR) approaches rely on training-based
indexing, i.e., fine-tuning a model to memorise the associations between a
query and the document identifier (docid) of a relevant document.
Training-based indexing has three limitations: high training overhead,
under-utilization of the pre-trained knowledge of large language models (LLMs),
and challenges in adapting to a dynamic document corpus. To address the above
issues, we propose a novel few-shot indexing-based GR framework (Few-Shot GR).
It has a novel few-shot indexing process, where we prompt an LLM to generate
docids for all documents in a corpus, ultimately creating a docid bank for the
entire corpus. During retrieval, we feed a query to the same LLM and constrain
it to generate a docid within the docid bank created during indexing, and then
map the generated docid back to its corresponding document. Few-Shot GR relies
solely on prompting an LLM without requiring any training, making it more
efficient. Moreover, we devise few-shot indexing with one-to-many mapping to
further enhance Few-Shot GR. Experiments show that Few-Shot GR achieves
superior performance to state-of-the-art GR methods that require heavy
training.