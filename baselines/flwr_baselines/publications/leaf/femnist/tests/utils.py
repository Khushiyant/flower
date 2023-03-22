import tempfile
from pathlib import Path

import PIL
import numpy as np
from PIL import Image


def recreate_nist():
    temp_dir = tempfile.TemporaryDirectory()
    raw_dir = Path(temp_dir.name) / "raw"
    (raw_dir / "by_write" / "hsf_0" / "a" / "c000_sth").mkdir(parents=True)
    (raw_dir / "by_write" / "hsf_0" / "b" / "c000_sth").mkdir(parents=True)
    (raw_dir / "by_class" / "4a" / "hsf_0").mkdir(parents=True)
    (raw_dir / "by_class" / "4b" / "hsf_0").mkdir(parents=True)

    # create 5 PNG files for directory "a" in "by_write"
    for i in range(3):
        img = create_random_image()
        img_path = raw_dir / "by_write" / "hsf_0" / "a" / "c000_sth" / f"{i}.png"
        img.save(img_path)
        (raw_dir / "by_class" / "4a" / "hsf_0" / f"{i}.png").symlink_to(img_path)
    for i in range(3, 5):
        img = create_random_image()
        img_path = raw_dir / "by_write" / "hsf_0" / "a" / "c000_sth" / f"{i}.png"
        img.save(img_path)
        (raw_dir / "by_class" / "4b" / "hsf_0" / f"{i}.png").symlink_to(img_path)
    # create 8 PNG files for directory "b" in "by_write"
    for i in range(4):
        img = create_random_image()
        img_path = raw_dir / "by_write" / "hsf_0" / "b" / "c000_sth" / f"{i}.png"
        img.save(img_path)
        (raw_dir / "by_class" / "4a" / "hsf_0" / f"{i + 3}.png").symlink_to(img_path)
    for i in range(4, 8):
        img = create_random_image()
        img_path = raw_dir / "by_write" / "hsf_0" / "b" / "c000_sth" / f"{i}.png"
        img.save(img_path)
        (raw_dir / "by_class" / "4b" / "hsf_0" / f"{i + 1}.png").symlink_to(img_path)
    return temp_dir


def create_random_image() -> PIL.Image:
    arr = np.random.randint(0, 255, size=(128, 128), dtype=np.uint8)
    img = Image.fromarray(arr)
    return img
