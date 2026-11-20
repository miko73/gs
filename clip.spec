# -*- mode: python ; coding: utf-8 -*-
#
# Build:  .\.venv\Scripts\python.exe -m PyInstaller clip.spec --noconfirm
# Vysledek: dist\clip.exe  (service account JSON se kopiruje vedle nej rucne)

a = Analysis(
    ['clip.py'],
    pathex=[],
    binaries=[],
    datas=[],
    # grpc a google.auth si cast modulu nacitaji dynamicky, PyInstaller je sam nenajde
    hiddenimports=[
        'google.cloud.texttospeech',
        'google.auth.transport.requests',
        'grpc',
    ],
    hookspath=[],
    runtime_hooks=[],
    # nepouzivane knihovny - zbytecne by nafoukly vystup
    excludes=['tkinter', 'numpy', 'pandas', 'matplotlib', 'PIL', 'scipy'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='clip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
