#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��SGB�4.E�LZS/rB�-� �nB�s�%wL+�n�\?��U:�WO��K.�}u}@�ʚ�\B��🤖7��{��{�*u�Fp�d�VҤ1�i�~aC� ��?r��d}�$-��ų�H���D�T�
"""
from hashlib import sha256
print sha256(blob).hexdigest()