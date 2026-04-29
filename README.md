# Foxhole Map Mod Packer

Python tool for creating custom HD map mods for Foxhole (Update 63+) using provided textures

## Requirements

### Texture Requirements
- All textures must be 2048x1776 RGBA

### Python Dependencies

- Python 3.7 or higher
- numpy
- Pillow (PIL)

```bash
pip install numpy pillow
```

### BC7 Encoder

Included `bc7_encoder.cp31*-win_amd64.pyd` binaries will work if you use Python 3.13 or 3.14 on a Windows Machine, otherwise you'll need to build encoder yourself.
BC7 encoder is a compiled C++ extension that provides texture compression into expected pixel format.

- General build requirements:
  - **Cython**: For compiling the Python extension
  - **numpy**: Development headers (included with numpy installation)
- Windows requirements:
  - Microsoft Visual C++ Build Tools
- Linux requirements:
  - `g++` and `python3-dev` (`sudo apt-get install python3-dev build-essential`)

Build with:
```bash
python build_encoder.py
```

## Layers

High-resolution stitched map layers for compositing custom maps are available at [Tsekho/fh_map_exporter](https://github.com/Tsekho/fh_map_exporter/tree/main/export/_final). Combine layers using your preferred image editing software.

## Usage

### Basic Usage

This module provides five main functions:

#### 1. `pak` - Package a generic mod

Accepts a dictionary of file paths and their binary data:

```python
from paker import pak

files = {
    "War/Content/Textures/MyTexture.uasset": b"...",
    "War/Content/Data/MyData.uasset": b"..."
}

pak("output", files, compress=True)
```

#### 2. `pak_textures_bc7` - Package Pre-Compressed BC7 Textures

Use this when you already have BC7-compressed texture data (must be exactly 3,637,248 bytes per texture):

```python
from paker import pak_textures_bc7, HEADERS

with open("example/texture", "rb") as f:
    texture_data = f.read()

mappings = {map_name: texture_data for map_name in HEADERS}

pak_textures_bc7("output", compress=True, mappings=mappings)
```

#### 3. `pak_textures_nprgba` - Package numpy array RGBA Images

Compress numpy RGBA images to BC7 format and package them. **Requires the BC7 encoder to be built.**

```python
from paker import pak_textures_nprgba, HEADERS
import numpy as np
from PIL import Image

image = np.array(Image.open("example/texture.png"))

mappings = {map_name: image for map_name in HEADERS}

pak_textures_nprgba("output", compress=True, mappings=mappings)
```

#### 4. `pak_textures_folder` - Package Entire Folder

Process all supported image files in a folder. **Requires the BC7 encoder to be built.**

```python
from paker import pak_textures_folder

pak_textures_folder("output", compress=True, folder="path/to/textures")
```

#### 5. `pak_stitched` - Package Stitched Map Image

Break a full stitched map image into individual regions and package. **Requires the BC7 encoder to be built.**

The stitched image must be in the exact format of the layers linked above.

This is particularly useful for creating mods from those layers:

```python
from paker import pak_stitched

pak_stitched("my_custom_map", compress=True, stitched_image="my_custom_map.png")
```

## Project Structure

```
.
├── paker.py                 # Main module with packaging functions
├── build_encoder.py         # Script to build the BC7 encoder extension
├── bc7_encoder*.pyd/.so     # Compiled BC7 encoder
├── bc7_src/                 # BC7 encoder source files
├── assets/
│   ├── WorldMapBG.uasset    # Upscaled background texture
│   ├── mask.png             # Alpha mask for region extraction
│   └── headers/             # Binary headers for each map region
│       ├── MapAcrithiaHex
│       ├── MapAllodsBightHex
│       └── ... (All 55 map headers)
└── example/
    ├── texture              # Sample BC7 texture data
    └── texture.png          # Sample PNG texture
```
