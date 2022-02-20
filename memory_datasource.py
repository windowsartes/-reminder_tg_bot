from message_data import ReminderData

class MemoryDataSource():
    def __init__(self):
        self.reminders = dict()

    def add_reminder(self, chat_id, message, time):
        message_data = ReminderData(message, time)
        if chat_id not in self.reminders.keys():
            self.reminders[chat_id] = list()
            self.reminders[chat_id].append(message_data)
        else:
            self.reminders[chat_id].append(message_data)
        return message_data