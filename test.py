import subprocess
import webbrowser

def openCommand(userquery):
    userquery = userquery.replace(Assistantname, "")
    userquery = userquery.replace("open", "")
    userquery = userquery.strip().lower()

    app_name = userquery

    if app_name != "":
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                say("Opening " + userquery)
                file_path = results[0][0]
                try:
                    subprocess.run(['xdg-open', file_path], check=True)
                except subprocess.CalledProcessError as e:
                    say(f"Error opening file: {e}")

            else:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    url = results[0][0]
                    say("Opening " + userquery)
                    try:
                        print(f"Attempting to open URL: {url}")  # Debugging line
                        webbrowser.open(url)
                    except Exception as e:
                        say(f"Error opening URL: {e}")

                else:
                    say("Could not find the application or file. Attempting to open with subprocess.")
                    try:
                        subprocess.run(userquery, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        say(f"Error opening application: {e}")

        except Exception as e:
            say(f"Something went wrong: {e}")
