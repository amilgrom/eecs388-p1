#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��SGB�4.E�LZS/rB�-� �nB�s�%wL+�n�\?��U:�WO��K.�}u}@�ʚ�\B��🤖7��{��{�*u�Fp�d�VҤ1�i�~aC� ��?r��d}�$-��ų�H���D�T�
"""
from hashlib import sha256
hashed = sha256(blob).hexdigest()
goodSha256Hash = """307bc5293876f43d2fb092d0d243709fb08b8500bc9e6ca63e425c96202e7ba7"""
if (hashed == goodSha256Hash):
	print "I come in peace."
else:
	print "Prepare to be destroyed!"