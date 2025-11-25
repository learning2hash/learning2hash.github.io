---
layout: publication
title: 'Legalsearchlm: Rethinking Legal Case Retrieval As Legal Elements Generation'
authors: Chaeeun Kim, Jinu Lee, Wonseok Hwang
conference: Arxiv
year: 2025
bibkey: kim2025legalsearchlm
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.23832'}]
tags: ["Evaluation", "Large Scale Search", "Scalability", "Text Retrieval"]
short_authors: Chaeeun Kim, Jinu Lee, Wonseok Hwang
---
Legal Case Retrieval (LCR), which retrieves relevant cases from a query case, is a fundamental task for legal professionals in research and decision-making. However, existing studies on LCR face two major limitations. First, they are evaluated on relatively small-scale retrieval corpora (e.g., 100-55K cases) and use a narrow range of criminal query types, which cannot sufficiently reflect the complexity of real-world legal retrieval scenarios. Second, their reliance on embedding-based or lexical matching methods often results in limited representations and legally irrelevant matches. To address these issues, we present: (1) LEGAR BENCH, the first large-scale Korean LCR benchmark, covering 411 diverse crime types in queries over 1.2M legal cases; and (2) LegalSearchLM, a retrieval model that performs legal element reasoning over the query case and directly generates content grounded in the target cases through constrained decoding. Experimental results show that LegalSearchLM outperforms baselines by 6-20% on LEGAR BENCH, achieving state-of-the-art performance. It also demonstrates strong generalization to out-of-domain cases, outperforming naive generative models trained on in-domain data by 15%.