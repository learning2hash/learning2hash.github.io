---
layout: publication
title: 'Automatic Histograms: Leveraging Language Models For Text Dataset Exploration'
authors: Emily Reif, Crystal Qian, James Wexler, Minsuk Kahng
conference: Extended Abstracts of the CHI Conference on Human Factors in Computing
  Systems
year: 2024
bibkey: reif2024automatic
citations: 7
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2402.14880'}]
tags: ["Datasets"]
short_authors: Reif et al.
---
Making sense of unstructured text datasets is perennially difficult, yet
increasingly relevant with Large Language Models. Data workers often rely on
dataset summaries, especially distributions of various derived features. Some
features, like toxicity or topics, are relevant to many datasets, but many
interesting features are domain specific: instruments and genres for a music
dataset, or diseases and symptoms for a medical dataset. Accordingly, data
workers often run custom analyses for each dataset, which is cumbersome and
difficult. We present AutoHistograms, a visualization tool leveragingLLMs.
AutoHistograms automatically identifies relevant features, visualizes them with
histograms, and allows the user to interactively query the dataset for
categories of entities and create new histograms. In a user study with 10 data
workers (n=10), we observe that participants can quickly identify insights and
explore the data using AutoHistograms, and conceptualize a broad range of
applicable use cases. Together, this tool and user study contributeto the
growing field of LLM-assisted sensemaking tools.