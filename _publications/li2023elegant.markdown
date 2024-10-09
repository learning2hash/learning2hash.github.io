---
layout: publication
title: E4srec An Elegant Effective Efficient Extensible Solution Of Large Language Models For Sequential Recommendation
authors: Xinhang Li, Chong Chen, Xiangyu Zhao, Yong Zhang, Chunxiao Xing
conference: "Arxiv"
year: 2023
bibkey: li2023elegant
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2312.02443v1"}
  - {name: "Code", url: "https://github.com/HestiaSky/E4SRec/"}
tags: ['ARXIV', 'Has Code']
---
The recent advancements in Large Language Models (LLMs) have sparked interest in harnessing their potential within recommender systems. Since LLMs are designed for natural language tasks existing recommendation approaches have predominantly transformed recommendation tasks into open-domain natural language generation tasks. However this approach necessitates items to possess rich semantic information often generates out-of-range results and suffers from notably low efficiency and limited extensibility. Furthermore practical ID-based recommendation strategies reliant on a huge number of unique identities (IDs) to represent users and items have gained prominence in real-world recommender systems due to their effectiveness and efficiency. Nevertheless the incapacity of LLMs to model IDs presents a formidable challenge when seeking to leverage LLMs for personalized recommendations. In this paper we introduce an Elegant Effective Efficient Extensible solution for large language models for Sequential Recommendation (E4SRec) which seamlessly integrates LLMs with traditional recommender systems that exclusively utilize IDs to represent items. Specifically E4SRec takes ID sequences as inputs ensuring that the generated outputs fall within the candidate lists. Furthermore E4SRec possesses the capability to generate the entire ranking list in a single forward process and demands only a minimal set of pluggable parameters which are trained for each dataset while keeping the entire LLM frozen. We substantiate the effectiveness efficiency and extensibility of our proposed E4SRec through comprehensive experiments conducted on four widely-used real-world datasets. The implementation code is accessible at https://github.com/HestiaSky/E4SRec/.
