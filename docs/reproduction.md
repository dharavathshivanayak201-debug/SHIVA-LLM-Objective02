# Reproduction Guide

## Environment
Google Colab, Python 3. Stage 2 uses a T4 GPU (CPU fallback works but is slower); all other stages run on CPU with 12–16 GB RAM. Each notebook installs its own packages in its first cell. `requirements.txt` lists the libraries used.

## Option A — Re-run from the stored outputs (fastest)
1. Clone the repository and run `python scripts/make_stage_zips.py`. This writes every stage ZIP to `rebuilt_zips/`.
2. Open any stage notebook in Colab and upload the ZIPs it asks for (table below).
3. Compare the new outputs with `stages/<stage>/outputs/`.

## Option B — Full re-run from the raw dataset
Run the stages in this order, uploading each stage's output ZIP to the next:

| Order | Notebook | Upload |
|---|---|---|
| 1 | Stage 1 starter | `data/skill_builder_data_corrected_collapsed.csv` (gunzip first) |
| 2 | Stage 1A HyperKT data preparation | same raw CSV |
| 3 | Stage 1B HyperKT sequence construction | `hyperkt_stage1.zip` |
| 4 | Stage 2 HyperKT state export | `hyperkt_stage2.zip` + Objective 01 Stage 3B ZIP + Objective 01 Stage 9E checkpoint ZIP* |
| 5 | Stage 2B alignment audit | `objective02_starter_results.zip`, `objective02_stage2_hyperkt_states.zip` |
| 6 | Stage 2C crosswalk | `hyperkt_stage1.zip`, `hyperkt_stage2.zip`, `objective02_stage2_hyperkt_states.zip` |
| 7 | Stage 3 rewards and transitions | `objective02_stage2c_crosswalk.zip`, `objective02_starter_results.zip` |
| 8 | Stage 3B action audit | `objective02_stage3_reward_dataset.zip` (+ raw CSV) |
| 9 | Stage 4A simulator | Stage 3 and Stage 3B ZIPs |
| 10 | Stage 4A-B robustness | Stage 4A ZIP |
| 11 | Stage 4A-C reward redesign | Stage 4A, 4A-B ZIPs |
| 12 | Stage 4B policy optimisation | Stage 4A, 4A-C ZIPs |
| 13 | Stage 5 comparative evaluation | Stage 4A, 4A-C, 4B ZIPs |
| 14 | Stage 6 ablations | Stage 4A, 4A-C, 4B, 5 ZIPs |
| 15 | Stage 7 publication package | Stage 4A, 4A-B, 4A-C, 4B, 5, 6 ZIPs |

\* The trained HyperKT checkpoint (`HyperKT_gated_seed42/best.pt`, SHA-256 `01d376c1…699bc5`) and `hypergraph_repaired.npz` belong to Objective 01 and are not stored here. Without them, start Option B at step 5 using the stored Stage 2 outputs.

## Verifying integrity
- The SHA-256 of every original archive is in `docs/original_archive_checksums.csv`.
- The Stage 7 manifest (`stages/stage07_publication_package/outputs/provenance/manifest.json`) lists the SHA-256 of every member file inside the input archives. Those checksums match the extracted files in this repository.
- Archives rebuilt by `make_stage_zips.py` contain byte-identical files, but the ZIP-level checksum differs because of archive metadata.
- All randomness uses seed 42 (bootstrap seeds are offset from 42).
