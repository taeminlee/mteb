from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class OntheITBM2(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="OntheITBM2-filtered-split",
        description="ontheit_bm2",
        reference=None,
        dataset={
            "path": "KU-HIAI-ONTHEIT/ontheit_benchmark_2",
            "revision": "3756e1427a4d52cb6e2c290b665ec8b8fdbfb71a"
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["dev"],
        eval_langs=["kor-Hang"],
        main_score="ndcg_at_10",
        date=None,
        form=None,
        domains=None,
        task_subtypes=None,
        license=None,
        socioeconomic_status=None,
        annotations_creators=None,
        dialect=None,
        text_creation=None,
        bibtex_citation="""""",
        n_samples=None,
        avg_character_length=None,
    )
