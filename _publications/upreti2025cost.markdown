---
layout: publication
title: Cost-effective, Low Latency Vector Search With Azure Cosmos DB
authors: Nitish Upreti, Krishnan Sundaram, Hari Sudan Sundar, Samer Boshra, Balachandar
  Perumalswamy, Shivam Atri, Martin Chisholm, Revti Raman Singh, Greg Yang, Subramanyam
  Pattipaka, Tamara Hass, Nitesh Dudhey, James Codella, Mark Hildebrand, Magdalen
  Manohar, Jack Moffitt, Haiyang Xu, Naren Datha, Suryansh Gupta, Ravishankar Krishnaswamy,
  Prashant Gupta, Abhishek Sahu, Ritika Mor, Santosh Kulkarni, Hemeswari Varada, Sudhanshu
  Barthwal, Amar Sagare, Dinesh Billa, Zishan Fu, Neil Deshpande, Shaun Cooper, Kevin
  Pilch, Simon Moreno, Aayush Kataria, Vipul Vishal, Harsha Vardhan Simhadri
conference: Proceedings of the VLDB Endowment
year: 2025
bibkey: upreti2025cost
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2505.05885'}]
tags: ["Efficiency", "Tools & Libraries", "Vector Indexing"]
short_authors: Upreti et al.
---
Vector indexing enables semantic search over diverse corpora and has become an important interface to databases for both users and AI agents. Efficient vector search requires deep optimizations in database systems. This has motivated a new class of specialized vector databases that optimize for vector search quality and cost. Instead, we argue that a scalable, high-performance, and cost-efficient vector search system can be built inside a cloud-native operational database like Azure Cosmos DB while leveraging the benefits of a distributed database such as high availability, durability, and scale. We do this by deeply integrating DiskANN, a state-of-the-art vector indexing library, inside Azure Cosmos DB NoSQL. This system uses a single vector index per partition stored in existing index trees, and kept in sync with underlying data. It supports < 20ms query latency over an index spanning 10 million of vectors, has stable recall over updates, and offers nearly 15x and 41x lower query cost compared to Zilliz and Pinecone serverless enterprise products. It also scales out to billions of vectors via automatic partitioning. This convergent design presents a point in favor of integrating vector indices into operational databases in the context of recent debates on specialized vector databases, and offers a template for vector indexing in other databases.