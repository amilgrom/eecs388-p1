#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��SGB�4.E�LZS/rB+-� �nB�s�%wL+�n�\?��U:��N��K.�}u}@�J��\B��🤖7��{��{�*u��p�d�VҤ1�i�~aC� ��?r�e}�$-��ų�H��fD�T�
"""
from hashlib import sha256
print sha256(blob).hexdigest()