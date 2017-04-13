import sys
import pickle 


class Mary:

	def __init__(self):
		self.empty_dict = dict()
		self.mary_list = list()
		try:
			self.empty_dict = self.deserialize_dict()
		except FileNotFoundError:
			pass


	def serialize_dictionary(self):
		"""
		this method will serialize the lists stored in the dictionary in the messages file. Serialization means the process of translating data structures or object state into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and reconstructed later in the same or another computer environment. (wikipedia answer)

		"""
		self.mary_list.extend(sys.argv[1:])
		self.empty_dict['Mary'] = self.mary_list
		print(self.empty_dict)

		# with statement is opening the file that is being serialized to, the module pickle needs to be used with its 'dump' method and pass the object as well as the file that I want it to be written to, then I close the file so that it is secure
		with open('messages', 'wb') as entry:
			pickle.dump(self.empty_dict, entry)

	def deserialize_dict(self):
		"""
		this method will unpickle the data, turning it back into a more readable format	
		this try except block will read the message
		"""
		try:
		    with open('messages', 'rb') as entry:
		        self.empty_dict = pickle.load(entry)
		except EOFError:
		    pass

		return self.empty_dict


m = Mary()
m.serialize_dictionary()
m.deserialize_dict()
