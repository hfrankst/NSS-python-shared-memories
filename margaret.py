import sys
import pickle

class Margaret:

	def __init__(self):
		self.empty_dict = dict()
		self.margaret_list = list()
		try:
			self.empty_dict = self.deserialize_dict()
		except FileNotFoundError:
			pass


	def serialize_dict(self): 
		"""
		This method will serialize or convert the data into a format that is easier for the computer to transfer around
		""" 
		self.margaret_list.extend(sys.argv[1:])
		self.empty_dict['Margaret'] = self.margaret_list
		print(self.empty_dict)

		with open('messages', 'wb') as entry:
			pickle.dump(self.empty_dict, entry)
		
	def deserialize_dict(self):
		"""
		this method will unpickle the data, turning it back into a more readable format	
		"""
		try:
		    with open('messages', 'rb') as entry:
		        self.empty_dict = pickle.load(entry)
		except EOFError:
		    pass

		return self.empty_dict
		
marg = Margaret()
marg.serialize_dict()
marg.deserialize_dict()