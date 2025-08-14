To turn your Flask application into a standalone executable (`.exe`) and have it run automatically when Windows starts, you can use a combination of tools and system settings.

### 1\. Create a Standalone Executable

The most common way to package a Python application into an executable is by using a tool called **PyInstaller**. It bundles your Python code, dependencies, and a Python interpreter into a single file or folder.

#### Steps to Use PyInstaller:

1.  **Install PyInstaller:** Make sure your virtual environment is active and then install PyInstaller.

    ```bash
    pip install pyinstaller
    ```

2.  **Create the Executable:** Navigate to the `model` directory where your `app.py` file is located and run the following command. The `--onefile` flag creates a single `.exe` file.

    ```bash
    pyinstaller --onefile app.py
    ```

After running the command, PyInstaller will create a new directory called `dist`. Inside this directory, you will find `app.exe`, which is your standalone application.

**Important:** This executable still requires the Ollama server to be running. It only packages your Flask app, not the Ollama server itself.

-----

### 2\. Run the App on Windows Startup

To make your application and the Ollama server run automatically when your computer starts, you can use the Windows Task Scheduler.

#### Steps to Automate with Task Scheduler:

1.  **Open Task Scheduler:** Press the **Windows key**, type `Task Scheduler`, and press Enter.

2.  **Create a New Task:**

      * In the right-hand pane, click **"Create Task..."**.
      * On the **General** tab, give your task a name, like "Ollama Chat App".
      * Check the box for **"Run with highest privileges"**.

3.  **Set the Trigger:** This tells Windows when to run the task.

      * Go to the **Triggers** tab and click **"New..."**.
      * In the "Begin the task" dropdown, select **"At startup"**. This ensures the task runs as soon as Windows boots.
      * Click **OK**.

4.  **Set the Actions:** This is where you specify what commands to run. You will need to create two separate actions: one for the Ollama server and one for your Flask app.

      * **Action 1: Start Ollama Server:**

          * Go to the **Actions** tab and click **"New..."**.
          * In the "Action" dropdown, select **"Start a program"**.
          * For "Program/script", enter the full path to your Ollama executable. The default path is often `C:\Program Files\Ollama\ollama.exe`.
          * Click **OK**.

      * **Action 2: Start Your Flask App Executable:**

          * Click **"New..."** again.
          * For "Program/script", enter the full path to your `app.exe` file (e.g., `C:\secure-web-llm\model\dist\app.exe`).
          * Click **OK**.

5.  **Review and Save:** Go to the **Conditions** and **Settings** tabs to adjust any other preferences, such as whether to run on battery power. Finally, click **OK** to save the task.

Now, whenever you restart your computer, Windows will automatically launch both the Ollama server and your Flask application, making it accessible at `http://127.0.0.1:5000` without any manual intervention.