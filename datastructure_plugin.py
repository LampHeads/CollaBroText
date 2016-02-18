

import  sublime,sublime_plugin, json, uuid, subprocess
from datetime import datetime

list_of_threads = []
new_list_of_threads = []


class Thread:

	def __init__(self, region, comment_string = None,list_of_comments = [], is_resolved = False):
		self.thread_key = str(uuid.uuid4())
		#print(list(region))
		getting_region = list(region.split(','))
		#print(getting_region)

		self.region = sublime.Region(int(getting_region[0]),int(getting_region[1]))
		self.is_resolved = is_resolved



		if (comment_string == None):
			self.list_of_comments = list_of_comments
		else:
			cobj = Comment(comment_string)
			list_of_comments.append(cobj)
			self.list_of_comments = list_of_comments
			#write_thread()


	def find_thread(region):
		for x in list_of_threads:
			if (x.region == region):
				return x





	@staticmethod
	def write_list_threads(plist_of_threads):	 
		#jsonlist = [self.thread_key, self.region, self.list_of_comments]
		with open('/home/shantanu/Desktop/datastructurework/datafile.json', 'w') as f:
			#f.write('[\n')
			#self.write_thread()
			json.dump([ThreadEncoder(indent = 1).default(x) for x in plist_of_threads], f, cls = ThreadEncoder, indent = 1)
			#f.write('\n')
			#f.write(']')


	@staticmethod
	def read_thread():
		with open('/home/shantanu/Desktop/datastructurework/datafile.json', 'r') as fl:
			new_list_of_threads = json.load(fl)
			return(new_list_of_threads)

			# self.thread_key = data["thread_key"]
			# self.region = data["region"]
			# self.is_resolved = data["is_resolved"]
			# self.list_of_comments = data["list_of_comments"]

	@staticmethod
	def converting_from_file_to_new_list_of_threads(pnew_list_of_threads):
		# print(pnew_list_of_threads)
		pnewer_list_of_threads = [Thread( x["region"], list_of_comments = x["list_of_comments"], is_resolved = x["is_resolved"]) for x in pnew_list_of_threads]
		return pnewer_list_of_threads









	def add_thread(self, plist_of_threads):
		plist_of_threads.append(self)


	def add_comment(self, comment_string):
		cobj = Comment(comment_string)
		self.list_of_comments.append(cobj)





	# def highlighter(self, view):
	# 	# reg = [self.region]
	# 	for region in view.sel() :
	# 		#reg.append(region)
	# 		view.add_regions('thread_key %d' % self.thread_key, [region], 'string', '', sublime.PERSISTENT)
	# 		return region



	# def write__new_thread(self):	 
	# 	#jsonlist = [self.thread_key, self.region, self.list_of_comments]
	# 	with open('/home/shantanu/.config/sublime-text-3/Packages/User/datafile.json', 'a') as f:
	# 		json.dump(self, f, cls = ThreadEncoder, indent = 1)
	# 		f.write('\n')



	# def as_Thread(self,dic):
	# 	return Thread(dic["thread_key"], dic["region"], dic["list_of_comments"], dic["is_resolved"])



class Comment:
	
	def __init__(self, comment_string):
		
		git_uname = subprocess.Popen("git config user.name", shell=True, stdout=subprocess.PIPE).stdout.read()
		self.username = git_uname.decode("utf-8")
		
		self.comment_key = str(uuid.uuid4())

		self.comment_string = comment_string

		timestamp_string = str(datetime.now())
		self.timestamp = timestamp_string[0:timestamp_string.rfind(".")]




class ThreadEncoder(json.JSONEncoder):
	# def getting_comments_list(self, obj):
	# 	thislist = []
	# 	for w in obj.list_of_comments:
	# 		thislist.append(CommentEncoder.default(w))
	# 	return thislist



	def default(self, obj):
		changed_region = str(obj.region)[1:-2]
		if isinstance(obj, Thread):
			return {"thread_key":obj.thread_key, "region":changed_region, "is_resolved":obj.is_resolved, "list_of_comments":[CommentEncoder(indent = 1).default(x) for x in obj.list_of_comments]}#json.dumps(obj.list_of_comments, cls=CommentEncoder)}
		return json.JSONEncoder.default(self, obj)




class CommentEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Comment):
			return {"username":obj.username,"comment_key":obj.comment_key, "comment_string":obj.comment_string, "timestamp":obj.timestamp}
		return json.JSONEncoder.default(self, obj)










class WritetestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# c = Comment('mr3',123456, 'third Comment', 7)
		# d = Comment('mr4',456789, '4th Comment', 8)
		# t = Thread(16, "17,18", [c, d])
		# u = Thread(18, "19,20", [c, d])
		# v = Thread(20, "21,22", [c, d])
		# w = Thread(21,"0,0",[c, d])

		# e = Comment('mr7',123456712321,'another comment', 11)

		# t.add_thread(list_of_threads)
		# # print(list_of_threads)
		# u.add_thread(list_of_threads)
		# # print(list_of_threads)
		# v.add_thread(list_of_threads)
		# # print(list_of_threads)

		# v.add_comment(e)


		# # t.highlighter(self.view)
		# # u.highlighter(self.view)
		# # v.highlighter(self.view)

		# # w.region = w.highlighter(self.view)

		# Thread.write_list_threads(list_of_threads)
		# yo = Thread.read_thread()
		# new_list_of_threads = Thread.converting_from_file_to_new_list_of_threads(yo)

		# print(new_list_of_threads)



		# # t.create_list_threads()
		# # t.write_thread()

		# # newobj = Thread('','',[])
		# # newobj.read_thread()
		# # print(newobj.list_of_comments)









		# c = Comment('mr3','third Comment', 7)
		# d = Comment('mr4', '4th Comment', 8)
		# t = Thread( "17,18", [c, d])
		# u = Thread( "19,20", [c, d])
		# v = Thread( "21,22", [c, d])
		# w = Thread( "0,0",[c, d])

		# e = Comment('mr7', 'another comment', 11)

		# t.add_thread(list_of_threads)
		# # print(list_of_threads)
		# u.add_thread(list_of_threads)
		# # print(list_of_threads)
		# v.add_thread(list_of_threads)
		# # print(list_of_threads)

		# v.add_comment(e)


		# # t.highlighter(self.view)
		# # u.highlighter(self.view)
		# # v.highlighter(self.view)

		# # w.region = w.highlighter(self.view)

		# Thread.write_list_threads(list_of_threads)
		# yo = Thread.read_thread()
		# new_list_of_threads = Thread.converting_from_file_to_new_list_of_threads(yo)

		# print(new_list_of_threads)



		t = Thread( "17,18", "This is a first comment")

		t.add_thread(list_of_threads)
		t.add_comment("second comment")


		Thread.write_list_threads(list_of_threads)
		yo = Thread.read_thread()
		new_list_of_threads = Thread.converting_from_file_to_new_list_of_threads(yo)

		print(new_list_of_threads)





