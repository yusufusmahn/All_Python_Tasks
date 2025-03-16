def add_task(store, description):
	task = {"description": description}
	store.append(task)
	return "Task added"


def view_tasks(store):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		result = ""
		for task in store:
			result += f"{task['description']}\n"
		return result



def mark_task_as_completed(store, user):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		result = ""
		for task in store:
			result += f"[x]{task['description']}"
		return result
			


def delete_task(store, input):
	if len(store) == 0:
		return "No task added, Kindly select one to add a task"

	else:
		result = ""
		for task in store:
			if input in task:
				result -= f"[X]{task['description']}"
		return result			
			




def main():

	store = []
	
	print("TO-DO LIST MANAGER")
	print("=======================")
	
	while True:
		print("""
1. Add a task
2. View taks
3. Mark task as completed
4. Delete a task
5. Exit
""")

		choice = int(input("Select an option to continue: "))
		while choice not in {1,2,3,4,5}:
			choice = int(input("Invalid option, Kindly select options between 1 and 5: "))

		if choice == 1:
			description = input("Enter the task: ")
			result = add_task(store, description)
			print(result)

		elif choice == 2:

			result = view_tasks(store)
			print(result)

		elif choice == 3:
			user = input("Enter completed task: ")
			result = mark_task_as_completed(store, user)
			print(result)

		elif choice == 4:
			user = input("Enter completed task: ")
			result = delete_task(store, input)
			print(result)


		elif choice == 5:

			print("Exiting the app!!!")
			break



main()
