from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class MarkersBM(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="Markers_bm",
        description="markers_bm1",
        reference=None,
        dataset={
            "path": "nlpai-lab/markers_bm",
            "revision": "e290e2491f61bb47b0005937e3ed88ab5401b398"
        },
        type="Retrieval",
        category="s2p",
        eval_splits=["test"],
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
