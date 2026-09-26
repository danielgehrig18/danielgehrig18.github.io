---
title: "Neural Events: Discrete Asynchronous Autoencoders for Event-Based Vision"
authors:
- Roberto Pellerito
- Daniel Gehrig
- Shintaro Shiba
- Davide Scaramuzza
author_notes:
#date: "2026-06-18T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2026-06-18T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*arXiv*"
publication_short: ""

abstract: "Event cameras capture dynamic scenes with exceptional temporal fidelity by representing them as a continuous stream of microsecond resolution events. Each individual event, however, only carries minimal semantic value, merely signaling a localized brightness change. To derive meaningful signals, downstream algorithms need to quickly integrate cues from a potentially massive torrent of low-information events. Current architectures, however, are easily overwhelmed, struggling to balance capturing fine-grained temporal dynamics and maintaining a manageable data throughput. This paper proposes a framework to re-tokenize event streams into a small set of highly informative neural events, each representing a local spatio-temporal context window with a discrete learnable code. Every time this code flips, a neural event is triggered, yielding a highly compressed data stream. We demonstrate that, across object detection and classification, networks trained on neural events are on par or surpass the performance of state-of-the-art approaches while reducing the event rate by a factor of 2.0."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2606.19835
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
