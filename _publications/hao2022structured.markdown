---
layout: publication
title: Structured Prompting Scaling In-context Learning To 1000 Examples
authors: Yaru Hao, Yutao Sun, Li Dong, Zhixiong Han, Yuxian Gu, Furu Wei
conference: "Arxiv"
year: 2022
bibkey: hao2022structured
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2212.06713v1"}
  - {name: "Code", url: "https://aka.ms/structured-prompting"}
tags: ['ARXIV', 'Has Code']
---
Large language models have exhibited intriguing in-context learning capability achieving promising zero- and few-shot performance without updating the parameters. However conventional in-context learning is usually restricted by length constraints rendering it ineffective to absorb supervision from a large number of examples. In order to go beyond few shots we introduce structured prompting that breaks the length limit and scales in-context learning to thousands of examples. Specifically demonstration examples are separately encoded with well-designed position embeddings and then they are jointly attended by the test example using a rescaled attention mechanism. So we can scale the number of exemplars with linear complexity instead of quadratic complexity with respect to length. Experimental results on a diverse set of tasks show that our approach improves end-task performance and reduces evaluation variance over conventional in-context learning as the number of demonstration examples increases. Code has been released at https://aka.ms/structured-prompting.
