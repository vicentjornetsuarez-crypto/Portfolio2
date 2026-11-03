from pathlib import Path
import html5lib

root = Path(r"C:\Users\DAM1\portfolio")
files = sorted(root.rglob("*.html"))
print(f"HTML verificadas: {len(files)}")
ok = []
bad = []

for file in files:
    try:
        html5lib.parse(file.read_text(encoding="utf-8"), namespaceHTMLElements=False)
        ok.append(file.name)
    except Exception as exc:
        bad.append((file.name, str(exc)))

print("OK:", ", ".join(ok))
print("ERRORES:", len(bad))
if bad:
    for name, err in bad:
        print(f"{name} -> {err}")
    raise SystemExit(1)
