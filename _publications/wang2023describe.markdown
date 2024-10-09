---
layout: publication
title: Describe Explain Plan And Select Interactive Planning With Large Language Models Enables Open-world Multi-task Agents
authors: Zihao Wang, Shaofei Cai, Guanzhou Chen, Anji Liu, Xiaojian Ma, Yitao Liang
conference: "Arxiv"
year: 2023
bibkey: wang2023describe
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2302.01560v3"}
  - {name: "Code", url: "https://github.com/CraftJarvis/MC-Planner"}
tags: ['ARXIV', 'Has Code']
---
We investigate the challenge of task planning for multi-task embodied agents in open-world environments. Two main difficulties are identified 1) executing plans in an open-world environment (e.g. Minecraft) necessitates accurate and multi-step reasoning due to the long-term nature of tasks and 2) as vanilla planners do not consider how easy the current agent can achieve a given sub-task when ordering parallel sub-goals within a complicated plan the resulting plan could be inefficient or even infeasible. To this end we propose ()escribe ()xplain ()lan and ()elect (()) an interactive planning approach based on Large Language Models (LLMs). DEPS facilitates better error correction on initial LLM-generated () by integrating () of the plan execution process and providing self-() of feedback when encountering failures during the extended planning phases. Furthermore it includes a goal () which is a trainable module that ranks parallel candidate sub-goals based on the estimated steps of completion consequently refining the initial plan. Our experiments mark the milestone of the first zero-shot multi-task agent that can robustly accomplish 70+ Minecraft tasks and nearly double the overall performances. Further testing reveals our methods general effectiveness in popularly adopted non-open-ended domains as well (i.e. ALFWorld and tabletop manipulation). The ablation and exploratory studies detail how our design beats the counterparts and provide a promising update on the () grand challenge with our approach. The code is released at https://github.com/CraftJarvis/MC-Planner.
