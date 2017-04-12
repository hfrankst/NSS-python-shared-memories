import sys
import pickle 

class Mary:

	def __init__(self):
		self.dictionary = dict()

	def serialize_dictionary(self):
		"""
		this method will serialize the lists stored in the dictionary in the messages file. Serialization means the process of translating data structures or object state into a format that can be stored (for example, in a file or memory buffer, or transmitted across a network connection link) and reconstructed later in the same or another computer environment. (wikipedia answer)

		Will need to use pickle functions to manipulate the data
		"""

	def deserialize_dict(self):
		"""
		this method will unpickle the data, turning it back into a more readable format	
		"""