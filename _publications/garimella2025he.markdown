---
layout: publication
title: 'HE-LRM: Encrypted Deep Learning Recommendation Models Using Fully Homomorphic
  Encryption'
authors: Garimella et al.
conference: Soft Computing
year: 2025
bibkey: garimella2025he
citations: 11
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2506.18150'}]
tags: ["Recommender-Systems"]
---
Fully Homomorphic Encryption (FHE) is an encryption scheme that not only encrypts data but also allows for computations to be applied directly on the encrypted data. While computationally expensive, FHE can enable privacy-preserving neural inference in the client-server setting: a client encrypts their input with FHE and sends it to an untrusted server. The server then runs neural inference on the encrypted data and returns the encrypted results. The client decrypts the output locally, keeping both the input and result private from the server. Private inference has focused on networks with dense inputs such as image classification, and less attention has been given to networks with sparse features. Unlike dense inputs, sparse features require efficient encrypted lookup operations into large embedding tables, which present computational and memory constraints for FHE.
  In this paper, we explore the challenges and opportunities when applying FHE to Deep Learning Recommendation Models (DLRM) from both a compiler and systems perspective. DLRMs utilize conventional MLPs for dense features and embedding tables to map sparse, categorical features to dense vector representations. We develop novel methods for performing compressed embedding lookups in order to reduce FHE computational costs while keeping the underlying model performant. Our embedding lookup improves upon a state-of-the-art approach by \\(77 \times\\). Furthermore, we present an efficient multi-embedding packing strategy that enables us to perform a 44 million parameter embedding lookup under FHE. Finally, we integrate our solutions into the open-source Orion framework and present HE-LRM, an end-to-end encrypted DLRM. We evaluate HE-LRM on UCI (health prediction) and Criteo (click prediction), demonstrating that with the right compression and packing strategies, encrypted inference for recommendation systems is practical.