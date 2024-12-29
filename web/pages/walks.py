import streamlit as st
from streamlit_calendar import calendar


st.title("Walks")

tab1, tab2, tab3 = st.tabs([ "View All Walks", "Add a Walk", "Manage Walks" ])

# List all walks

with tab1:
    calendar_options = {
        "editable": True,
        "selectable": True,
        "headerToolbar": {
            "left": "today prev,next",
            "center": "title",
            "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
        },
        "slotMinTime": "06:00:00",
        "slotMaxTime": "18:00:00",
        "initialView": "resourceTimelineDay",
        "resourceGroupField": "walker",
        "resources": [
            {"id": "Ali", "walker": "Ali", "title": "Ali"},
        ],
    }
    calendar_events = [
        {
            "title": "Mika",
            "start": "2025-01-02T08:30:00",
            "end": "2025-01-0T09:30:00",
            "resourceId": "Ali",
        },
        {
            "title": "Betty",
            "start": "2025-01-02T10:00:00",
            "end": "2025-01-02T11:00:00",
            "resourceId": "Ali",
        },
        {
            "title": "Bertie",
            "start": "2025-01-03T11:30:00",
            "end": "2025-01-03T12:30:00",
            "resourceId": "Ali",
        }
    ]
    custom_css="""
        .fc-event-past {
            opacity: 0.8;
        }
        .fc-event-time {
            font-style: italic;
        }
        .fc-event-title {
            font-weight: 700;
        }
        .fc-toolbar-title {
            font-size: 2rem;
        }
    """

    calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
    st.write(calendar)
