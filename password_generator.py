import json
import time
import random
import pyperclip
import os
import json_db_workers as json_db

json_pass_file = os.path.join(os.getcwd(), 'password.json')

json_db.check_create_data_base(json_pass_file, {'Passwords': []})


def search_existence(services):
	password_list = json_db.read_json(json_pass_file, "Passwords")

	for item in enumerate(password_list):
		if item[1]["Service"] == services:
			return item[0]


def random_engine():
	time_addition = time.localtime()  # добавление временной метки
	time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_addition)
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	literal = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
	           "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
	capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
	            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
	list_symbols = ["?", "&", "!", "%", "#", "*", "$", "<", ">", "(", ")", "-", "+", "="]

	service_name = input("Entry the service name: ").capitalize()
	login_name = input("Entry the login: ").capitalize()

	n = 0
	try:
		n = int(input("Enter length of the password: "))
	except ValueError as e:
		print("ERROR: ", e)

	shuffled_result = ""
	for x in range(n):  # генерация рандомного пароля
		x = random.choice(numbers)
		y = random.choice(literal)
		z = random.choice(capitals)
		a = random.choice(list_symbols)
		result_list = [x, y, z, a]
		random.shuffle(result_list)
		shuffled_result += "".join(map(str, result_list))
	# строка перемешивает случайно выбранные символы для избежания повторяющихся паттернов

	password_dict = {"Service": service_name,
	                 "Login": login_name,
	                 "Password": shuffled_result[:n],
	                 "Time stamp": time_string}
	pyperclip.copy(shuffled_result[:n])  # метод копирования текста в буфер обмена
	try:
		if search_existence(service_name) is not None:
			index = search_existence(service_name)
			data = json_db.read_json(json_pass_file, "Passwords")
			data[index] = password_dict
			json_db.update_dict({"Passwords": data}, json_pass_file)
		else:
			json_db.append_data_json("Passwords", password_dict, json_pass_file)
		return True
	except Exception as e:
		print(e)
		return False


def password_show(services=False, login=False):
	password_list = json_db.read_json(json_pass_file, "Passwords")
	
	
	login_list = []

	if services:
		for item in password_list:
			print(f"{item['Service']}: {item['Description']}")
	if login:
		for item in password_list:
			login_list.append(item['Login'])
		print(sorted(login_list))


def manually_input():
	time_addition = time.localtime()  # добавление временной метки
	time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_addition)
	print("Enter all fields:")
	service = input("Service name: ")
	login = input("Login name: ")
	password = input("Password: ")
	password_dict = {"Service": service,
	                 "Login": login,
	                 "Password": password,
	                 "Time stamp": time_string}
	try:
		if search_existence(service) is not None:
			index = search_existence(service)
			data = json_db.read_json(json_pass_file, "Passwords")
			data[index] = password_dict
			json_db.update_dict({"Passwords": data}, json_pass_file)
		else:
			json_db.append_data_json("Passwords", password_dict, json_pass_file)
		return True
	except Exception as e:
		print(e)
		return False


def show_detailed(service="", login=None):
	password_list = json_db.read_json(json_pass_file, "Passwords")
	
	if service:
		service_names = [item['Service'].lower() for item in password_list]
		try:
			find_service = service_names.index(service.lower())
			pyperclip.copy(password_list[find_service]['Password'])
			print("Password copied in the clipboard")
			return json.dumps(password_list[find_service], indent=2)
		except ValueError:
			return "There is no such service or you misspelled"
			
		
	if login:
		for item in password_list:
			if item['Login'] == login:
				pyperclip.copy(item['Password'])
				print(f"{item['Service']} {item['Login']} {item['Password']} {item['Time stamp']}")
			


def search_password(service=""):
	password_list = json_db.read_json(json_pass_file, "Passwords")

	for item in password_list:
		if service.lower() == item["Service"].lower():
			return json.dumps(item, indent=2)



