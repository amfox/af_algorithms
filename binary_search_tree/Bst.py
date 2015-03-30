#coding=utf-8

class Node( object ) :
	def __init__( self, key, left=None, right=None ) :
		self.val = key
		self.less = left
		self.more = right	
	def __init__( self, first=None ) :
		self.root = None
		if first is None :
			return
		elif isinstance( first, list ) :
			self._add_multiple( first )
		else :
			self.add( first )
	def g_less( self ) :
		return self.less
	def g_more( self ) :
		return self.more
	def change_less( self, another ) :
		self.less = another
	def change_more( self, another ) :
		self.more = another
	def g_val( self ) :
		return self.val

	def change_val( self, new_key ) :
		self.val = new_key
	def __eq__( self, another ) :
		return self.val == another.val

	def __gt__( self, another ) :
		return self.val > another.val

	def __lt__( self, another ) :
		return self.val < another.val
	def am_leaf( self ) :
		return self.less is None and self.more is None

	def less_is_empty( self ) :
		return self.less is None

	def more_is_empty( self ) :
		return self.more is None
class Bst( object ) :
	def __init__( self, key, left=None, right=None ) :
		self.val = key
		self.less = left
		self.more = right	
	def __init__( self, first=None ) :
		self.root = None
		if first is None :
			return
		elif isinstance( first, list ) :
			self._add_multiple( first )
		else :
			self.add( first )
	def add( self, wanted ) :
		if isinstance( wanted, list ) :
			self._add_multiple( wanted )
		elif self.is_empty() :
			self.root = Node( wanted )
		else :
			insertion = Node( wanted )
			self._add_leaf( self.root, insertion )
	def _add_multiple( self, wanted_vals ) :
		for val in wanted_vals :
			self.add( val )
	def _add_leaf( self, comparison, new_node ) : 
		'currently, not checking until I enter'
		if comparison == new_node :
			return # no duplicates
		elif comparison > new_node :
			if comparison.less_is_empty( ) :
				comparison.change_less( new_node )
			else :
				self._add_leaf( comparison.g_less( ), new_node )
		else :
			if comparison.more_is_empty( ) :
				comparison.change_more( new_node )
			else :
				self._add_leaf( comparison.g_more( ), new_node )
	def confirm( self, desire ) :
		if self.is_empty() :
			return False
		elif self.root.g_val() == desire :
			return True
		else :
			fake = Node( desire )
			result = self._find( self.root, fake )
			if result is None :
				return False
			else : # found
				return True	
	def _find( self, maybe, unconfirmed ) :
		if maybe < unconfirmed :
			maybe = maybe.g_more()
			if maybe is None :
				return maybe # failure
			elif maybe == unconfirmed :
				return maybe # success
			else :
				return self._find( maybe, unconfirmed )
		else : # maybe > unconfirmed
			maybe = maybe.g_less()
			if maybe == unconfirmed or maybe is None :
				return maybe
			else :
				return self._find( maybe, unconfirmed )
	def delete( self, unwanted_val ) :
		if self.is_empty() :
			return
		elif self.root.g_val() == unwanted_val :
			self._delete_root()
		else :
			obsolete = Node( unwanted_val )
			ancestor_stack = [ ]
			ancestor_stack = self._path_to_obsolete( obsolete, self.root, ancestor_stack )
			if ancestor_stack[ -1 ] is None :
				return
			else :
				self._perform_delete( ancestor_stack )
	def _perform_delete( self, ancestor_stack ) :
		o_less_Leaf = True
		obsolete = ancestor_stack.pop( )
		parent = ancestor_stack.pop( )
		o_was_less = obsolete < parent
			def _delete_root( self ) :
				fake = Node( self.root.g_val() + self.root.g_val() )
				fake_stack = [fake, self.root]
				self._perform_delete( fake_stack )
				if fake.less_is_empty() :
					self.root = fake.g_more()
				else :
					self.root = fake.g_less()
		if obsolete.am_leaf() :
			self._update_parent( parent_of_o, None, o_was_less )
		elif obsolete.less_is_empty() :
			self._replace_with_solo( parent, o_was_less, obsolete, o_less_Leaf )
		elif obsolete.more_is_empty() :
			self._replace_with_solo( parent, o_was_less, obsolete, not o_less_Leaf )
		else : # two children
			self._replace_with_two_children( parent, o_was_less, obsolete )
	def _update_parent( self, parent, replacer, from_less ) :
		if from_less :
			parent.change_less( replacer )
		else :
			parent.change_more( replacer )
	def _replace_with_solo( self, parent, from_less, obsolete, o_less_Leaf ) :
		if o_less_Leaf :
			self._update_parent( parent_of_o, obsolete.g_more(), from_less )
		else : # more is empty
			self._update_parent( parent_of_o, obsolete.g_less(), from_less )
	def _replace_with_two_children( self, parent, from_less, obsolete ) :
		left_replace = obsolete.g_val() % 2 == 0 # magic, or use rand_bool( )
		if left_replace :
			replacer, reps_parent = self._max_and_parent( obsolete.g_less(), obsolete )
			self._less_replace_2_kid( parent, from_less, obsolete, replacer, reps_parent )
		else : # right_replace
			replacer, reps_parent = self._min_and_parent( obsolete.g_more( ), obsolete )
			self._more_replace_2_kid( parent, from_less, obsolete, replacer, reps_parent )
	def _less_replace_2_kid( self, parent, from_less, obsolete, replacer, reps_parent ) :
		if reps_parent is obsolete :
			replacer.change_more( obsolete.g_more() )
			o_less_Leaf = True
			self._replace_with_solo( parent, from_less, obsolete, not o_less_Leaf )
		else :
			self._update_parent( parent, replacer, from_less )
			replacer.change_more( obsolete.g_more() )
			reps_parent.change_more( replacer.g_less() )
			replacer.change_less( obsolete.g_less() )
	def _more_replace_2_kid( self, parent, from_less, obsolete, replacer, reps_parent ) :
		if reps_parent is obsolete :
			replacer.change_less( obsolete.g_less() )
			o_less_Leaf = True
			self._replace_with_solo( parent, from_less, obsolete, o_less_Leaf )
		else :
			self._update_parent( parent, replacer, from_less )
			replacer.change_less( obsolete.g_less() )
			reps_parent.change_less( replacer.g_more() ) # is this right?
			replacer.change_more( obsolete.g_more() )
	def _path_to_obsolete( self, obsolete, focus, ancestorStack ) :
		ancestorStack.append( focus )
		if focus is None or focus == obsolete :
			return ancestorStack
		else :
			if focus < obsolete :
				return self._path_to_obsolete( obsolete, focus.g_more( ), ancestorStack )
			else :
				return self._path_to_obsolete( obsolete, focus.g_less( ), ancestorStack )

	def _max_and_parent( self, a_child, a_root ) :
		if a_child.more_is_empty() :
			return a_child, a_root
		else :
			return self._max_and_parent( a_child.g_more(), a_child )

	def _min_and_parent( self, a_child, a_root ) :
		if a_child.less_is_empty() :
			return a_child, a_root
		# else :
		while not a_child.less_is_empty() :
			a_root = a_child
			a_child = a_child.g_less()
		return a_child, a_root
	def g_all_elements( self ) :
		everything = []
		if self.root is None :
			return everything
		else :
			everything = self._traverse( self.root, everything )
			return everything

	def _traverse( self, focus, container ) :
		'in order, obviously'
		if focus is None :
			return container
		else :
			container = self._traverse( focus.g_less(), container )
			container.push( focus.g_val() )
			container = self._traverse( focus.g_more(), container )
			return container

	def is_empty( self ) :
		return self.root is None

	def erase( self ) :
		self.root = None
	def pr_hV( self ) :
		if tree.is_empty() :
			print ">--"
		else :
			print "v"
			self._pr_90( [ self.root ] )

	def _pr_hV( self, pr_stack ) :
		vert = pr_stack.__len__() - 1
		if vert >= 0 :
			self._pr_90_links( pr_stack, vert + 1 )
			print
			self._pr_90_links( pr_stack, vert )
			pr_stack = self._pr_90_row( pr_stack )
			self._pr_90( pr_stack )

	def _pr_hV_links( self, pr_stack, vert ) : # test this addition
		for ind in range( 0, vert ) :
			nn = pr_stack[ ind ]
			if nn is None :
				print "  ",
			else :
				print "| ",

	def _pr_hV_row( self, pr_stack ) :
		## python print \n suppression substitutes a space
		row_str = []
		focus = pr_stack.pop()
		while not focus is None :
			row_str.append( str( focus.g_val() ) )
			if not focus.less_is_empty() :
				pr_stack.append( focus.g_less() )
			elif not focus.more_is_empty() :
				pr_stack.append( None ),		
			if not focus.more_is_empty() :
				row_str.append( "-" )
			focus = focus.g_more()
		row_str = ''.join( row_str ) # turn list to string.
		print row_str
		#self._pr_node_stack( pr_stack )
		pr_stack = self._strip_placeholders( pr_stack )
		return pr_stack

	def _strip_placeholders( self, pr_stack ) :
		'ie None'
		focus = None
		while pr_stack.__len__() > 0 :
			focus = pr_stack.pop()
			if not focus is None :
				pr_stack.append( focus )
				break
		return pr_stack

