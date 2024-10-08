import password_generator
import dropbox_IO_module as dropbox
import help


def main():
	# dropbox.update_password()
	print("Get strong passwords quickly and store them offline!")
	while True:
		user_input = input("Input task: ").lower().strip()
		if user_input == "gen pass":
			password_generator.random_engine()
		elif user_input == "show services":
			password_generator.password_show(services=True)
		elif user_input == "show logins":
			password_generator.password_show(login=True)
		elif user_input == "manual":
			password_generator.manually_input()
		elif user_input == "search":
			service = input("Input service: ")
			print(password_generator.show_detailed(service=service))
		elif user_input == "del pass":
			password_generator.password_show(services=True)
			password_to_delete = input("Enter service to whom password should be deleted: ")
			password_generator.show_detailed(service=password_to_delete.capitalize(), login=None, delete=True)
		elif user_input == "help":
			print(help.help_sting)
		elif user_input == "upload":
			dropbox.upload_password()
		elif user_input == "quit":
			return
		else:
			print("Unknown command")


if __name__ == "__main__":
	main()
