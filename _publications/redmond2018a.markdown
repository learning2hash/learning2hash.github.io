---
layout: publication
title: A Cross-architecture Instruction Embedding Model For Natural Language Processing-inspired
  Binary Code Analysis
authors: Kimberly Redmond, Lannan Luo, Qiang Zeng
conference: Proceedings 2019 Workshop on Binary Analysis Research
year: 2019
bibkey: redmond2018a
citations: 50
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1812.09652'}]
tags: [Compact Codes, Evaluation]
short_authors: Kimberly Redmond, Lannan Luo, Qiang Zeng
---
Given a closed-source program, such as most of proprietary software and
viruses, binary code analysis is indispensable for many tasks, such as code
plagiarism detection and malware analysis. Today, source code is very often
compiled for various architectures, making cross-architecture binary code
analysis increasingly important. A binary, after being disassembled, is
expressed in an assembly languages. Thus, recent work starts exploring Natural
Language Processing (NLP) inspired binary code analysis. In NLP, words are
usually represented in high-dimensional vectors (i.e., embeddings) to
facilitate further processing, which is one of the most common and critical
steps in many NLP tasks. We regard instructions as words in NLP-inspired binary
code analysis, and aim to represent instructions as embeddings as well.
  To facilitate cross-architecture binary code analysis, our goal is that
similar instructions, regardless of their architectures, have embeddings close
to each other. To this end, we propose a joint learning approach to generating
instruction embeddings that capture not only the semantics of instructions
within an architecture, but also their semantic relationships across
architectures. To the best of our knowledge, this is the first work on building
cross-architecture instruction embedding model. As a showcase, we apply the
model to resolving one of the most fundamental problems for binary code
similarity comparison---semantics-based basic block comparison, and the
solution outperforms the code statistics based approach. It demonstrates that
it is promising to apply the model to other cross-architecture binary code
analysis tasks.