tree = Bst()
something_wrong = True
seems_okay = not something_wrong
status = seems_okay # at least initially
print "\n\t PROBLEMS"
status = node_should_work() or status
status = should_erase()  or status
status = should_insert( tree ) or status # propagates truth
status = should_confirm( tree ) or status
status = should_delete( tree ) or status
status = should_traverse( tree ) or status
if seems_okay :
	print "> Silent test run"
else :
	print "\n<> so go fix that"
#check_by_eye( tree )

def should_insert( tree ) :
	flag = should_add_to_empty( tree )
	flag = should_add_to_root_leaf( tree ) or flag
	flag = should_add_multiple( tree ) or flag
	flag = should_not_add_copy( tree ) or flag
	return flag
def should_add_to_empty( tree ) :
	if not tree.is_empty( ) :
		tree.erase( )
	root_v = 'aa'
	tree.add( root_v )
	if not tree.root.g_val() == root_v :
		print "I> didn't add val to empty tree"
		return something_wrong
	tree.erase( )
	return seems_okay
def should_add_to_root_leaf( tree ) :
	root_v = -12
	new_val = 21
	tree.add( root_v )
	tree.add( new_val )
	if tree.root.am_leaf( ) :
		print "I> didn't add val to a node"
		return something_wrong
	elif tree.root.more_is_empty() :
		print "I> added new node to opposite side"
		return something_wrong
	elif tree.root.g_more( ).g_val() != new_val :
		print "I> added to right side, wrong value"
		return something_wrong
	return seems_okay

