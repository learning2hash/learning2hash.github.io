---
layout: publication
title: Galactica A Large Language Model For Science
authors: Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic
conference: "Arxiv"
year: 2022
bibkey: taylor2022galactica
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2211.09085v1"}
tags: ['ARXIV']
---
Information overload is a major obstacle to scientific progress. The explosive growth in scientific literature and data has made it ever harder to discover useful insights in a large mass of information. Today scientific knowledge is accessed through search engines but they are unable to organize scientific knowledge alone. In this paper we introduce Galactica a large language model that can store combine and reason about scientific knowledge. We train on a large scientific corpus of papers reference material knowledge bases and many other sources. We outperform existing models on a range of scientific tasks. On technical knowledge probes such as LaTeX equations Galactica outperforms the latest GPT-3 by 68.237; versus 49.037;. Galactica also performs well on reasoning outperforming Chinchilla on mathematical MMLU by 41.337; to 35.737; and PaLM 540B on MATH with a score of 20.437; versus 8.837;. It also sets a new state-of-the-art on downstream tasks such as PubMedQA and MedMCQA dev of 77.637; and 52.937;. And despite not being trained on a general corpus Galactica outperforms BLOOM and OPT-175B on BIG-bench. We believe these results demonstrate the potential for language models as a new interface for science. We open source the model for the benefit of the scientific community.
