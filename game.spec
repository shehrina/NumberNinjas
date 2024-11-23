# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Game.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/rawad/Desktop/CS2212 Project/group6/save_data.csv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Game',
)
app = BUNDLE(
    coll,
    name='Game.app',
    icon=None,
    bundle_identifier=None,
)
