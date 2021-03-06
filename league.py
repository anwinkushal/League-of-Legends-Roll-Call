import sys
import ctypes
import pyautogui
import pkg_resources.py2_warn


def run_as_admin(argv=None , debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys , '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str , argv[1:])
    else:
        arguments = map(str , argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print('Command line: ' , executable , argument_line)
    ret = shell32.ShellExecuteW(None , u"runas" , executable , argument_line , None , 1)
    if int(ret) <= 32:
        return False
    return None
def league_roll_call():
    # accept queue button
    accept_button = None

    # 'in queue' label
    queue_label = None

    role = input('Enter Role: ')

    print('Running Stay at Client')

    while True:

        # keep searching for the 'in queue label' to know that the user is in queue
        while queue_label is None:

            try:
                queue_label = pyautogui.locateOnScreen('./res/queue.png' , confidence=0.8)
            except:
                pass

        # while queue label is present
        # meaning we are not in champ select yet
        while queue_label is not None:

            queue_label = pyautogui.locateOnScreen('./res/queue.png' , confidence=0.8)

            # keep searching for accept button
            while accept_button is None:
                try:
                    accept_button = pyautogui.locateOnScreen('./res/accept-queue.png' , confidence=0.8)
                except:
                    pass

            # get the location of the accept button
            accept_location = pyautogui.center(accept_button)

            # click it
            pyautogui.click(accept_location)

        chat_box = None

        # search for the chat box
        while chat_box is None:
            try:
                chat_box = pyautogui.locateOnScreen('./res/chat-box.png' , confidence=0.8)
            except:
                pass

        # get the location of the chat box
        chat_location = pyautogui.center(chat_box)

        # click it
        pyautogui.click(chat_location)

        # spam the role in the chat box
        for i in range(4):
            pyautogui.write(role)
            pyautogui.press('enter')

        print('Script done! Now exiting...')

        break



ret = run_as_admin()
if ret is True:
    league_roll_call()
else:print('Error(ret=%d): cannot elevate privilege.' % (ret ,))
