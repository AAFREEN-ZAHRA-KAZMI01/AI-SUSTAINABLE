import streamlit as st
import pandas as pd
from datetime import datetime

def run():
    st.header('Predictive Scheduling (AI Calendar for Machines)')
    st.write('Auto-generated weekly machine operation calendar with export options.')

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    schedule = {
        'Machine A': ['OFF 10 PM–6 AM'] * 7,
        # Machine B runs Tue-Fri 11 AM-4 PM, OFF other days
        'Machine B': ['OFF'] + ['Run 11 AM–4 PM'] * 4 + ['OFF'] * 2
    }

    df_schedule = pd.DataFrame(schedule, index=days)
    st.table(df_schedule)

    # CSV export
    csv = df_schedule.to_csv()
    st.download_button('Download Schedule CSV', data=csv, file_name='machine_schedule.csv', mime='text/csv')

    # Simple ICS export (weekly event for Machine B Tue-Fri)
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\n"
    today = datetime.today()
    for i, day in enumerate(days[:5]):  # Mon-Fri
        date_str = (today).strftime('%Y%m%d')
        ics_content += (
            "BEGIN:VEVENT\n"
            "SUMMARY:Machine B Operation\n"
            f"DTSTART;TZID=Asia/Karachi:{date_str}T110000\n"
            f"DTEND;TZID=Asia/Karachi:{date_str}T160000\n"
            "RRULE:FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR\n"
            "END:VEVENT\n"
        )
    ics_content += "END:VCALENDAR"

    st.download_button('Download Schedule ICS', data=ics_content, file_name='machine_schedule.ics', mime='text/calendar')
