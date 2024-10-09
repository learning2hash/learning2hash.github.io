---
layout: publication
title: Large Language Models Are Few(1)-shot Table Reasoners
authors: Wenhu Chen
conference: "Arxiv"
year: 2022
bibkey: chen2022large
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.06710v2"}
  - {name: "Code", url: "https://github.com/wenhuchen/TableCoT"}
tags: ['ARXIV', 'Has Code']
---
Recent literature has shown that large language models (LLMs) are generally excellent few-shot reasoners to solve text reasoning tasks. However the capability of LLMs on table reasoning tasks is yet to be explored. In this paper we aim at understanding how well LLMs can perform table-related tasks with few-shot in-context learning. Specifically we evaluated LLMs on popular table QA and fact verification datasets like WikiTableQuestion FetaQA TabFact and FEVEROUS and found that LLMs are competent at complex reasoning over table structures though these models are not pre-trained on any table corpus. When combined with chain of thoughts prompting LLMs can achieve very strong performance with only a 1-shot demonstration even on par with some SoTA models. We show that LLMs are even more competent at generating comprehensive long-form answers on FetaQA than tuned T5-large. We further manually studied the reasoning chains elicited from LLMs and found that these reasoning chains are highly consistent with the underlying semantic form. We believe that LLMs can serve as a simple yet generic baseline for future research. The code and data are released in https://github.com/wenhuchen/TableCoT.
