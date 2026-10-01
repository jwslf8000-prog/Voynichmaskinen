#!/usr/bin/env python3
"""Adaptive experiment scheduler for Voynichmaskinen.

This module schedules tests; scientific test functions are registered separately.
It never fabricates a result. A child test can only be scheduled from a completed
parent whose result contains a next_question.
"""
from dataclasses import dataclass, asdict
import json, pathlib

@dataclass
class TestRecord:
    test_id: int
    parent_test_id: int | None
    question: str
    family: str
    hypotheses: list[str]
    seed: int
    status: str = "planned"
    result: dict | None = None
    new_questions: list[str] | None = None
    next_question: str | None = None

FAMILIES = [
    "core_function","prefix_function","suffix_function","position",
    "cross_line","folio_section","minimal_pairs","repeated_constructions",
    "image_labels","reverse_prediction","taxonomy","language_morphology",
    "generative_code"
]

def next_id(records):
    return 1 if not records else max(r["test_id"] for r in records)+1

def schedule_child(records, parent, family, hypotheses, seed):
    if parent["status"] != "complete":
        raise ValueError("Parent must be complete")
    q = parent.get("next_question")
    if not q:
        raise ValueError("Completed parent has no next_question")
    return TestRecord(next_id(records), parent["test_id"], q, family,
                      hypotheses, seed)

def append(path, record):
    p=pathlib.Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("a",encoding="utf-8") as f:
        f.write(json.dumps(asdict(record),ensure_ascii=False)+"\n")

if __name__=="__main__":
    print("Adaptive 100k scheduler ready; no synthetic results are generated.")
