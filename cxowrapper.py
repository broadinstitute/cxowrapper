import pdb

try:
	import cx_Oracle as cxo
except BaseException as e:
	pdb.set_trace()

class cxowrapper(object):
	def __init__(self, connstr):
		self.conn = cxo.Connection(connstr)
		self.cursor = cxo.Cursor(self.conn)

	def queryAll(self, sql):
		aRows = []
		self.execute(sql)
		rows = self.cursor.fetchall()
		columns = self.cursor.description
		for row in rows:
			aRow = {}
			for i in xrange(len(columns)):
				aRow[columns[i][0]] = row[i]
			aRows.append(aRow)
		return aRows

	def queryRow(self, sql):
		self.execute(sql)
		row = self.cursor.fetchone()
		if not row:
			return None
		columns = self.cursor.description
		aRow = {}
		for i in xrange(len(columns)):
			aRow[columns[i][0]] = row[i]
		return aRow

	def queryOne(self, sql):
		self.execute(sql)
		row = self.cursor.fetchone()
		return row[0] if row else None

	def execute(self, sql):
		self.cursor.execute(sql)

