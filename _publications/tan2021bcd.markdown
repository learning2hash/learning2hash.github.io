---
    layout: publication
    title: "BCD: A Cross-Architecture Binary Comparison Database Experiment Using Locality Sensitive Hashing Algorithms"
    authors: Tan Haoxi
    conference: Arxiv
    year: 2021
    bibkey: tan2021bcd
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by-sa/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2112.05492"}
   - {name: "Code", url: "https://github.com/h4sh5/bcddb"}
    tags: ['LSH', 'Arxiv']
    ---
    Given a binary executable without source code, it is difficult to determine what each function in the binary does by reverse engineering it, and even harder without prior experience and context. In this paper, we performed a comparison of different hashing functions' effectiveness at detecting similar lifted snippets of LLVM IR code, and present the design and implementation of a framework for cross-architecture binary code similarity search database using MinHash as the chosen hashing algorithm, over SimHash, SSDEEP and TLSH. The motivation is to help reverse engineers to quickly gain context of functions in an unknown binary by comparing it against a database of known functions. The code for this project is open source and can be found at https://github.com/h4sh5/bcddb