"""Rebuild the stage ZIP archives that the Colab notebooks expect as uploads.

Usage:  python scripts/make_stage_zips.py [output_dir]

Each notebook asks for the ZIP produced by earlier stages (for example Stage 5 asks for
objective02_stage4a_simulator.zip). This script packs every stages/<stage>/outputs folder
back into the archive name the notebooks look for. Files stored as *.gz in this
repository are decompressed back to their original names.

Note: rebuilt archives contain the same files but will not have the same SHA-256 as the
original archives listed in docs/original_archive_checksums.csv (ZIP metadata differs).
"""
import gzip, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    "stage01_starter_baseline": "objective02_starter_results.zip",
    "stage01a_hyperkt_data_preparation": "hyperkt_stage1.zip",
    "stage01b_hyperkt_sequence_construction": "hyperkt_stage2.zip",
    "stage02_hyperkt_state_export": "objective02_stage2_hyperkt_states.zip",
    "stage02b_event_alignment_audit": "objective02_stage2b_audit.zip",
    "stage02c_event_crosswalk": "objective02_stage2c_crosswalk.zip",
    "stage03_reward_and_transitions": "objective02_stage3_reward_dataset.zip",
    "stage03b_action_transition_audit": "objective02_stage3b_action_transition_audit.zip",
    "stage04a_simulator": "objective02_stage4a_simulator.zip",
    "stage04ab_robustness_audit": "objective02_stage4ab_robustness_audit.zip",
    "stage04ac_reward_redesign": "objective02_stage4ac_reward_redesign.zip",
    "stage04b_policy_optimization": "objective02_stage4b_policy_optimization.zip",
    "stage05_comparative_evaluation": "objective02_stage5_comparative_evaluation.zip",
    "stage06_ablation_analysis": "objective02_stage6_ablation_analysis.zip",
    "stage07_publication_package": "objective02_stage7_publication_package.zip",
}

def main(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for stage, name in ARCHIVES.items():
        src = ROOT / "stages" / stage / "outputs"
        with zipfile.ZipFile(out_dir / name, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(p for p in src.rglob("*") if p.is_file()):
                rel = f.relative_to(src).as_posix()
                if f.suffix == ".gz":
                    z.writestr(rel[:-3], gzip.decompress(f.read_bytes()))
                else:
                    z.write(f, rel)
        print("wrote", out_dir / name)

if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "rebuilt_zips")
