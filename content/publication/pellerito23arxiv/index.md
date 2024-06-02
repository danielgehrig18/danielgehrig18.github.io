---
title: "End-to-End Learned Event- and Image-based Visual Odometry"
authors:
- Roberto Pellerito
- Marco Cannici
- Daniel Gehrig
- Joris Belhadj
- Olivier Dubois-Matra
- Massimo Casasco
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-03-20T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*arXiv*"
publication_short: ""

abstract: "Visual Odometry (VO) is crucial for autonomous robotic navigation, especially in GPS-denied environments like planetary terrains. While standard RGB cameras struggle in low-light or high-speed motion, event-based cameras offer high dynamic range and low latency. However, seamlessly integrating asynchronous event data with synchronous frames remains challenging. We introduce RAMP-VO, the first end-to-end learned event- and image-based VO system. It leverages novel Recurrent, Asynchronous, and Massively Parallel (RAMP) encoders that are 8x faster and 20% more accurate than existing asynchronous encoders. RAMP-VO further employs a novel pose forecasting technique to predict future poses for initialization. Despite being trained only in simulation, RAMP-VO outperforms image- and event-based methods by 52% and 20%, respectively, on traditional, real-world benchmarks as well as newly introduced Apollo and Malapert landing sequences, paving the way for robust and asynchronous VO in space."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/Arxiv23_Pellerito.pdf
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
