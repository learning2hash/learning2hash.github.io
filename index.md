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
<p>
  <strong>
    <a target="_blank" href="http://arxiv.org/abs/2510.04127">
      Learning-Based Hashing for ANN Search: Foundations and Early Advances
    </a>
    <span style="background-color:#dc2626; color:#fff; font-size:0.8em; padding:2px 6px; border-radius:4px; margin-left:6px;">
      NEW
    </span>
  </strong><br />
  Sean Moran.<br />
  <em>2025</em><br />
  <span style="color:#4b5563;">
    An accessible introduction to the field of learning-based hashing and a synthesis of its early core advances, bridging projection, quantisation, and supervised approaches for efficient similarity search.
  </span>
</p>

<style>
.tag-cloud {
  display:flex;
  flex-wrap:wrap;
  gap:.5rem .75rem;
  margin:.4rem 0 .8rem;
}
.tag-cloud a {
  text-decoration:none;
  border-radius:999px;
  padding:.15rem .45rem;
  background:#f6f7f9;
  border:1px solid #e6e8ec;
  display:inline-flex;
  align-items:center;
  gap:.35rem;
  font-size:.75rem;
  line-height:1.1;
  color:#6b7280;
  font-weight:500;
}
.tag-cloud a:hover { background:#f0f3f7; color:#4b5563; }
.tag-cloud a:focus { outline:none; box-shadow:0 0 0 3px rgba(26,115,232,.25); }
.tag-cloud a,
.tag-cloud a:link,
.tag-cloud a:visited,
.tag-cloud a:hover,
.tag-cloud a:active {
  color:#6b7280 !important;
  text-decoration:none !important;
}
</style>

---

### Browse Papers by Tag

<p>Explore the latest research by browsing papers categorized by tags. Select a tag below to dive deeper into specific topics within the field of learning to hash:</p>

<div class="tag-cloud">
{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags %}
  {% assign rawtags = rawtags | concat: ttags %}
{% endfor %}
{% assign rawtags = rawtags | uniq | sort %}
{% for tag in rawtags %}
  <a href="/tags.html#{{ tag | uri_escape }}">{{ tag }}</a>
{% endfor %}
</div>
---

### What This Site Offers
<ul style="font-size: 1em;">
  <li>🔍 Access over 3,000 curated publications, organized by topic and methodological taxonomy</li>
  <li>📈 Identify emerging trends in supervised, unsupervised, deep, and quantized hashing methods</li>
  <li>🧠 Examine real-world applications including audio retrieval, source code search, and geospatial monitoring</li>
  <li>📎 Contribute to the resource by submitting new papers or updates</li>
</ul>

---

### What is Learning to Hash?
<p>
<a href="https://en.wikipedia.org/wiki/Nearest_neighbor_search">Nearest neighbour search</a> involves retrieving similar items from large datasets, often in high-dimensional spaces. <strong>Learning to Hash (L2H)</strong> enhances this process by learning compact representations—typically binary codes, but sometimes real-valued or quantized forms—that preserve semantic or structural similarity. These representations enable fast and memory-efficient approximate retrieval by avoiding exhaustive comparisons.
</p>

<p>
Learning to Hash techniques underpin a broad range of applications, including large-scale multimedia retrieval, recommendation systems, source code search, scientific data mining, and real-time anomaly detection.
</p>

#### Selected Applications
<ul>
  <li><strong><a href="https://arxiv.org/abs/2111.04473">Source Code Search</a></strong> – MinHash applied to large-scale code recommendation</li>
  <li><strong><a href="https://openreview.net/pdf?id=rkgNKkHtvB">Efficient Transformers</a></strong> – Locality-Sensitive Hashing (LSH) for computational efficiency</li>
  <li><strong><a href="https://eng.uber.com/lsh/">Fraud Detection</a></strong> – Spatial anomaly detection using LSH at Uber</li>
  <li><strong><a href="https://www.aclweb.org/anthology/P14-5007">Event Tracking</a></strong> – Social media monitoring through similarity-preserving hashing</li>
  <li><strong><a href="https://ai.google/research/pubs/pub34634">Image Retrieval</a></strong> – Scalable visual indexing with LSH at Google</li>
</ul>

---

### How Hashing Works
<p>
Learning to hash involves training a model to encode data points into compact representations, often binary hash codes. These are used to index items into hash tables. During retrieval, only a subset of nearby buckets are examined, significantly reducing the search space compared to exhaustive nearest neighbour methods.
</p>

<p align="center">
  <img src="/public/media/hashing.png?raw=true" alt="Locality Sensitive Hashing (LSH)" width="600" style="max-width: 100%; border-radius: 10px;"/>
  <br><em>Example of LSH in action, from the <a href="https://learning2hash.github.io/cite.html">PhD thesis of Sean Moran</a>.</em>
</p>

---

### Contribute to the Collection
<p>
This site is maintained as a community-driven literature review. If you have authored or come across a relevant paper, we encourage you to contribute via our submission form or GitHub pull request. See the <a href="contributing.html">Contributing</a> page for details.
</p>

<p>
To explore further, view the full set of indexed papers on the <a href="/papers.html">All Papers</a> page, or visit the <a href="/resources.html">Resources</a> section for foundational materials and curated tools.
</p>

---

<p style="font-size: 0.9em;">Copyright © <a href="https://sjmoran.github.io/">Sean Moran</a> 2025. All opinions are my own. If you find this resource helpful, a coffee is always appreciated <a href="https://www.buymeacoffee.com/sjmoran" target="_blank" style="color:#2563eb; text-decoration:none;">☕</a> to support its upkeep.</p>
