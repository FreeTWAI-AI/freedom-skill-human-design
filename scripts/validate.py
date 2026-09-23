"""Validate a public synthetic collaboration plan; never perform external actions."""
import json
import sys
from pathlib import Path


def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["plan must be an object"]
    if not isinstance(data.get("title"), str) or not data["title"].strip():
        errors.append("title is required")
    if data.get("data_classification") != "synthetic":
        errors.append("public examples must be synthetic; private records stay outside this repo")
    expected_kind = 'human-design'
    if data.get("kind") != expected_kind:
        errors.append("kind must be " + expected_kind)
    check(data, errors)
    return errors


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def records(data, key, errors):
    value = data.get(key)
    if not isinstance(value, list) or not value or not all(isinstance(item, dict) for item in value):
        errors.append(key + " must contain at least one object")
        return []
    return value


def unique_ids(items, label, errors):
    identifiers = [item.get("id") for item in items]
    if any(not isinstance(value, str) or not value.strip() for value in identifiers):
        errors.append(label + " ids must be nonempty strings")
        return set()
    if len(set(identifiers)) != len(identifiers):
        errors.append(label + " ids must be unique")
    return set(identifiers)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def check(data, errors):
    if data.get("birth_data_collected") is not False:
        errors.append("this public study template does not collect birth data")
    if not text(data.get("consent_scope")):
        errors.append("consent scope is required")
    sources = records(data, "sources", errors)
    source_ids = unique_ids(sources, "source", errors)
    for source in sources:
        if not text(source.get("title")) or not text(source.get("rights")):
            errors.append("source title and rights are required")
        url = source.get("url", "")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append("source must link to an HTTPS reading reference")
    for note in records(data, "notes", errors):
        if note.get("source_id") not in source_ids:
            errors.append("note must reference a listed source")
        if note.get("claim_type") not in ("interpretation", "personal_observation", "source_claim", "open_question"):
            errors.append("classify notes without claiming a diagnostic or scientific finding")
        for field in ("summary", "question", "limitations"):
            if not text(note.get(field)):
                errors.append("note requires " + field)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python3 scripts/validate.py <plan.json>")
    try:
        problems = validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as error:
        raise SystemExit(str(error))
    if problems:
        print("\n".join(problems), file=sys.stderr)
        raise SystemExit(1)
    print("PASS: structural checks only; no real-world activity or results verified")
