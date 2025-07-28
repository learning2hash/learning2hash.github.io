---
layout: publication
title: A Slicing-based Approach For Detecting And Patching Vulnerable Code Clones
authors: Hakam Alomari, Christopher Vendome, Hilal Gyawali
conference: 2025 IEEE/ACM 33rd International Conference on Program Comprehension (ICPC)
year: 2025
bibkey: alomari2025slicing
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.02349'}]
tags: []
short_authors: Hakam Alomari, Christopher Vendome, Hilal Gyawali
---
Code cloning is a common practice in software development, but it poses
significant security risks by propagating vulnerabilities across cloned
segments. To address this challenge, we introduce srcVul, a scalable, precise
detection approach that combines program slicing with Locality-Sensitive
Hashing to identify vulnerable code clones and recommend patches. srcVul builds
a database of vulnerability-related slices by analyzing known vulnerable
programs and their corresponding patches, indexing each slice's unique
structural characteristics as a vulnerability slicing vector. During clone
detection, srcVul efficiently matches slicing vectors from target programs with
those in the database, recommending patches upon identifying similarities. Our
evaluation of srcVul against three state-of-the-art vulnerable clone detectors
demonstrates its accuracy, efficiency, and scalability, achieving 91% precision
and 75% recall on established vulnerability databases and open-source
repositories. These results highlight srcVul's effectiveness in detecting
complex vulnerability patterns across diverse codebases.