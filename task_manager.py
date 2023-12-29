tasks = []


def create_task(title, description):
    global tasks
    tasks.append((title, description))
    print(f"Создана новая задача: {title}")
