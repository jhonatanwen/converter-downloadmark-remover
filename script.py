import os


def main():
    act_path = os.getcwd()
    downloader_textmark = {"yt5s.io-", "y2meta.com-", "SnapSave.io - "}
    log_output = ""

    for file_name in os.listdir(act_path):
        if os.path.isfile(os.path.join(act_path, file_name)):
            for textmark in downloader_textmark:
                if file_name.startswith(textmark):
                    new_file_name = file_name.replace(textmark, "", 1)

                    os.rename(
                        os.path.join(act_path, file_name),
                        os.path.join(act_path, new_file_name)
                    )

                    log_output = log_output + f"File renamed: {file_name} -> {new_file_name}\n"

                    if(os.name != "nt"):
                        os.system("clear")
                        print(log_output)
                    if(os.name == "nt"):
                        os.system("cls")
                        print(log_output)



    if log_output == "":
        print("There's no file that need to be renamed!\n")
        input("-----------PRESS ENTER TO EXIT-----------")
        return

    input("-----------PRESS ENTER TO EXIT-----------")
    return

if __name__ == "__main__":
    main()