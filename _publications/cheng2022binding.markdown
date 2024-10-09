---
layout: publication
title: Binding Language Models In Symbolic Languages
authors: Zhoujun Cheng, Tianbao Xie, Peng Shi, Chengzu Li, Rahul Nadkarni, Yushi Hu, Caiming Xiong, Dragomir Radev, Mari Ostendorf, Luke Zettlemoyer, Noah A. Smith, Tao Yu
conference: "Arxiv"
year: 2022
bibkey: cheng2022binding
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2210.02875v2"}
  - {name: "Code", url: "https://github.com/HKUNLP/Binder"}
tags: ['ARXIV', 'Has Code']
---
Though end-to-end neural approaches have recently been dominating NLP tasks in both performance and ease-of-use they lack interpretability and robustness. We propose Binder a training-free neural-symbolic framework that maps the task input to a program which (1) allows binding a unified API of language model (LM) functionalities to a programming language (e.g. SQL Python) to extend its grammar coverage and thus tackle more diverse questions (2) adopts an LM as both the program parser and the underlying model called by the API during execution and (3) requires only a few in-context exemplar annotations. Specifically we employ GPT-3 Codex as the LM. In the parsing stage with only a few in-context exemplars Codex is able to identify the part of the task input that cannot be answerable by the original programming language correctly generate API calls to prompt Codex to solve the unanswerable part and identify where to place the API calls while being compatible with the original grammar. In the execution stage Codex can perform versatile functionalities (e.g. commonsense QA information extraction) given proper prompts in the API calls. Binder achieves state-of-the-art results on WikiTableQuestions and TabFact datasets with explicit output programs that benefit human debugging. Note that previous best systems are all finetuned on tens of thousands of task-specific samples while Binder only uses dozens of annotations as in-context exemplars without any training. Our code is available at https://github.com/HKUNLP/Binder .
