import wx
from datetime import datetime, date

# ----------------- Helper Functions --------------------

def calculate_age(event):
    try:
        bday = int(day.GetValue())
        bmonth = int(month.GetValue())
        byear = int(year.GetValue())
        dob = date(byear, bmonth, bday)
        today = date.today()

        # Years / Months / Days
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            prev_month = (today.month - 1) or 12
            prev_year = today.year if today.month != 1 else today.year - 1
            days += (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days

        if months < 0:
            years -= 1
            months += 12

        # Total days lived
        total_days = (today - dob).days

        # Next birthday
        next_birthday = date(today.year, bmonth, bday)
        if next_birthday < today:
            next_birthday = date(today.year + 1, bmonth, bday)
        days_left = (next_birthday - today).days

        # Output text
        output.SetLabel(
            f"Age: {years} Years  {months} Months  {days} Days\n\n"
            f"Total Days Lived: {total_days}\n"
            f"Next Birthday In: {days_left} days 🎂"
        )
    except:
        output.SetLabel("⚠️error")

def update_clock(event):
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.SetLabel(f"🕒 {current_time}")

# ----------------------- GUI ----------------------------

app = wx.App()
frame = wx.Frame(None, title="Modern Age Calculator", size=(430, 600),
                 style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

panel = wx.Panel(frame)
panel.SetBackgroundColour("#1e1e1e")

font1 = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
font2 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

title = wx.StaticText(panel, label="✨ AGE CALCULATOR ✨")
title.SetForegroundColour("white")
title.SetFont(font1)

# Input fields
day = wx.TextCtrl(panel, size=(60, 35), style=wx.TE_CENTER)
month = wx.TextCtrl(panel, size=(60, 35), style=wx.TE_CENTER)
year = wx.TextCtrl(panel, size=(80, 35), style=wx.TE_CENTER)

for box in [day, month, year]:
    box.SetBackgroundColour("#2E2E2E")
    box.SetForegroundColour("white")
    box.SetFont(font2)

dob_label = wx.StaticText(panel, label="Enter Your Birth Date (DD  MM  YYYY)")
dob_label.SetForegroundColour("white")

# Calculate button
btn = wx.Button(panel, label="Calculate Age", size=(200, 40))
btn.SetBackgroundColour("#4caf50")
btn.SetForegroundColour("white")
btn.SetFont(font2)
btn.Bind(wx.EVT_BUTTON, calculate_age)

# Output area
output = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER)
output.SetForegroundColour("#00e676")
output.SetFont(font2)

# Live Clock
clock_label = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER)
clock_label.SetForegroundColour("#80d8ff")
clock_label.SetFont(font2)

# Timer for clock
timer = wx.Timer(panel)
panel.Bind(wx.EVT_TIMER, update_clock, timer)
timer.Start(1000)  # 1 second

# ---------------- Layout ------------------

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 20)
sizer.Add(clock_label, 0, wx.ALIGN_CENTER | wx.TOP, 10)
sizer.Add(dob_label, 0, wx.ALIGN_CENTER | wx.TOP, 30)

row = wx.BoxSizer(wx.HORIZONTAL)
row.Add(day, 0, wx.RIGHT, 10)
row.Add(month, 0, wx.RIGHT, 10)
row.Add(year, 0)
sizer.Add(row, 0, wx.ALIGN_CENTER | wx.TOP, 10)

sizer.Add(btn, 0, wx.ALIGN_CENTER | wx.TOP, 30)
sizer.Add(output, 0, wx.ALIGN_CENTER | wx.TOP, 40)

panel.SetSizer(sizer)

frame.Centre()
frame.Show()
app.MainLoop()

