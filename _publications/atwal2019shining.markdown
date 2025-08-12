---
layout: publication
title: 'Shining A Light On Spotlight: Leveraging Apple''s Desktop Search Utility To
  Recover Deleted File Metadata On Macos'
authors: Tajvinder Singh Atwal, Mark Scanlon, Nhien-An Le-Khac
conference: Digital Investigation
year: 2019
bibkey: atwal2019shining
citations: 6
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1903.07053'}]
tags: []
short_authors: Tajvinder Singh Atwal, Mark Scanlon, Nhien-An Le-Khac
---
Spotlight is a proprietary desktop search technology released by Apple in
2004 for its Macintosh operating system Mac OS X 10.4 (Tiger) and remains as a
feature in current releases of macOS. Spotlight allows users to search for
files or information by querying databases populated with filesystem
attributes, metadata, and indexed textual content. Existing forensic research
into Spotlight has provided an understanding of the metadata attributes stored
within the metadata store database. Current approaches in the literature have
also enabled the extraction of metadata records for extant files, but not for
deleted files. The objective of this paper is to research the persistence of
records for deleted files within Spotlight's metadata store, identify if
deleted database pages are recoverable from unallocated space on the volume,
and to present a strategy for the processing of discovered records. In this
paper, the structure of the metadata store database is outlined, and
experimentation reveals that records persist for a period of time within the
database but once deleted, are no longer recoverable. The experimentation also
demonstrates that deleted pages from the database (containing metadata records)
are recoverable from unused space on the filesystem.