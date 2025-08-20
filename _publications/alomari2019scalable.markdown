---
layout: publication
title: Scalable Source Code Similarity Detection In Large Code Repositories
authors: F Alomari, M Harbi
conference: ICST Transactions on Scalable Information Systems
year: 2019
bibkey: alomari2019scalable
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1907.11817'}]
tags: [Evaluation, Efficiency, Similarity Search]
short_authors: F Alomari, M Harbi
---
Source code similarity are increasingly used in application development to
identify clones, isolate bugs, and find copy-rights violations. Similar code
fragments can be very problematic due to the fact that errors in the original
code must be fixed in every copy. Other maintenance changes, such as extensions
or patches, must be applied multiple times. Furthermore, the diversity of
coding styles and flexibility of modern languages makes it difficult and cost
ineffective to manually inspect large code repositories. Therefore, detection
is only feasible by automatic techniques. We present an efficient and scalable
approach for similar code fragment identification based on source code control
flow graphs fingerprinting. The source code is processed to generate control
flow graphs that are then hashed to create a unique fingerprint of the code
capturing semantics as well as syntax similarity. The fingerprints can then be
efficiently stored and retrieved to perform similarity search between code
fragments. Experimental results from our prototype implementation supports the
validity of our approach and show its effectiveness and efficiency in
comparison with other solutions.