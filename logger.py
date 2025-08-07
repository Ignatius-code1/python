def write_file(f_name,tx):
    with open(f_name, 'a') as file:
        file.write(f"{tx} \n")

write_file(f_name="logger.txt", tx="This is a log message.")