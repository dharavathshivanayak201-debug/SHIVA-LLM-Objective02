# Reproduction Guide

Run the notebooks in `notebooks/` in stage order on Google Colab (Python 3, CPU). Each stage uploads the ZIP outputs of earlier stages and produces its own ZIP.

| Stage | Required inputs |
|---|---|
| 6 | Stage 4A, 4A-C, 4B, 5 ZIPs |
| 7 | Stage 4A, 4A-B, 4A-C, 4B, 5, 6 ZIPs |

Verify outputs against `manifests/` (SHA-256 checksums from the Stage 7 package).
