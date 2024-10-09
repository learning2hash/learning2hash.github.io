---
layout: publication
title: Exploring Human-like Translation Strategy With Large Language Models
authors: Zhiwei He, Tian Liang, Wenxiang Jiao, Zhuosheng Zhang, Yujiu Yang, Rui Wang, Zhaopeng Tu, Shuming Shi, Xing Wang
conference: "Arxiv"
year: 2023
bibkey: he2023exploring
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2305.04118v3"}
  - {name: "Code", url: "https://github.com/zwhe99/MAPS-mt"}
tags: ['ARXIV', 'Has Code']
---
Large language models (LLMs) have demonstrated impressive capabilities in general scenarios exhibiting a level of aptitude that approaches in some aspects even surpasses human-level intelligence. Among their numerous skills the translation abilities of LLMs have received considerable attention. Compared to typical machine translation that focuses solely on source-to-target mapping LLM-based translation can potentially mimic the human translation process which might take preparatory steps to ensure high-quality translation. This work explores this possibility by proposing the MAPS framework which stands for Multi-Aspect Prompting and Selection. Specifically we enable LLMs first to analyze the given source sentence and induce three aspects of translation-related knowledge keywords topics and relevant demonstrations to guide the final translation process. Moreover we employ a selection mechanism based on quality estimation to filter out noisy and unhelpful knowledge. Both automatic (3 LLMs x 11 directions x 2 automatic metrics) and human evaluation (preference study and MQM) demonstrate the effectiveness of MAPS. Further analysis shows that by mimicking the human translation process MAPS reduces various translation errors such as hallucination ambiguity mistranslation awkward style untranslated text and omission. Source code is available at https://github.com/zwhe99/MAPS-mt.
