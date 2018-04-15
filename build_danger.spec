# -*- mode: python -*-

block_cipher = None

a = Analysis(['danger.py'],
             pathex=[''],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=['./hooks'],
             runtime_hooks=['hooks/rthook-Crypto.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='danger',
          debug=False,
          strip=False,
          upx=True,
          console=True)