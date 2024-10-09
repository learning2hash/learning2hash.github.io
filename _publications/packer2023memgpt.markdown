---
layout: publication
title: Memgpt Towards Llms As Operating Systems
authors: Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez
conference: "Arxiv"
year: 2023
bibkey: packer2023memgpt
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2310.08560v2"}
  - {name: "Code", url: "https://memgpt.ai"}
tags: ['ARXIV', 'Has Code']
---
Large language models (LLMs) have revolutionized AI but are constrained by limited context windows hindering their utility in tasks like extended conversations and document analysis. To enable using context beyond limited context windows we propose virtual context management a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory. Using this technique we introduce MemGPT (Memory-GPT) a system that intelligently manages different memory tiers in order to effectively provide extended context within the LLMs limited context window and utilizes interrupts to manage control flow between itself and the user. We evaluate our OS-inspired design in two domains where the limited context windows of modern LLMs severely handicaps their performance document analysis where MemGPT is able to analyze large documents that far exceed the underlying LLMs context window and multi-session chat where MemGPT can create conversational agents that remember reflect and evolve dynamically through long-term interactions with their users. We release MemGPT code and data for our experiments at https://memgpt.ai.
