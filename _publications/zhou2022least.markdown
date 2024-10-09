---
layout: publication
title: Least-to-most Prompting Enables Complex Reasoning In Large Language Models
authors: Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le, Ed Chi
conference: "Arxiv"
year: 2022
bibkey: zhou2022least
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2205.10625v3"}
tags: ['ARXIV']
---
Chain-of-thought prompting has demonstrated remarkable performance on various natural language reasoning tasks. However it tends to perform poorly on tasks which requires solving problems harder than the exemplars shown in the prompts. To overcome this challenge of easy-to-hard generalization we propose a novel prompting strategy least-to-most prompting. The key idea in this strategy is to break down a complex problem into a series of simpler subproblems and then solve them in sequence. Solving each subproblem is facilitated by the answers to previously solved subproblems. Our experimental results on tasks related to symbolic manipulation compositional generalization and math reasoning reveal that least-to-most prompting is capable of generalizing to more difficult problems than those seen in the prompts. A notable finding is that when the GPT-3 code-davinci-002 model is used with least-to-most prompting it can solve the compositional generalization benchmark SCAN in any split (including length split) with an accuracy of at least 9937; using just 14 exemplars compared to only 1637; accuracy with chain-of-thought prompting. This is particularly noteworthy because neural-symbolic models in the literature that specialize in solving SCAN are trained on the entire training set containing over 15000 examples. We have included prompts for all the tasks in the Appendix.
