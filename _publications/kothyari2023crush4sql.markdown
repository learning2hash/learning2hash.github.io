---
layout: publication
title: 'CRUSH4SQL: Collective Retrieval Using Schema Hallucination For Text2sql'
authors: Mayank Kothyari, Dhruva Dhingra, Sunita Sarawagi, Soumen Chakrabarti
conference: Proceedings of the 2023 Conference on Empirical Methods in Natural Language
  Processing
year: 2023
bibkey: kothyari2023crush4sql
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.01173'}]
tags: ["Datasets", "EMNLP", "Evaluation"]
short_authors: Kothyari et al.
---
Existing Text-to-SQL generators require the entire schema to be encoded with
the user text. This is expensive or impractical for large databases with tens
of thousands of columns. Standard dense retrieval techniques are inadequate for
schema subsetting of a large structured database, where the correct semantics
of retrieval demands that we rank sets of schema elements rather than
individual elements. In response, we propose a two-stage process for effective
coverage during retrieval. First, we instruct an LLM to hallucinate a minimal
DB schema deemed adequate to answer the query. We use the hallucinated schema
to retrieve a subset of the actual schema, by composing the results from
multiple dense retrievals. Remarkably, hallucination \(\unicode\{x2013\}\)
generally considered a nuisance \(\unicode\{x2013\}\) turns out to be actually
useful as a bridging mechanism. Since no existing benchmarks exist for schema
subsetting on large databases, we introduce three benchmarks. Two
semi-synthetic datasets are derived from the union of schemas in two well-known
datasets, SPIDER and BIRD, resulting in 4502 and 798 schema elements
respectively. A real-life benchmark called SocialDB is sourced from an actual
large data warehouse comprising 17844 schema elements. We show that our method1
leads to significantly higher recall than SOTA retrieval-based augmentation
methods.