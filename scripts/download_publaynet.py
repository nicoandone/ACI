import argparse
import json
from pathlib import Path

from datasets import load_dataset
from PIL import ImageDraw

CATEGORIES = {1: "text", 2: "title", 3: "list", 4: "table", 5: "figure"}
COLORS = {1: "blue", 2: "red", 3: "orange", 4: "green", 5: "purple"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=100)
    parser.add_argument("--split", default="validation")
    parser.add_argument("--out", default="data/publaynet")
    args = parser.parse_args()

    out = Path(args.out)
    (out / "images").mkdir(parents=True, exist_ok=True)
    (out / "gt_preview").mkdir(parents=True, exist_ok=True)

    ds = load_dataset("jordanparker6/publaynet", split=args.split, streaming=True)

    coco = {"images": [], "annotations": [], "categories": [{"id": k, "name": v} for k, v in CATEGORIES.items()]}

    for sample in ds.take(args.n):
        img = sample["image"].convert("RGB")
        img_id = sample["id"]
        fname = f"{img_id}.png"
        img.save(out / "images" / fname)
        coco["images"].append({"id": img_id, "file_name": fname, "width": img.width, "height": img.height})

        preview = img.copy()
        draw = ImageDraw.Draw(preview)
        for ann in sample["annotations"]:
            x, y, w, h = ann["bbox"]
            cat = ann["category_id"]
            coco["annotations"].append({"id": len(coco["annotations"]), "image_id": img_id, "category_id": cat, "bbox": [x, y, w, h]})
            draw.rectangle([x, y, x + w, y + h], outline=COLORS[cat], width=2)
            draw.text((x + 2, y + 2), CATEGORIES[cat], fill=COLORS[cat])
        preview.save(out / "gt_preview" / fname)

    with open(out / "annotations.json", "w") as f:
        json.dump(coco, f, indent=1)


if __name__ == "__main__":
    main()
