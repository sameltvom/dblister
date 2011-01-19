import rb
import rhythmdb
import gtk

class DblisterPlugin (rb.Plugin):
	def __init__(self):
		rb.Plugin.__init__(self)
	def activate(self, shell):
		self.shell = shell
		print '##### dblister #####'

		
		print '--- Trying to print using library_source'
		for row in self.shell.props.library_source.props.base_query_model:
		 	entry = row[0]
		 	artist = self.shell.props.db.entry_get(entry, rhythmdb.PROP_ARTIST)
			print artist


		##################### Print all artists in database ######################

		# loop through all songs currently selected (i.e. all songs since we did p.set_selection([""]) above
		# for each song, try to add the artist name to the 'artists' set
		artists = set() # unique keys, no duplicates
		for row in self.shell.props.selected_source.props.base_query_model:
		 	entry = row[0]
		 	artist = self.shell.props.db.entry_get(entry, rhythmdb.PROP_ARTIST)
			artists.add(artist)

		print '--- artists ---'
		for artist in artists:
			print artist


		##################### Print all songs in database ######################

		print '--- songs ---'
		# loop through all songs currently selected (i.e. all songs since we did p.set_selection([""]) above
		# for each song, print artist name and title
		for row in self.shell.props.selected_source.props.base_query_model:
		 	entry = row[0]
		 	artist = self.shell.props.db.entry_get(entry, rhythmdb.PROP_ARTIST)
		 	song = self.shell.props.db.entry_get(entry, rhythmdb.PROP_TITLE)
			print artist + ' - ' + song
			
	def deactivate(self, shell):
		del self.shell
		print 'Bye world'
