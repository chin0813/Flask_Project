import json
class Model:
	def read(_self,args):
		if not _self._storage:
			return "Missing stroage path for model {}".format(_self._name or "")
		with open('modules/'+_self._storage) as f:
			records = json.load(f)
		if ("ids" not in args) or (len(args["ids"])) == 0:
			return records
		else:
			vals = []
			for i in args["ids"]:
				if not any(d['id'] == i for d in records):
					return "ID {} does not exist in model {}".format(i,_self._name or "") 
				else:
					vals.append(next(d for d in records if d["id"]==i))
			return vals,200


