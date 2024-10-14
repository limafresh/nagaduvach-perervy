from tkinter import Tk, Label, Button, messagebox

# Створення вікна
root = Tk()
root.title("Нагадувач перерви")
root.resizable(0, 0)

# Оголошення змінних
remaining_time = 1200  # 20 хвилин у секундах
is_timer_running = False
number_of_twenty = 0


# Функції
def update_timer():
    global is_timer_running, remaining_time, number_of_twenty
    if is_timer_running:
        if remaining_time > 0:
            remaining_time -= 1
            # Ділення з остачею, 1-ше значення, mins - частка,
            # 2-ге, secs - остача
            mins, secs = divmod(remaining_time, 60)
            # 02 - відображається у 2-х цифрах
            time_label["text"] = f"{mins:02}:{secs:02}"
            root.after(1000, update_timer)
        else:
            is_timer_running = False
            remaining_time = 1200
            time_label["text"] = "20:00"
            start_btn["state"] = "normal"
            pause_btn["state"] = "disabled"
            number_of_twenty += 1
            number_of_twenty_label["text"] = (
                f"Кількість 20-хвилинок: {number_of_twenty}"
            )
            messagebox.showinfo(
                "Перерва!",
                "Подивіться 20 секунд на предмети, що на відстані 6 метрів!"
            )


def start():
    global is_timer_running, remaining_time
    if not is_timer_running:
        is_timer_running = True
        start_btn["state"] = "disabled"
        pause_btn["state"] = "normal"
        update_timer()


def pause():
    global is_timer_running
    if is_timer_running:
        is_timer_running = False
        pause_btn["text"] = "Продовжити"
    else:
        is_timer_running = True
        pause_btn["text"] = "Пауза"
        update_timer()


# Створення віджетів
instruction = Label(text='Коли сядете за екран, натисніть "Старт"')
instruction.pack()

start_btn = Button(text="Старт", command=start)
start_btn.pack()

pause_btn = Button(text="Пауза", command=pause)
pause_btn.pack()
pause_btn["state"] = "disabled"

time_label = Label(text="20:00")
time_label.pack()

number_of_twenty_label = Label(text="Кількість 20-хвилинок: 0")
number_of_twenty_label.pack()

root.mainloop()
