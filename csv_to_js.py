from pathlib import Path

ROOT = Path(__file__).parent
FILES = [("sat20",  "SAT20_CSV"),
         ("jupe20", "JUPE20_CSV"),
         ("ven10",  "VEN10_CSV")]

for stem, varname in FILES:
    src = ROOT / "data" / f"{stem}.csv"
    dst = ROOT / "data" / f"{stem}.js"
    txt = src.read_text(encoding="utf-8")

    txt = txt.replace("\\", "\\\\")   # \
    txt = txt.replace("`",  "\\`")    #  `
    txt = txt.replace("${", "\\${")   # ${

    dst.write_text(f"window.{varname} = `\n{txt}`;\n", encoding="utf-8")
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
