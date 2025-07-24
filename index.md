---
layout: default
title: "Awesome Papers on Learning to Hash: A Curated, Evolving Resource"
description: "Explore recent research in learning to hash, including key publications, topic tags, taxonomy-driven organization, real-world applications, and community contributions — a living literature review for approximate nearest neighbour methods."
comments: true
permalink: /
---

# Awesome Papers on Learning to Hash

<p style="font-size: 1.2em;">
A curated and continuously updated collection of academic papers on hashing-based approximate nearest neighbour (ANN) search, spanning applications in computer vision, natural language processing, bioinformatics, and related domains.
</p>

---

### 🏷 Browse Papers by Tag
<p>
Explore the literature by topic. Use the tags below to navigate research on supervised hashing, deep binary embeddings, quantization, indexing strategies, and other relevant themes:
</p>

{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort %}
<p style="margin: 1em 0;">
{% for tag in rawtags %}<tag style="display: inline-block; margin: 0.2em 0.5em;"><a href="/tags.html#{{ tag }}">#{{ tag }}</a></tag>{% endfor %}
</p>

---

### 📚 What This Site Offers
<ul style="font-size: 1em;">
  <li>🔍 Access over 2,000 curated publications, organized by topic and methodological taxonomy</li>
  <li>📈 Identify emerging trends in supervised, unsupervised, deep, and quantized hashing methods</li>
  <li>🧠 Examine real-world applications including audio retrieval, source code search, and geospatial monitoring</li>
  <li>📎 Contribute to the resource by submitting new papers or updates</li>
</ul>

---

### 🤔 What is Learning to Hash?
<p>
<a href="https://en.wikipedia.org/wiki/Nearest_neighbor_search">Nearest neighbour search</a> involves identifying similar items within large datasets. Learning to hash improves this process by mapping data into compact binary hash codes that preserve similarity relationships — facilitating efficient, memory-conscious retrieval.
</p>

<p>
These methods underpin a wide range of systems, from multimedia search and recommendation engines to scientific data analysis pipelines.
</p>

#### 🔬 Selected Applications
<ul>
  <li><strong><a href="https://arxiv.org/abs/2111.04473">Source Code Search</a></strong> – MinHash applied to large-scale code recommendation</li>
  <li><strong><a href="https://openreview.net/pdf?id=rkgNKkHtvB">Efficient Transformers</a></strong> – Locality-Sensitive Hashing (LSH) for computational efficiency</li>
  <li><strong><a href="https://eng.uber.com/lsh/">Fraud Detection</a></strong> – Spatial anomaly detection using LSH at Uber</li>
  <li><strong><a href="https://www.aclweb.org/anthology/P14-5007">Event Tracking</a></strong> – Social media monitoring through similarity-preserving hashing</li>
  <li><strong><a href="https://ai.google/research/pubs/pub34634">Image Retrieval</a></strong> – Scalable visual indexing with LSH at Google</li>
</ul>

---

### 🧩 How Hashing Works
<p>
Learning to hash involves training a model to encode data points into binary hash codes. These codes are then used to assign items to buckets in one or more hash tables. During retrieval, only the relevant buckets are searched — reducing computational overhead significantly compared to exhaustive search.
</p>

<p align="center">
  <img src="/public/media/hashing.png?raw=true" alt="Locality Sensitive Hashing (LSH)" width="600" style="max-width: 100%; border-radius: 10px;"/>
  <br><em>Example of LSH in action, from the <a href="https://learning2hash.github.io/cite.html">PhD thesis of Sean Moran</a>.</em>
</p>

---

### 🤝 Contributing to the Collection
<p>
This site is maintained as a community resource. If you have authored or come across a relevant paper, we encourage you to contribute via our submission form or GitHub pull request. See the <a href="contributing.html">Contributing</a> page for details.
</p>

<p>
To explore further, view the full set of indexed papers on the <a href="/papers.html">All Papers</a> page, or visit the <a href="/resources.html">Resources</a> section for foundational materials and curated tools.
</p>

---

<p style="font-size: 0.9em;">Copyright © <a href="https://sjmoran.github.io/">Sean Moran</a> 2025. All opinions are my own.</p>
