from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class OntheITBM1(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="OntheITBM1-filtered",
        description="ontheit_bm1",
        reference=None,
        dataset={
            "path": "/data/ONTHEIT/ontheit_benchmark_1",
            "revision": "10f4db1a99e39f2163265177e5b087000420feb3"
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
