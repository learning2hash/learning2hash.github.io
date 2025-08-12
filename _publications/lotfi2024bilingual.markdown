---
layout: publication
title: 'Bilingual BSARD: Extending Statutory Article Retrieval To Dutch'
authors: Ehsan Lotfi, Nikolay Banar, Nerses Yuzbashyan, Walter Daelemans
conference: Arxiv
year: 2024
bibkey: lotfi2024bilingual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.07462'}]
tags: []
short_authors: Lotfi et al.
---
Statutory article retrieval plays a crucial role in making legal information
more accessible to both laypeople and legal professionals. Multilingual
countries like Belgium present unique challenges for retrieval models due to
the need for handling legal issues in multiple languages. Building on the
Belgian Statutory Article Retrieval Dataset (BSARD) in French, we introduce the
bilingual version of this dataset, bBSARD. The dataset contains parallel
Belgian statutory articles in both French and Dutch, along with legal questions
from BSARD and their Dutch translation. Using bBSARD, we conduct extensive
benchmarking of retrieval models available for Dutch and French. Our
benchmarking setup includes lexical models, zero-shot dense models, and
fine-tuned small foundation models. Our experiments show that BM25 remains a
competitive baseline compared to many zero-shot dense models in both languages.
We also observe that while proprietary models outperform open alternatives in
the zero-shot setting, they can be matched or surpassed by fine-tuning small
language-specific models. Our dataset and evaluation code are publicly
available.