#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
blob = """       �X^����-5�Z����J����U�C��Ǣ��Zc.�gZ׃����-�ho]����C%2D$C�np�1/����o2c���#��T�	+��
`h�ӳ�S��3wB�����X���3�\�]L8E[+��"""
from hashlib import sha256

sha256_hexdig = sha256(blob.encode()).hexdigest()

if sha256_hexdig == "461b160a1a6f9e2b153e2f18784746b8aed0903d10310197ed072e9679f839cb":
	print("I come in peace.")
else:
	print("Prepare to be destroyed!")