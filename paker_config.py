from __future__ import annotations

import os
from pathlib import Path

_DIR = Path(__file__).resolve().parent


def _env_path(name: str, default: Path) -> Path:
    value = os.getenv(name)
    if not value:
        return default
    return Path(value).expanduser()


ASSETS_DIR = _env_path("FH_PAKER_ASSETS_DIR", _DIR / "assets")
HEADERS_DIR = _env_path("FH_PAKER_HEADERS_DIR", ASSETS_DIR / "headers")
MASK_PATH = _env_path("FH_PAKER_MASK_PATH", ASSETS_DIR / "mask.png")
WORLDMAP_BG_UASSET_PATH = _env_path(
    "FH_PAKER_WORLDMAP_BG_UASSET_PATH",
    ASSETS_DIR / "WorldMapBG.uasset",
)
LAYER_COLLECTION_DIR = _env_path(
    "FH_PAKER_LAYER_COLLECTION_DIR",
    _DIR / "layer_collection",
)

BG_PATH = r"War\Content\Textures\UI\WorldMap\WorldMapBG.uasset"

HEADER_NAMES = {
    "MapAcrithiaHex": [11804, 10792],
    "MapAllodsBightHex": [13344, 8128],
    "MapAshFieldsHex": [7184, 9904],
    "MapBasinSionnachHex": [10264, 1024],
    "MapCallahansPassageHex": [10264, 4576],
    "MapCallumsCapeHex": [7184, 2800],
    "MapClahstraHex": [13344, 6352],
    "MapClansheadValleyHex": [13344, 2800],
    "MapDeadlandsHex": [10264, 6352],
    "MapDrownedValeHex": [11804, 7240],
    "MapEndlessShoreHex": [14884, 7240],
    "MapFarranacCoastHex": [5644, 5464],
    "MapFishermansRowHex": [4104, 6352],
    "MapGodcroftsHex": [16424, 4576],
    "MapGreatMarchHex": [10264, 9904],
    "MapGutterHex": [4104, 4576],
    "MapHeartlandsHex": [8724, 9016],
    "MapHomeRegionC": [19504, 11680],
    "MapHomeRegionW": [1024, 1024],
    "MapHowlCountyHex": [11804, 1912],
    "MapKalokaiHex": [10264, 11680],
    "MapKingsCageHex": [7184, 6352],
    "MapKuuraStrandHex": [4104, 2800],
    "MapLinnMercyHex": [8724, 5464],
    "MapLochMorHex": [8724, 7240],
    "MapLykosIsleHex": [17964, 5464],
    "MapMarbanHollowHex": [11804, 5464],
    "MapMooringCountyHex": [8724, 3688],
    "MapMorgensCrossingHex": [14884, 3688],
    "MapNevishLineHex": [5644, 3688],
    "MapOarbreakerHex": [2564, 7240],
    "MapOlavisWakeHex": [1024, 4576],
    "MapOnyxHex": [16424, 9904],
    "MapOriginHex": [5644, 9016],
    "MapPalantineBermHex": [2564, 5464],
    "MapPariPeakHex": [2564, 3688],
    "MapPipersEnclaveHex": [19504, 8128],
    "MapReachingTrailHex": [10264, 2800],
    "MapReaversPassHex": [14884, 9016],
    "MapRedRiverHex": [8724, 10792],
    "MapSableportHex": [7184, 8128],
    "MapShackledChasmHex": [11804, 9016],
    "MapSpeakingWoodsHex": [8724, 1912],
    "MapStemaLandingHex": [4104, 8128],
    "MapStlicanShelfHex": [14884, 5464],
    "MapStonecradleHex": [7184, 4576],
    "MapTempestIslandHex": [16424, 6352],
    "MapTerminusHex": [13344, 9904],
    "MapTheFingersHex": [17964, 7240],
    "MapTyrantFoothillsHex": [17964, 9016],
    "MapUmbralWildwoodHex": [10264, 8128],
    "MapViperPitHex": [11804, 3688],
    "MapWeatheredExpanseHex": [13344, 4576],
    "MapWestgateHex": [5644, 7240],
    "MapWrestaHex": [16424, 8128],
}
