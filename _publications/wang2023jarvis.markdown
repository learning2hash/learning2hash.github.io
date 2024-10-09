---
layout: publication
title: JARVIS-1 Open-world Multi-task Agents With Memory-augmented Multimodal Language Models
authors: Zihao Wang, Shaofei Cai, Anji Liu, Yonggang Jin, Jinbing Hou, Bowei Zhang, Haowei Lin, Zhaofeng He, Zilong Zheng, Yaodong Yang, Xiaojian Ma, Yitao Liang
conference: "Arxiv"
year: 2023
bibkey: wang2023jarvis
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2311.05997v3"}
tags: ['ARXIV', 'Cross Modal']
---
Achieving human-like planning and control with multimodal observations in an open world is a key milestone for more functional generalist agents. Existing approaches can handle certain long-horizon tasks in an open world. However they still struggle when the number of open-world tasks could potentially be infinite and lack the capability to progressively enhance task completion as game time progresses. We introduce JARVIS-1 an open-world agent that can perceive multimodal input (visual observations and human instructions) generate sophisticated plans and perform embodied control all within the popular yet challenging open-world Minecraft universe. Specifically we develop JARVIS-1 on top of pre-trained multimodal language models which map visual observations and textual instructions to plans. The plans will be ultimately dispatched to the goal-conditioned controllers. We outfit JARVIS-1 with a multimodal memory which facilitates planning using both pre-trained knowledge and its actual game survival experiences. JARVIS-1 is the existing most general agent in Minecraft capable of completing over 200 different tasks using control and observation space similar to humans. These tasks range from short-horizon tasks e.g. chopping trees to long-horizon tasks e.g. obtaining a diamond pickaxe. JARVIS-1 performs exceptionally well in short-horizon tasks achieving nearly perfect performance. In the classic long-term task of () JARVIS-1 surpasses the reliability of current state-of-the-art agents by 5 times and can successfully complete longer-horizon and more challenging tasks. The project page is available at https://craftjarvis.org/JARVIS-1
