
class HS:

	_tbl = []
	def __init__(self, f):
		self.load(f)
	def __str__(self) -> str:
		return '\n'.join(['\t'.join(i) for i in self._tbl])
	def load(self, f):
		self._tbl = set()
		with open(f, 'r', encoding='utf-8') as f:
			for l in f.readlines():
				p = l.strip().split('\t')
				if len(p) > 1:
					self._tbl.add((p[0], p[1]))
		self._tbl = sorted(self._tbl, key=lambda x: (len(x[0]), x[0]), reverse=True)

	def __sp(self, d, s):
		ret = []
		tmp = ''
		for c in s:
			hit = False
			for i in d:
				if c == i:
					if len(tmp) > 0:
						ret.append(tmp)
						tmp = ''
					ret.append(c)
					hit = True
					break
			if not hit:
				tmp += c
		ret.append(tmp)
		return ret

	def __rep(self, l):
		ret = []
		for i in l:
			if i == '\\':
				continue
			if i == 'n':
				continue
			if i == '　':
				continue			
			if len(i) < 1:
				continue
			a = '▣'
			for j in self._tbl:
				if i == j[0]:
					a = j[1]
					break
			ret.append(a)
		return ret

	import re

	def conv(self, q):
		s = self.__sp(r'……—―。、「」！？　\n', q)
		s = self.__rep(s)
		s = ''.join(s)
		s = re.sub(r'…[。，！？]', '…', s)
		return s
