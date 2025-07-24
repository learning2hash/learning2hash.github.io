---
layout: default
title: "Awesome Papers on Learning to Hash: A Curated, Evolving Resource"
description: "Explore the latest research in learning to hash, including key papers, topic tags, taxonomy-based organization, applications, and community contributions — a living literature review for ANN and hashing methods."
comments: true
permalink: /
---

# Awesome Papers on Learning to Hash

<p style="font-size: 1.2em;">A curated, living collection of research on hashing-based approximate nearest neighbour search — across vision, NLP, bioinformatics, and beyond.</p>

---

### 🏷 Browse Papers by Tag
<p>Quickly explore the latest research by topic. Click a tag below to dive into supervised hashing, deep binary embeddings, quantization, indexing techniques, and more:</p>

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
  <li>🔍 Search and browse 2000+ curated papers organized by topic and taxonomy</li>
  <li>📈 Discover trends in supervised, unsupervised, deep, and quantized hashing</li>
  <li>🧠 Explore research applications from audio and image retrieval to code search and earthquake detection</li>
  <li>📎 Contribute your own papers and help keep the field current</li>
</ul>

---

### 🤔 What is Learning to Hash?
<p><a href="https://en.wikipedia.org/wiki/Nearest_neighbor_search">Nearest Neighbour Search</a> is about finding similar items in large datasets. Learning to hash improves this process by encoding data into binary hash codes that preserve similarity — enabling fast, memory-efficient retrieval.</p>

<p>These techniques power everything from image search and source code recommendation to seismic monitoring and malware detection.</p>

#### 🔬 Applications in Action
<ul>
  <li><strong><a href="https://arxiv.org/abs/2111.04473">Source Code Search</a></strong> – MinHash for code recommendations</li>
  <li><strong><a href="https://openreview.net/pdf?id=rkgNKkHtvB">Efficient Transformers</a></strong> – Using LSH to reduce training cost</li>
  <li><strong><a href="https://eng.uber.com/lsh/">Fraud Detection at Uber</a></strong> – LSH for spatial anomaly detection</li>
  <li><strong><a href="https://www.aclweb.org/anthology/P14-5007">Event Tracking</a></strong> – Social media monitoring via hashing</li>
  <li><strong><a href="https://ai.google/research/pubs/pub34634">Image Retrieval</a></strong> – Google’s large-scale visual indexing with LSH</li>
</ul>

---

### 🧩 How Hashing Works
<p>Learning to hash maps input data into binary hash codes. These are then used to index points into hash tables. At query time, only nearby hash buckets are searched — dramatically reducing computation compared to brute-force approaches.</p>

<p align="center">
  <img src="/public/media/hashing.png?raw=true" alt="Locality Sensitive Hashing (LSH)" width="600" style="max-width: 100%; border-radius: 10px;"/>
  <br><em>Visual example of LSH. From the <a href="https://learning2hash.github.io/cite.html">PhD thesis of Sean Moran</a>.</em>
</p>

---

### 🤝 Help Curate the Field
<p>This project is a community-driven literature review. If you’ve written or discovered a new paper, you can submit it with a simple form or pull request. See the <a href="contributing.html">Contributing page</a> for instructions.</p>

<p>Want to go deeper? Check out the full list of contributions on the <a href="/papers.html">All Papers</a> page or explore our <a href="/resources.html">Resources</a> section for primers and background.</p>

---

<p style="font-size: 0.9em;">Copyright © <a href="https://sjmoran.github.io/">Sean Moran</a> 2025. All opinions are my own.</p>
