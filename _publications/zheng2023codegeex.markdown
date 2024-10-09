---
layout: publication
title: Codegeex A Pre-trained Model For Code Generation With Multilingual Benchmarking On Humaneval-x
authors: Qinkai Zheng, Xiao Xia, Xu Zou, Yuxiao Dong, Shan Wang, Yufei Xue, Zihan Wang, Lei Shen, Andi Wang, Yang Li, Teng Su, Zhilin Yang, Jie Tang
conference: "Arxiv"
year: 2023
bibkey: zheng2023codegeex
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2303.17568v2"}
  - {name: "Code", url: "https://github.com/THUDM/CodeGeeX"}
tags: ['ARXIV', 'Has Code']
---
Large pre-trained code generation models such as OpenAI Codex can generate syntax- and function-correct code making the coding of programmers more productive and our pursuit of artificial general intelligence closer. In this paper we introduce CodeGeeX a multilingual model with 13 billion parameters for code generation. CodeGeeX is pre-trained on 850 billion tokens of 23 programming languages as of June 2022. Our extensive experiments suggest that CodeGeeX outperforms multilingual code models of similar scale for both the tasks of code generation and translation on HumanEval-X. Building upon HumanEval (Python only) we develop the HumanEval-X benchmark for evaluating multilingual models by hand-writing the solutions in C++ Java JavaScript and Go. In addition we build CodeGeeX-based extensions on Visual Studio Code JetBrains and Cloud Studio generating 4.7 billion tokens for tens of thousands of active users per week. Our user study demonstrates that CodeGeeX can help to increase coding efficiency for 83.437; of its users. Finally CodeGeeX is publicly accessible and in Sep. 2022 we open-sourced its code model weights (the version of 850B tokens) API extensions and HumanEval-X at https://github.com/THUDM/CodeGeeX.
