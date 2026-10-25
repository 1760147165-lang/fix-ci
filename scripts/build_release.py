"""Build the skill ZIP and a self-contained chat attachment using only stdlib."""
from pathlib import Path
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fix-ci"


def build():
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert entry.startswith("---\nname: fix-ci\n"), "Invalid skill entrypoint"
    assert "\ndescription: " in entry.split("---", 2)[1], "Missing description"
    refs = sorted(set(re.findall(r"\]\((references/[^)]+)\)", entry)))
    assert refs, "Reference workflow is missing"
    for rel in refs:
        assert (SKILL / rel).is_file(), f"Missing reference: {rel}"
    files = {"SKILL.md": entry.encode("utf-8")}
    files.update({rel: (SKILL / rel).read_bytes() for rel in refs})
    files["LICENSE.txt"] = (ROOT / "LICENSE").read_bytes()
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    archive = out / "fix-ci.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for rel, data in sorted(files.items()):
            info = zipfile.ZipInfo(f"fix-ci/{rel}", date_time=(2026, 10, 25, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == {f"fix-ci/{rel}" for rel in files}
        for rel, data in files.items():
            assert z.read(f"fix-ci/{rel}") == data
    body = entry.split("---", 2)[2].lstrip()
    for rel in refs:
        body = body.replace(f"[{rel}]({rel})", f"the included reference section `{rel}` below")
    portable = out / "fix-ci-portable.md"
    sections = ["# fix-ci portable edition\n\nRead these instructions when the user asks to apply this skill. Follow the host's capabilities and the user's task scope. Missing tools or evidence must be reported.\n\n" + body]
    for rel in refs:
        sections.append(f"\n\n---\n\n## Included reference: {rel}\n\n" + (SKILL / rel).read_text(encoding="utf-8"))
    sections.append("\n\n---\n\n## License\n\n" + files["LICENSE.txt"].decode("utf-8"))
    portable.write_text("".join(sections), encoding="utf-8")
    assert not re.search(r"\]\(references/", portable.read_text(encoding="utf-8"))
    sums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in [archive, portable])
    (out / "SHA256SUMS.txt").write_text(sums, encoding="utf-8")
    print(sums, end="")
    print(f"Validated {len(files)} archived files and self-contained text.")


if __name__ == "__main__":
    build()
