---
title: "RoSHI: A Versatile Robot-oriented Suit for Human Data In-the-Wild"
authors:
- Wenjing Margaret Mao
- Jefferson Ng
- Luyang Hu
- Daniel Gehrig
- Antonio Loquercio
author_notes:
#date: "2026-04-08T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2026-04-08T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*"
publication_short: ""

abstract: "Scaling up robot learning will likely require human data containing rich and long-horizon interactions in the wild. Existing approaches for collecting such data trade off portability, robustness to occlusion, and global consistency. We introduce RoSHI, a hybrid wearable that fuses low-cost sparse IMUs with the Project Aria glasses to estimate the full 3D pose and body shape of the wearer in a metric global coordinate frame from egocentric perception. This system is motivated by the complementarity of the two sensors: IMUs provide robustness to occlusions and high-speed motions, while egocentric SLAM anchors long-horizon motion and stabilizes upper body pose. We collect a dataset of agile activities to evaluate RoSHI. On this dataset, we generally outperform other egocentric baselines and perform comparably to a state-of-the-art exocentric baseline (SAM3D). Finally, we demonstrate that the motion data recorded from our system are suitable for real-world humanoid policy learning."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Robotics
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/pdf/2604.07331
url_code: 'https://github.com/Jirl-upenn/RoSHI-MoCap'
url_dataset: ''
url_poster: ''
url_project: 'https://roshi-mocap.github.io/'
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
