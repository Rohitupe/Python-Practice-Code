from win10toast import ToastNotifier

n = ToastNotifier()

n.show_toast("Rohit Tupe", "Hi, This is a Windows Toast Message",
             duration=10, icon_path="images/ghost.ico", threaded=True)
