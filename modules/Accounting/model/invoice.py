#Yet another bad practice~ using setup.py is better than importing from root directory
from core.model import Model
class Invoice(Model):
	_name="invoice"
	# store storage path as path after "modules"
	_storage="Accounting/storage/invoices.json"