---
layout: publication
title: Jochre 3 And The Yiddish OCR Corpus
authors: Assaf Urieli, Amber Clooney, Michelle Sigiel, Grisha Leyfer
conference: Arxiv
year: 2025
bibkey: urieli2025jochre
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.08442'}]
tags: ["Datasets", "Text Retrieval"]
short_authors: Urieli et al.
---
We describe the construction of a publicly available Yiddish OCR Corpus, and
describe and evaluate the open source OCR tool suite Jochre 3, including an
Alto editor for corpus annotation, OCR software for Alto OCR layer generation,
and a customizable OCR search engine. The current version of the Yiddish OCR
corpus contains 658 pages, 186K tokens and 840K glyphs. The Jochre 3 OCR tool
uses various fine-tuned YOLOv8 models for top-down page layout analysis, and a
custom CNN network for glyph recognition. It attains a CER of 1.5% on our test
corpus, far out-performing all other existing public models for Yiddish. We
analyzed the full 660M word Yiddish Book Center with Jochre 3 OCR, and the new
OCR is searchable through the Yiddish Book Center OCR search engine.