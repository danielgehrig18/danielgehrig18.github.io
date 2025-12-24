---
title: "Deep Visual Odometry with Events and Frames"
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
publication: "*IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*"
publication_short: ""

abstract: "Visual Odometry (VO) is crucial for autonomous robotic navigation, especially in GPS-denied environments like planetar y terrains. To improve robustness, recent model-based VO systems have begun combining standard and event-based cameras. While event cameras excel in low-light and high-speed motion, standard cameras provide dense and easier-to-track features. However, the field of image- and event-based VO still predominantly relies on model-based methods and is yet to fully integrate recent image-only advancements leveraging end-to-end learning-based architectures. Seamlessly integrating the two modalities remains challenging due to their different nature, one asynchronous, the other not, limiting the potential for a more effective image- and event-based VO. We introduce RAMP-VO, the first end-to-end learned image- and eventbased VO system. It leverages novel Recurrent, Asynchronous, and Massively Parallel (RAMP) encoders capable of fusing asynchronous events with image data, providing 8× faster inference and 33% more accurate predictions than existing solutions. Despite being trained only in simulation, RAMP-VO outperforms previous methods on the newly introduced Apollo and Malapert datasets, and on existing benchmarks, where it improves image- and event-based methods by 58.8% and 30.6%, paving the way for robust and asynchronous VO in space."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/IROS24_Pellerito.pdf
url_code: 'https://github.com/uzh-rpg/rampvo'
url_dataset: 'https://github.com/uzh-rpg/rampvo'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/mzSQR2MEAsU'

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
