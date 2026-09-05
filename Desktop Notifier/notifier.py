import time
import notify2
from topnews import topStories

# path to notification window icon
icon_path = r"C:\Users\khanu\Downloads\news_icon.png"

# fech news items
newsitems = topStories()

# initialise the d bus connection
notify2.init("New Notifier")

# create notification object
n = notify2.Notification(None, icon=icon_path)

# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# set timeout for notification
n.set_timeout(10000)

for newsitem in newsitems:
    # update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notification on screen
    n.show()

    # short delay between notifications
    time.sleep(15)