def should_add_multiple( tree ) :
	#print "I> doesn't test multiple yet"
	tree.erase()
	root_val = .5
	l_child = .25
	lis = [root_val, l_child]
	tree.add(lis)
	if not tree.root.g_val() == root_val :
		print "I> multiple didn't deposit first val"
		return something_wrong
	elif not tree.root.g_less().g_val() == l_child :
		print "I> multiple didn't add second val"
		return something_wrong
	return seems_okay
def should_not_add_copy( tree ) :
	tree.erase()
	root_v = 'do'
	child = 're'
	tree.add( root_v )
	tree.add( root_v )
	if not tree.root.am_leaf() :
		print "I> added a second copy of a val"
		return something_wrong
	tree.add( child )
	tree.add( child )
	if not tree.root.g_more().am_leaf() :
		print "I> added redundant node to interior"
		return something_wrong
	tree.add( root_v )
	root_okay = tree.root.less_is_empty()
	child_okay = tree.root.g_more().am_leaf()
	if not root_okay or not child_okay :
		print "I> added redundant on second try"
		return something_wrong
	return seems_okay
def should_confirm( tree ) :
	tree.erase()
	root_v = 4
	val_yes = 5
	val_no = val_yes + val_yes
	bunch = [ root_v, 3, 6, val_yes]
	if tree.confirm( val_no ) :
		print "C> confirmed value when tree empty"
		return something_wrong
	tree.add( bunch )
	if not tree.confirm( root_v ) :
		print "C> didn't confirm root's value"
		return something_wrong
	elif not tree.confirm( val_yes ) :
		print "C> didn't find key in subtree"
		return something_wrong
	elif tree.confirm( val_no ) :
		print "C> tree thinks it contains an uninserted value"
		return something_wrong
	else :
		return seems_okay

def should_traverse( tree ) :
	tree.erase()
	bunch = [ 4, 2, 1, 3, 7, 5, 8 ]
	tree.add( bunch )
	bundle = tree.g_all_elements()
	bunch.sort()
	for elem in range( 0, bunch.__len__() - 1 )	:
		if not bundle[ elem ] == bunch[ elem ] :
			print "T> ret " + str( bundle[ elem ] ) + " is not supp " + str( bunch[ elem ] )
			print bundle
			return something_wrong
	tree.erase
	return seems_okay


