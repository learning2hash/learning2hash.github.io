---
layout: publication
title: 'Curator: Efficient Indexing For Multi-tenant Vector Databases'
authors: Yicheng Jin, Yongji Wu, Wenjun Hu, Bruce M. Maggs, Xiao Zhang, Danyang Zhuo
conference: Arxiv
year: 2024
bibkey: jin2024curator
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.07119'}]
tags: [Evaluation, Efficiency, Memory Efficiency, Vector Indexing]
short_authors: Jin et al.
---
Vector databases have emerged as key enablers for bridging intelligent
applications with unstructured data, providing generic search and management
support for embedding vectors extracted from the raw unstructured data. As
multiple data users can share the same database infrastructure, multi-tenancy
support for vector databases is increasingly desirable. This hinges on an
efficient filtered search operation, i.e., only querying the vectors accessible
to a particular tenant. Multi-tenancy in vector databases is currently achieved
by building either a single, shared index among all tenants, or a per-tenant
index. The former optimizes for memory efficiency at the expense of search
performance, while the latter does the opposite. Instead, this paper presents
Curator, an in-memory vector index design tailored for multi-tenant queries
that simultaneously achieves the two conflicting goals, low memory overhead and
high performance for queries, vector insertion, and deletion. Curator indexes
each tenant's vectors with a tenant-specific clustering tree and encodes these
trees compactly as sub-trees of a shared clustering tree. Each tenant's
clustering tree adapts dynamically to its unique vector distribution, while
maintaining a low per-tenant memory footprint. Our evaluation, based on two
widely used data sets, confirms that Curator delivers search performance on par
with per-tenant indexing, while maintaining memory consumption at the same
level as metadata filtering on a single, shared index.