def copy_file(command: str) -> None:
    _, source_file, target_file = command.split()

    if source_file == target_file:
        return

    with open(source_file, "r", encoding="utf-8") as file_in, \
         open(target_file, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
