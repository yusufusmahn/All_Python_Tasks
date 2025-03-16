import unittest
import to_do_list_manager

class TestToDoListManagerFunction(unittest.TestCase):



	def test_to_add_task(self):
		store = []
		actual = to_do_list_manager.add_task(store, "shopping")
		result = "Task added"
		self.assertEqual(actual, result)
	
	
	def test_to_add_multiple_tasks(self):
		store = []
		description = "shopping","exercise"
		actual = to_do_list_manager.add_task(store, description)
		result = "Task added"
		self.assertEqual(actual, result)


	def test_no_task(self):
		store = []
		actual = to_do_list_manager.view_tasks(store)
		result = "No task added, Kindly select one to add a task"
		self.assertEqual(actual, result)


	def test_to_mark_as_complete_when_no_task_added(self):
		store = []
		actual = to_do_list_manager.mark_task_as_completed(store, "shopping")
		result = "No task added, Kindly select one to add a task"
		self.assertEqual(actual, result)


	def test_to_delete_task_when_no_task_added(self):
		store = []
		actual = to_do_list_manager.delete_task(store, "shopping")
		result = "No task added, Kindly select one to add a task"
		self.assertEqual(actual, result)



	def test_to_mark_task_as_complete(self):
		store = []
		actual = to_do_list_manager.mark_task_as_completed(store, "shopping")
		result = "[X]shopping"
		self.assertEqual(actual, result)












